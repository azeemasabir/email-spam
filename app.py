import streamlit as st
import joblib
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

import nltk

try:
    nltk.data.find('corpora/stopwords')
except:
    nltk.download('stopwords')
# Download stopwords (only runs first time)
nltk.download('stopwords')

# Load model and vectorizer
model = joblib.load('naive_bayes_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Initialize preprocessing tools
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

# SAME cleaning function as training
def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www.\S+', '', text)
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'\b\d{5,}\b', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = ' '.join([stemmer.stem(word) for word in text.split() if word not in stop_words])
    return text

# --- UI ---
st.title("📧 Email Spam Classifier")

user_input = st.text_area("Enter your email message:")

if st.button("Predict"):
    if user_input.strip() != "":
        cleaned = clean_text(user_input)
        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)[0]

        if prediction == 1:
            st.error("🚫 Spam Email")
        else:
            st.success("✅ Not Spam")
    else:
        st.warning("Please enter a message first.")