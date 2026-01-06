import streamlit as st
import joblib

tfidf = joblib.load("tfidf.pkl")
clf = joblib.load("classifier.pkl")
reg = joblib.load("regressor.pkl")

st.title("Programming Problem Difficulty Predictor")

title = st.text_area("Problem Title")
desc = st.text_area("Problem Description")
inp = st.text_area("Input Description")
out = st.text_area("Output Description")

if st.button("Predict"):
    text = title + " " + desc + " " + inp + " " + out
    vec = tfidf.transform([text])

    pred_class = clf.predict(vec)[0]
    pred_score = reg.predict(vec)[0]

    st.success(f"Predicted Difficulty Class: {pred_class}")
    st.success(f"Predicted Difficulty Score: {round(pred_score, 2)}")

