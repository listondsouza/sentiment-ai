
============================================================
                    SENTIMENT AI
              DOWNLOAD & SETUP GUIDE
============================================================

This guide shows you how to download and run Sentiment AI.

Choose ONE of the three methods below.

A = Windows Command Prompt
B = Ubuntu Terminal
C = Visual Studio Code

============================================================
A. WINDOWS COMMAND PROMPT
============================================================


STEP 1 — Install Git

1. Open your web browser.

2. Go to the official Git website.

3. Download Git for Windows.

4. Install Git.

5. During installation, you can keep the default options.

6. When installation is finished, close the installer.


STEP 2 — Open Command Prompt

1. Press:

   Windows + R

2. Type:

   cmd

3. Press Enter.

A black window will appear.

This is Command Prompt.


STEP 3 — Check Git

Type:

   git --version

Press Enter.

You should see something similar to:

   git version 2.x.x

If you see a Git version, Git is installed correctly.


STEP 4 — Check Git LFS

Sentiment AI contains a large RoBERTa model.

Git LFS is needed to download it correctly.

Type:

   git lfs version

Press Enter.

If Git LFS is installed, you will see a version number.


STEP 5 — Install Git LFS if necessary

If the previous command says that Git LFS is not recognized:

1. Download and install Git LFS.

2. Close Command Prompt.

3. Open Command Prompt again.

4. Type:

   git lfs install

5. Press Enter.


STEP 6 — Choose where to download the project

For example, to put the project on your Desktop:

Type:

   cd %USERPROFILE%\Desktop

Press Enter.


STEP 7 — Download Sentiment AI

Type:

   git clone https://github.com/listondsouza/sentiment-ai.git

Press Enter.

Git will now download the project.

Wait until it finishes.


STEP 8 — Enter the project folder

Type:

   cd sentiment-ai

Press Enter.

You are now inside the Sentiment AI project.


STEP 9 — Download the large model

Type:

   git lfs pull

Press Enter.

Wait for it to finish.

This downloads the large RoBERTa model.


STEP 10 — Check that the model exists

Type:

   dir models\roberta

Press Enter.

You should see files including:

   model.safetensors
   config.json
   tokenizer.json

The file named:

   model.safetensors

should be very large.

This is the RoBERTa model.


STEP 11 — Check Python

Type:

   python --version

Press Enter.

You should see a Python version.

If Python is not installed, install Python first.


STEP 12 — Create the Python environment

Type:

   python -m venv .venv

Press Enter.

Wait for the command to finish.


STEP 13 — Activate the environment

Type:

   .venv\Scripts\activate

Press Enter.

You should now see:

   (.venv)

at the beginning of the command line.

For example:

   (.venv) C:\Users\YourName\Desktop\sentiment-ai>


STEP 14 — Install the required libraries

Type:

   python -m pip install --upgrade pip

Press Enter.

Then type:

   pip install -r requirements.txt

Press Enter.

Wait until installation finishes.


STEP 15 — Download NLTK resources

Type:

   python -c "import nltk; nltk.download('wordnet'); nltk.download('omw-1.4')"

Press Enter.

Wait until both downloads finish.


STEP 16 — Start Sentiment AI

Type:

   python app.py

Press Enter.

You should see something similar to:

   Running on http://127.0.0.1:5000


STEP 17 — Open the website

Open your web browser.

Type this into the address bar:

   http://127.0.0.1:5000

Press Enter.

Sentiment AI should now open.


STEP 18 — Stop the website

When you are finished:

1. Go back to Command Prompt.

2. Press:

   CTRL + C

The website will stop running.



============================================================
B. UBUNTU TERMINAL
============================================================


STEP 1 — Open Terminal

Press:

   CTRL + ALT + T

The Ubuntu Terminal will open.


STEP 2 — Check Git

Type:

   git --version

Press Enter.

You should see a Git version.


STEP 3 — Install Git if necessary

If Git is not installed, type:

   sudo apt update

Press Enter.

Then type:

   sudo apt install git git-lfs

Press Enter.

If Ubuntu asks for your password, type your Ubuntu password.

Your password will not appear while typing.

Press Enter.


STEP 4 — Enable Git LFS

Type:

   git lfs install

Press Enter.


STEP 5 — Check Python

Type:

   python3 --version

Press Enter.

You should see a Python version.


STEP 6 — Install Python if necessary

If Python is not installed, type:

   sudo apt update

Press Enter.

Then:

   sudo apt install python3 python3-venv python3-pip

Press Enter.

Wait for the installation to finish.


STEP 7 — Choose where to download the project

For example, go to your home folder:

   cd ~

Press Enter.


STEP 8 — Download Sentiment AI

Type:

   git clone https://github.com/listondsouza/sentiment-ai.git

Press Enter.

Wait for Git to finish downloading the project.


STEP 9 — Enter the project

Type:

   cd sentiment-ai

Press Enter.


STEP 10 — Download the large RoBERTa model

Type:

   git lfs pull

Press Enter.

Wait until it finishes.


STEP 11 — Check the model

Type:

   ls -lh models/roberta

