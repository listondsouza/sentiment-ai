import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_path = "models/roberta"

print("Loading RoBERTa tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(
    model_path
)

print("RoBERTa tokenizer: OK")

print("Loading RoBERTa model...")

model = AutoModelForSequenceClassification.from_pretrained(
    model_path
)

print("RoBERTa model: OK")

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

model.to(device)

print("Device:", device)

text = "This product is absolutely amazing."

inputs = tokenizer(
    text,
    return_tensors="pt",
    truncation=True,
    padding=True,
    max_length=128
)

inputs = {
    key: value.to(device)
    for key, value in inputs.items()
}

model.eval()

with torch.no_grad():

    outputs = model(
        **inputs
    )

prediction = torch.argmax(
    outputs.logits,
    dim=1
).item()

print("RoBERTa prediction:", prediction)