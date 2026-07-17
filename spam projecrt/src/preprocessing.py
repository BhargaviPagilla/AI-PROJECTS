import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
stemmer=PorterStemmer()
stops=set(stopwords.words("english"))
def clean_text(text):
    text=text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    words=word_tokenize(text)
    words=[stemmer.stem(w) for w in words if w not in stops]
    return " ".join(words)