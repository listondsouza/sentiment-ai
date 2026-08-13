from flask import Flask, render_template, request, jsonify
import joblib
import re
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)

MODEL_DIR = "models"

logistic_model = joblib.load(
    f"{MODEL_DIR}/logistic_model.pkl"
)

nb_model = joblib.load(
    f"{MODEL_DIR}/nb_model.pkl"
)

svm_model = joblib.load(
    f"{MODEL_DIR}/svm_model.pkl"
)

tfidf = joblib.load(
    f"{MODEL_DIR}/tfidf.pkl"
)

stop_words = joblib.load(
    f"{MODEL_DIR}/stop_words.pkl"
)

lemmatizer = joblib.load(
    f"{MODEL_DIR}/lemmatizer.pkl"
)

roberta_path = f"{MODEL_DIR}/roberta"

tokenizer = AutoTokenizer.from_pretrained(
    roberta_path
)

roberta_model = AutoModelForSequenceClassification.from_pretrained(
    roberta_path
)

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

roberta_model.to(device)
roberta_model.eval()

id2label = {
    0: "Negative",
    1: "Neutral",
    2: "Positive"
}


def clean_text(text):

    text = str(text).lower()

    text = re.sub(
        r"<.*?>",
        " ",
        text
    )

    text = re.sub(
        r"http\S+|www\S+",
        " ",
        text
    )

    text = re.sub(
        r"[^a-z\s]",
        " ",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    words = text.split()

    words = [
        word
        for word in words
        if word not in stop_words
    ]

    words = [
        lemmatizer.lemmatize(word)
        for word in words
    ]

    return " ".join(words)


def predict_sentiment(review):

    processed_text = clean_text(
        review
    )

    user_tfidf = tfidf.transform(
        [processed_text]
    )

    logistic_prediction = (
        logistic_model.predict(
            user_tfidf
        )[0]
    )

    nb_prediction = (
        nb_model.predict(
            user_tfidf
        )[0]
    )

    svm_prediction = (
        svm_model.predict(
            user_tfidf
        )[0]
    )

    roberta_input = tokenizer(
        review,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    roberta_input = {
        key: value.to(device)
        for key, value in roberta_input.items()
    }

    with torch.no_grad():

        outputs = roberta_model(
            **roberta_input
        )

    roberta_class = torch.argmax(
        outputs.logits,
        dim=1
    ).item()

    roberta_prediction = id2label[
        roberta_class
    ]

    predictions = [
        logistic_prediction,
        nb_prediction,
        svm_prediction,
        roberta_prediction
    ]

    counts = {}

    for prediction in predictions:

        counts[prediction] = (
            counts.get(prediction, 0) + 1
        )

    highest_count = max(
        counts.values()
    )

    if highest_count >= 3:

        final_sentiment = max(
            counts,
            key=counts.get
        )

        decision_method = "Majority Vote"

    elif highest_count == 2:

        tied = [
            sentiment
            for sentiment, count
            in counts.items()
            if count == 2
        ]

        if len(tied) == 1:

            final_sentiment = tied[0]
            decision_method = "Majority Vote"

        else:

            final_sentiment = roberta_prediction
            decision_method = "RoBERTa (2-2 Tie)"

    else:

        final_sentiment = roberta_prediction
        decision_method = "RoBERTa Default"

    return {
        "logistic": logistic_prediction,
        "naive_bayes": nb_prediction,
        "svm": svm_prediction,
        "roberta": roberta_prediction,
        "final": final_sentiment,
        "method": decision_method
    }


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    data = request.get_json()

    review = data.get(
        "review",
        ""
    ).strip()

    if not review:

        return jsonify({
            "error": "Please enter a review."
        }), 400

    result = predict_sentiment(
        review
    )

    return jsonify(result)


if __name__ == "__main__":

    app.run(
        debug=True
    )