import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

#downloading required nltk resources
for resource in ["punkt", "punkt_tab", "stopwords", "wordnet"]:
    nltk.download(resource, quiet=True)

lemmatizer = WordNetLemmatizer()

#same stopwords as training
stop_words = set(stopwords.words("english"))
stop_words.update(["paper", "study", "result", "results", "using", "use", "also", "show", "find",
                   "abstract", "article"])

#clean text function
def clean_text(text, min_len=3):
        #remove biolerplate specific to dataset
    text = re.sub(r"\[Formula: see text\]", " ", text)
    text = re.sub(r"Copyright\s*©.*", " ", text) #copyright notices
    text = re.sub(r"http\S+|www\.\S+", " ", text) #urls
    text = re.sub(r"(Background|Objectives?|Methods?|Results?(?: and Conclusions?)?|Conclusions?|Purpose|Findings)(?=[A-Z])",
    " ", text) #headings stuck to next word

    #lowercase
    text = text.lower()

    #removing numbers and punctuation
    text = re.sub(r"[^a-z\s]", " ", text)

    #tokenise
    tokens = word_tokenize(text)

    #removing stopwords and short tokens then lemmatise
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    tokens = [t for t in tokens if t not in stop_words and len(t) >= min_len]

    #joining back into single string
    return " ".join(tokens)