<<<<<<< HEAD
import streamlit as st
import pickle
import re
import PyPDF2

# --------------------------------------------------
# Load saved model files
# --------------------------------------------------
clf = pickle.load(open("clf.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))

# --------------------------------------------------
# Resume cleaning function (SAME as training)
# --------------------------------------------------
def cleanResume(txt):
    cleanTxt = re.sub('http\S+\s', ' ', txt)
    cleanTxt = re.sub('RT|cc', ' ', cleanTxt)
    cleanTxt = re.sub('#\S+\s', ' ', cleanTxt)
    cleanTxt = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanTxt)
    cleanTxt = re.sub('\s+', ' ', cleanTxt)
    return cleanTxt.lower()

# --------------------------------------------------
# Streamlit UI
# --------------------------------------------------
st.set_page_config(page_title="AI Resume Screening", layout="centered")

st.title("🧠 AI-Based Resume Screening System")
st.write("Upload a resume or paste resume text to predict the job category.")

# --------------------------------------------------
# Text input
# --------------------------------------------------
resume_text = st.text_area("📄 Paste Resume Text Here", height=300)

# --------------------------------------------------
# PDF Upload
# --------------------------------------------------
uploaded_file = st.file_uploader("📂 Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    resume_text = ""
    for page in pdf_reader.pages:
        resume_text += page.extract_text()

# --------------------------------------------------
# Prediction Button
# --------------------------------------------------
if st.button("🔍 Predict Resume Category"):
    if resume_text.strip() == "":
        st.warning("⚠ Please upload or paste a resume.")
    else:
        cleaned_resume = cleanResume(resume_text)
        vectorized_resume = tfidf.transform([cleaned_resume])
        prediction_id = clf.predict(vectorized_resume)[0]
        predicted_category = le.inverse_transform([prediction_id])[0]

        st.success(f"✅ Predicted Resume Category: **{predicted_category}**")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.markdown("📌 *AI Resume Screening System using Machine Learning & Streamlit*")
=======
import streamlit as st
import pickle
import re
import PyPDF2

# --------------------------------------------------
# Load saved model files
# --------------------------------------------------
clf = pickle.load(open("clf.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))

# --------------------------------------------------
# Resume cleaning function (SAME as training)
# --------------------------------------------------
def cleanResume(txt):
    cleanTxt = re.sub('http\S+\s', ' ', txt)
    cleanTxt = re.sub('RT|cc', ' ', cleanTxt)
    cleanTxt = re.sub('#\S+\s', ' ', cleanTxt)
    cleanTxt = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanTxt)
    cleanTxt = re.sub('\s+', ' ', cleanTxt)
    return cleanTxt.lower()

# --------------------------------------------------
# Streamlit UI
# --------------------------------------------------
st.set_page_config(page_title="AI Resume Screening", layout="centered")

st.title("🧠 AI-Based Resume Screening System")
st.write("Upload a resume or paste resume text to predict the job category.")

# --------------------------------------------------
# Text input
# --------------------------------------------------
resume_text = st.text_area("📄 Paste Resume Text Here", height=300)

# --------------------------------------------------
# PDF Upload
# --------------------------------------------------
uploaded_file = st.file_uploader("📂 Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    resume_text = ""
    for page in pdf_reader.pages:
        resume_text += page.extract_text()

# --------------------------------------------------
# Prediction Button
# --------------------------------------------------
if st.button("🔍 Predict Resume Category"):
    if resume_text.strip() == "":
        st.warning("⚠ Please upload or paste a resume.")
    else:
        cleaned_resume = cleanResume(resume_text)
        vectorized_resume = tfidf.transform([cleaned_resume])
        prediction_id = clf.predict(vectorized_resume)[0]
        predicted_category = le.inverse_transform([prediction_id])[0]

        st.success(f"✅ Predicted Resume Category: **{predicted_category}**")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.markdown("📌 *AI Resume Screening System using Machine Learning & Streamlit*")
>>>>>>> 4ecacc3920ae9b509818816355e9c265d02640fc