Press Enter.

You should see:

   model.safetensors

The model file should be very large.


STEP 12 — Create the Python environment

Type:

   python3 -m venv .venv

Press Enter.

Wait for the command to finish.


STEP 13 — Activate the environment

Type:

   source .venv/bin/activate

Press Enter.

You should now see:

   (.venv)

at the beginning of the terminal.

For example:

   (.venv) user@computer:~/sentiment-ai$


STEP 14 — Upgrade pip

Type:

   python -m pip install --upgrade pip

Press Enter.


STEP 15 — Install the required libraries

Type:

   pip install -r requirements.txt

Press Enter.

Wait until installation finishes.


STEP 16 — Download NLTK resources

Type:

   python -c "import nltk; nltk.download('wordnet'); nltk.download('omw-1.4')"

Press Enter.

Wait until the downloads finish.


STEP 17 — Start Sentiment AI

Type:

   python app.py

Press Enter.

You should see:

   Running on http://127.0.0.1:5000


STEP 18 — Open the website

Open your web browser.

Enter:

   http://127.0.0.1:5000

Press Enter.

Sentiment AI should now open.


STEP 19 — Stop the website

When you are finished:

1. Go back to Terminal.

2. Press:

   CTRL + C

The website will stop running.



============================================================
C. VISUAL STUDIO CODE
============================================================


STEP 1 — Install Visual Studio Code

1. Download Visual Studio Code.

2. Install it.

3. Open Visual Studio Code.


STEP 2 — Install Git

Visual Studio Code uses Git to download the project.

Make sure Git is installed.

Open a terminal and type:

   git --version

Press Enter.

You should see a Git version.


STEP 3 — Install Git LFS

Type:

   git lfs version

Press Enter.

If Git LFS works, continue.

If it does not work, install Git LFS first.


STEP 4 — Open the VS Code Terminal

Inside Visual Studio Code:

1. Click:

   Terminal

2. Click:

   New Terminal

A terminal will appear at the bottom of VS Code.


STEP 5 — Check Python

Type:

   python --version

Press Enter.

You should see your Python version.


STEP 6 — Download the project

In the VS Code terminal, type:

   git clone https://github.com/listondsouza/sentiment-ai.git

Press Enter.

Wait for the download to finish.


STEP 7 — Open the project

Type:

   cd sentiment-ai

Press Enter.

Then type:

   code .

Press Enter.

The Sentiment AI project will open in VS Code.


STEP 8 — Download the large model

In the VS Code terminal, type:

   git lfs pull

Press Enter.

Wait until it finishes.

The RoBERTa model will now be downloaded.


STEP 9 — Check the project files

On the left side of VS Code you should see files and folders similar to:

   sentiment-ai
   │
   ├── models
   ├── templates
   ├── app.py
   ├── test_models.py
   ├── requirements.txt
   └── README.md


STEP 10 — Create the Python environment

In the VS Code terminal, type:

   python -m venv .venv

Press Enter.

Wait for it to finish.


STEP 11 — Activate the environment

If the VS Code terminal is PowerShell, type:

   .\.venv\Scripts\Activate.ps1

Press Enter.

You should see:

   (.venv)

at the beginning of the terminal.


STEP 12 — Select the Python interpreter

In VS Code:

1. Press:

   CTRL + SHIFT + P

2. Search for:

   Python: Select Interpreter

3. Click it.

4. Select the interpreter inside:

   .venv

It should look similar to:

   .venv\Scripts\python.exe


STEP 13 — Install the required libraries

In the VS Code terminal, type:

   python -m pip install --upgrade pip

Press Enter.

Then type:

   pip install -r requirements.txt

Press Enter.

Wait until installation finishes.


STEP 14 — Download NLTK resources

Type:

   python -c "import nltk; nltk.download('wordnet'); nltk.download('omw-1.4')"

Press Enter.

Wait until both resources are installed.


STEP 15 — Test the models

Type:

   python test_models.py

Press Enter.

The model test should complete successfully.


STEP 16 — Start the website

Type:

   python app.py

Press Enter.

You should see:

   Running on http://127.0.0.1:5000


STEP 17 — Open the website

Hold CTRL and click:

   http://127.0.0.1:5000

Or open your browser and type:

   http://127.0.0.1:5000


STEP 18 — Use Sentiment AI

1. Type a product review into the text box.

2. Submit the review.

3. The application will analyze the review.

4. The predictions from the models will appear.

5. The final sentiment will appear.


STEP 19 — Stop the website

When finished:

1. Go back to the VS Code terminal.

2. Press:

   CTRL + C

The website will stop running.


============================================================
IMPORTANT
============================================================

If you download the project again on another computer:

1. Clone the repository.
2. Run Git LFS.
3. Run git lfs pull.
4. Create the .venv environment.
5. Install requirements.txt.
6. Download the NLTK resources.
7. Run app.py.

Do NOT delete:

   models/

The models folder contains the trained sentiment models.

Do NOT delete:

   models/roberta/model.safetensors

This is the large RoBERTa model required by the application.


============================================================
END OF GUIDE
============================================================

