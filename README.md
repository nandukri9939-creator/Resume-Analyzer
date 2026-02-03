# 🧠 AI-Based Resume Screening System

An AI-powered Resume Screening System that automatically classifies resumes into relevant job categories using Natural Language Processing (NLP) and Machine Learning, with an interactive Streamlit web interface.

---

## 📌 Project Overview

Recruiters often receive hundreds or thousands of resumes for a single job opening. Manual screening is time-consuming, inconsistent, and prone to bias.

This project solves that problem by:
- Automatically analyzing resume content
- Extracting meaningful features using NLP
- Predicting the most suitable job category
- Providing a simple and interactive web interface

---

## 🎯 Objectives

- Automate resume screening using Machine Learning
- Reduce manual effort in recruitment
- Classify resumes into predefined job categories
- Build a user-friendly web interface using Streamlit

---

## 🛠️ Technologies Used

- Programming Language: Python 3.9
- Libraries and Frameworks:
  - NumPy
  - Pandas
  - Scikit-learn
  - Streamlit
  - PyPDF2
  - Regex (re)
- Machine Learning Algorithm:
  - K-Nearest Neighbors (KNN) using One-Vs-Rest classification
- Text Processing:
  - TF-IDF Vectorization
  - Resume text cleaning using regular expressions

---

## 📂 Project Structure

Resume_analyzer/
│
├── app.py  
├── clf.pkl  
├── tfidf.pkl  
├── label_encoder.pkl  
├── requirements.txt  
└── README.md  

---

## 📊 Dataset Description

- The dataset consists of resumes labeled with job categories.
- Each record includes:
  - Resume: Text content of the resume
  - Category: Job role associated with the resume
- The dataset is cleaned and preprocessed before training.

---

## ⚙️ Methodology

### Data Preprocessing
- Removed URLs, special characters, punctuation, and extra spaces
- Converted text to lowercase
- Cleaned resume text using regular expressions

### Feature Engineering
- Converted resume text into numerical format using TF-IDF Vectorizer

### Model Training
- Split the dataset into training and testing sets (80:20)
- Trained a One-Vs-Rest KNN classifier
- Evaluated model performance using accuracy score

### Model Saving
- Saved the trained model, TF-IDF vectorizer, and label encoder using pickle

### Web Deployment
- Built a Streamlit web application to:
  - Paste resume text
  - Upload PDF resumes
  - Predict job category

---

## 🖥️ Streamlit Web App Features

- Paste resume text for analysis
- Upload resume in PDF format
- Predict job category instantly
- Simple and interactive user interface

---

## ▶️ How to Run the Project

### Step 1: Create Conda Environment
```bash
conda create -n resume_ui python=3.10 -y
conda activate resume_ui


## 👩‍💻 Author

**Name:** Nandini Kumari  
**Email:** nandukri9939@gmail.com  
**LinkedIn:** https://www.linkedin.com/in/nandini-kumari-2b734b2a4  
**GitHub:** https://github.com/nandukri9939-creator
