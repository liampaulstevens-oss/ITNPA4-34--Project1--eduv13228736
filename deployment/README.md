# Researchly Research Abstract Classifier – Deployment

This folder contains a Streamlit web app that classifies research abstracts as either **AI-related** or **classical research** (Questions 1 and 2).

## Files

| File | Purpose |
|---|---|
| `app.py` | The Streamlit web interface |
| `preprocessing.py` | The text cleaning function used during training, applied to user input before prediction |
| `model.pkl` | The trained pipeline (TF-IDF vectoriser + Random Forest with balanced class weights) |
| `requirements.txt` | Python packages and versions needed to run the app |

## Model

The deployed model is the best-performing configuration from Question 2:

- **Features:** TF-IDF (unigrams and bigrams, 5,000 features, minimum document frequency of 2)
- **Classifier:** Random Forest (300 trees) with `class_weight="balanced"` to handle the 79/21 class imbalance
- **Test set performance:** macro F1 0.883, accuracy 0.924, AI recall 0.787

## How to run

### 1. Requirements

- Python 3.11 or later
- The packages in `requirements.txt`. The scikit-learn version must match, since the saved model was trained with scikit-learn 1.9.0.

### 2. Get the code

Clone the repository and open the deployment folder:

```bash
git clone https://github.com/liampaulstevens-oss/ITNPA4-34--Project1--eduv13228736
cd ITNPA4-34--Project1--eduv13228736/deployment
```

Alternatively, download the repository as a ZIP from GitHub (**Code → Download ZIP**), unzip it and open a terminal in the `deployment` folder.

### 3. Install the packages

It is recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

pip install -r requirements.txt
```

### 4. Start the app

```bash
streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`. If it doesn't open automatically, copy that address into your browser.

On first run, the app downloads the NLTK resources it needs (tokeniser, stopwords and WordNet), so an internet connection is required the first time.

## Using the app

1. Paste a research abstract into the **"Enter research abstract:"** box.
2. Click **Classify Abstract**.
3. The prediction appears below: either **artificial intelligence** or **classical research**.

To stop the app, press `Ctrl + C` in the terminal.

## Troubleshooting

| Problem | Solution |
|---|---|
| `File does not exist: app.py` | The terminal is not in the `deployment` folder. Use `cd` to move into it, and check with `ls` (macOS/Linux) or `dir` (Windows). |
| `FileNotFoundError: model.pkl` | Make sure `model.pkl` is in the same folder as `app.py`. |
| Errors or warnings when loading the model | Install the exact scikit-learn version: `pip install scikit-learn==1.9.0` |
| `Resource punkt not found` | Run the app once with an internet connection so NLTK can download its resources. |
| Port 8501 is already in use | Streamlit will use the next free port (e.g. 8502); check the address printed in the terminal. |
