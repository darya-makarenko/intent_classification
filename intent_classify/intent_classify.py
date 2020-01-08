import spacy
import pandas as pd
import nltk
import string
from spacy.lang.ru import Russian
punctuations = string.punctuation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.base import TransformerMixin
from nltk.stem import PorterStemmer 
from nltk.stem import arlstem
from nltk.stem.snowball import SnowballStemmer 
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords


with open('positive.csv', 'r', encoding='utf-8') as f:
    lines_pos = f.readlines()
    
with open('negative.csv', 'r', encoding='utf-8') as f:
    lines_neg = f.readlines()
    
f = open("stopwords.txt", "r", encoding="utf8")
stopwords = f.readlines()
stopwords = [word.strip() for word in stopwords]

nlp = spacy.load('xx_ent_wiki_sm')
df = pd.DataFrame([[line.strip(), '0', 'pos'] for line in lines_pos] +  [[line.strip(), '1', 'neg'] for line in lines_neg], columns=['text', 'label', 'label_text'])
df = df.sample(frac=1)
stemmer = SnowballStemmer("russian") 


def cleanup_text(text, logging=False):
    
    doc = nlp(text, disable=['parser', 'ner'])
    tokens = [tok.lemma_.lower().strip() for tok in doc]
    tokens = [tok for tok in tokens if tok not in punctuations and tok not in stopwords]
    tokens = [stemmer.stem(tok) for tok in tokens]
    tokens = ' '.join(tokens)
    return tokens.strip()


def tokenizeText(sample):
    tokens = parser(sample)
    lemmas = []
    for tok in tokens:
        lemmas.append(tok.lemma_.lower().strip() if tok.lemma_ != "-PRON-" else tok.lower_)
    tokens = lemmas
    return tokens


vectorizer = CountVectorizer(tokenizer=tokenizeText, ngram_range=(1,1))
parser = Russian()
clf = LogisticRegression()

class CleanTextTransformer(TransformerMixin):
    def transform(self, X, **transform_params):
        return [cleanup_text(text, False) for text in X]
    def fit(self, X, y=None, **fit_params):
        return self

pipe = Pipeline([('cleanText', CleanTextTransformer()),
                 ('vectorizer', vectorizer), 
                 ('clf', clf)])
            
p = pipe.fit(df['text'].to_list(), df['label'].to_list())



def classify_intent(texts):

    texts_info = []
    
    for text in texts:
        preds = pipe.predict_proba([text['text']])
        texts_info += [
                        {
                            'text': text['text'], 
                            'lang': text['lang'], 
                            'intents': [
                                {
                                    'label': 'pos', 
                                    'conf': preds[0][0]
                                },
                                {
                                    'label': 'neg', 
                                    'conf': preds[0][1]
                                }
                            ]
                        }
                    ]
    
    return texts_info