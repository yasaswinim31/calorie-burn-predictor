<h1 align="center">🔥 Calorie Burn Predictor</h1>

<p align="center">
  A machine learning-powered web app that predicts calories burned based on user metrics.
  <br />
  Built with <b>Python</b>, <b>scikit-learn</b>, and <b>Streamlit</b>.
</p>

---

## 🧠 Project Overview

This project demonstrates a complete machine learning workflow to predict calorie expenditure using personal and physiological data:

- 📊 Data loading and preprocessing
- 📈 Exploratory data analysis (EDA)
- 🔍 Model training and evaluation
- 💻 Streamlit-based interactive app

---


## 📁 Folder Structure

```bash
calorie-burn-predictor/
│
├── data/
│   └── calories.csv              # Dataset
│
├── notebooks/
│   └── eda_and_modeling.ipynb   # Jupyter notebook for EDA & ML
│
├── src/
│   └── calorie_model.joblib     # Saved ML model
│
├── streamlit_app/
│   └── app.py                   # Streamlit web application



│
├── requirements.txt             # Project dependencies
├── .gitignore                   # Files and folders to ignore
└── README.md                    # You're here!
```
---


## 🚀 How to Run

### ✅ Step 1: Clone the Repository

```bash
git clone https://github.com/yasaswinim31/calorie-burn-predictor.git
cd calorie-burn-predictor
```

### ✅ Step 2: Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate     # macOS/Linux

# OR

venv\Scripts\activate        # Windows
```

### ✅ Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```
### ✅ Step 3: Run the Sreamlit App

```bash
streamlit run streamlit_app/app.py
```
---
## 🧪 Models Used
	•	Linear Regression
	•	Ridge Regression
	•	Random Forest Regressor

Evaluation metrics:
	•	R² Score
	•	RMSE (Root Mean Squared Error)
 ---
 
## 📊 Dataset Features
	•	Gender
	•	Age
	•	Height (cm)
	•	Weight (kg)
	•	Duration (min)
	•	Heart Rate
	•	Body Temperature
	•	Calories Burned (target)

---
## 🛠 Tech Stack

| Tool          | Purpose             |
|---------------|---------------------|
| Python        | Core Language       |
| Pandas        | Data Manipulation   |
| Seaborn       | Visualization       |
| Sickit-learn  | ML Modeling         |
| Streamlit     | Web Applications    |
