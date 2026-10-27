# ITNPA Project 1 – Text Classification, Summarisation and Topic Modelling

**Student:** Liam Stevens EDUV13228736
**Module:** ITNPA4-34

This repository contains the code, data, outputs and documentation for Project 1.

## Repository structure

```
├── data/
│   ├── research_abstracts.json      Labelled research abstracts (Questions 1–2)
│   └── research_corpus/             Five research articles (Questions 3–4)
├── notebooks/
│   ├── Q1_Q2_classification.ipynb   Cleaning, feature analysis, models and enhancement
│   └── Q3_Q4_summarisation_topics.ipynb   Preprocessing, summarisation and LDA topic modelling
├── deployment/                      Streamlit app for the abstract classifier (see its README)
├── outputs/
│   └── lda_intertopic_map.html      Interactive pyLDAvis intertopic distance map
├── screenshots/                     Screenshots of the app and visualisations
└── documentation/                   Project report
```

## Summary of the work

### Questions 1–2: Abstract classification (AI vs classical research)

- Cleaned 1,138 abstracts (removed duplicates, non-abstract records and PDF boilerplate) and identified the abstract text as the relevant feature using TF-IDF and chi-square analysis.
- Baseline: Multinomial Naive Bayes (test macro F1 0.644, AI recall 0.234).
- Compared Logistic Regression, Linear SVM, Complement Naive Bayes and Random Forest.
- Enhancement: class weighting to address the 79/21 class imbalance.
- Best model: Random Forest with balanced class weights (test macro F1 0.883, AI recall 0.787), deployed as a Streamlit web app.

### Questions 3–4: Summarisation and topic modelling

- Built a dataframe of five research methodology articles and cleaned the PDF-extracted text (citations, page headers, hyphenation, duplicate sentences), followed by spaCy lemmatisation.
- Summarised article 1 with frequency-based extractive summarisation, and articles 2–5 with TextRank, aggregated into one overview.
- LDA topic modelling on 5-sentence chunks of the articles, with the number of topics chosen using c_v coherence; 8 topics selected.
- Intertopic distance map created with pyLDAvis.

## Running the notebooks

1. Install Python 3.11+ and the packages listed in `deployment/requirements.txt`, plus:
   ```bash
   pip install notebook matplotlib seaborn wordcloud spacy gensim pyLDAvis networkx
   python -m spacy download en_core_web_sm
   ```
2. Start Jupyter from the repository folder:
   ```bash
   jupyter notebook
   ```
3. Open a notebook from the `notebooks` folder and choose **Kernel → Restart & Run All**.

## Running the web app

See [`deployment/README.md`](deployment/README.md) for step-by-step instructions.
