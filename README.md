# 📧 Email Spam Classification System

A complete **Machine Learning project** that classifies emails as **Spam** or **Not Spam (Ham)** using Natural Language Processing (NLP) techniques and a deployed interactive web interface.

---

## 🚀 Project Overview

This project demonstrates the full pipeline of:

* Data preprocessing
* Feature extraction (TF-IDF)
* Model training (Naive Bayes)
* Model evaluation
* Deployment using Streamlit

Users can input an email message and instantly get a prediction.

---

## 🧠 Model Development Workflow

### 1️⃣ Dataset

* Dataset contains two columns:

  * `category` → `spam` or `ham`
  * `message` → email content

---

### 2️⃣ Data Preprocessing

Key preprocessing steps:

* Convert text to lowercase
* Remove:

  * URLs
  * Email addresses
  * Numbers
  * Special characters
* Remove stopwords (using NLTK)
* Apply stemming (PorterStemmer)
* Remove extra whitespace

---

### 3️⃣ Feature Engineering

* Used **TF-IDF Vectorization**
* Converts text into numerical vectors
* Captures importance of words across documents

```python
TfidfVectorizer(max_features=1000)
```

---

### 4️⃣ Train-Test Split

* 80% training data
* 20% testing data
* Stratified sampling to maintain class balance

---

### 5️⃣ Model Used

* **Multinomial Naive Bayes**
* Suitable for text classification tasks

```python
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)
```

---

### 6️⃣ Model Evaluation

Metrics used:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

---

## 💾 Model Saving

* Model saved using `joblib`
* Files:

  * `naive_bayes_model.pkl`
  * `tfidf_vectorizer.pkl`

---

## 🖥️ Frontend (Streamlit App)

A simple UI built using Streamlit:

* User inputs email text
* Text is preprocessed
* TF-IDF transformation applied
* Model predicts:

  * ✅ Not Spam
  * 🚫 Spam

---

## ⚠️ Important Note

The **same preprocessing function** used during training is reused during prediction to ensure consistency.

---

## 📦 Project Structure

```
project/
│
├── app.py                     # Streamlit frontend
├── naive_bayes_model.pkl     # Trained model
├── tfidf_vectorizer.pkl      # TF-IDF vectorizer
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone <your-repo-link>
cd project
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
streamlit run app.py
```

---

## 🌍 Deployment

The app can be deployed using:

### ✅ Streamlit Community Cloud

* Connect GitHub repository
* Select `app.py`
* Deploy instantly

### ✅ Hugging Face Spaces

* Upload files
* Use Streamlit SDK

---

## 📌 Requirements

```
streamlit
scikit-learn
nltk
joblib
```

---

## 🔑 Key Highlights

* End-to-end NLP pipeline
* Clean and reproducible preprocessing
* Lightweight and fast model
* Real-time prediction interface
* Easy deployment (no backend required)

---

## 📈 Future Improvements

* Add deep learning models (LSTM, BERT)
* Improve UI/UX design
* Add confidence score for predictions
* Support multiple languages
* Integrate database for storing inputs

---

## 🤝 Contribution

Feel free to fork this repository and improve the project.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgment

* NLTK for text preprocessing
* Scikit-learn for ML models
* Streamlit for UI and deployment

---

## 🎯 Conclusion

This project demonstrates how a complete **machine learning pipeline** can be built and deployed for real-world use with minimal complexity.

👉 From raw text → processed features → trained model → deployed app — everything is covered.

---
