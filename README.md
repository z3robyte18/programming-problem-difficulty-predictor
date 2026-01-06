# Programming Problem Difficulty Predictor

## 👉🏼Project Overview
This project aims to predict the difficulty level of programming problems using Natural Language Processing (NLP) and Machine Learning techniques.

Given a programming problem’s:   
- Title  
- Problem description  
- Input description  
- Output description  

the system predicts:

__1. Difficulty Class__ → Easy / Medium / Hard (Classification)

__2. Difficulty Score__ → Numerical score (Regression)

__A Streamlit-based web interface__ allows users to input problem details and get instant predictions.

## 👉🏼Dataset Used

* __Source:__ Programming problems dataset (JSON format)

* __File:__ data/problems.json

* __Number of samples:__ ~4000 problems

### Dataset Fields:
- title
- description
- input_description
- output_description
- problem_class (Easy / Medium / Hard)
- problem_score (float difficulty score)
- url
## 👉🏼Approach & Methodology
### Data Preprocessing
- Missing values handled using empty strings
- Multiple text fields combined into a single feature:
  - Title
  - Description
  - Input Description
  - Output Description

### Feature Extraction
- __TF-IDF Vectorization__
  - max_features = 8000
  - ngram_range = (1, 2)
  - Stop words removed (English)

### Models Used
1. __Classification Model__
   - __Model:__ RandomForestClassifier
   - __Target:__ problem_class
   - __Classes:__ Easy / Medium / Hard

2. __Regression Model__
   - __Model:__ RandomForestRegressor
   - __Target:__ problem_score
## 👉🏼Evaluation Metrics
### Classification
- __Accuracy:__ ~55%
- __Confusion Matrix:__ Included in notebook
> [!NOTE]
> Difficulty classification is inherently subjective and noisy, which affects accuracy.
### Regression
- __MAE (Mean Absolute Error):__ ~1.70
- __RMSE (Root Mean Squared Error):__ ~2.04

## 👉🏼Web Interface (Streamlit App)
### Features:
- Text boxes for:
  - Problem Title
  - Problem Description
  - Input Description
  - Output Description
- Predict button
- Displays:
  - Predicted Difficulty Class
  - Predicted Difficulty Score
### Tech Used:
- Streamlit
- Pre-trained ML models (.pkl files)
## 👉🏼Steps to Run the Project Locally
### 1. Clone the Repository
```bash
git clone https://github.com/z3robyte18/programming-problem-difficulty-predictor.git
cd programming-problem-difficulty-predictor
```
### 2. Create Virtual Environment (Optional but Recommended)
```bash
conda create -n difficulty-predictor python=3.10
conda activate difficulty-predictor
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the Streamlit App
```bash
streamlit run app/app.py
```
The app will open automatically in your browser.
## 👉🏼Project Structure

```text
ds_project/
│
├── app/ 
│   └── app.py
│
├── data/
│   └── problems.json
│
├── models/
│   ├── tfidf.pkl
│   ├── classifier.pkl
│   └── regressor.pkl
│
├── notebooks/
│   └── nlp_problem_difficulty.ipynb
│
├── README.md
├── .gitignore
└── report.pdf
```
## 👉🏼Demo Video

- __Duration:__ 2–3 minutes
- __Content covered:__
  - Project overview
  - Dataset & approach
  - Model training & evaluation
  - Live web app prediction
### 📌 __Demo Video Link:__  
👉 *Add Google Drive / YouTube link here*
## 👉🏼Author Details

- **Name:** Himani Rohaj  
- **Program:** BS-MS(Mathemtics and Computing)
- **Project Type:** NLP + ML + Web Application  
- **GitHub:** https://github.com/z3robyte18

## 👉🏼Conclusion
This project demonstrates how NLP techniques combined with machine learning can be used to estimate the difficulty of programming problems. Despite the subjective nature of difficulty labels, the system provides meaningful predictions and a practical interactive interface.


