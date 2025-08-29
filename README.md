# ✈️ Passenger Lounge Access Prediction

## 📌 Overview
This project is a **machine learning-based Streamlit app** that predicts **lounge access eligibility** for airline passengers.  
The app uses features like **class, customer type, flight distance, and inflight services** to determine if a passenger is eligible for lounge access.  

It also provides a **dashboard** to visualize the distribution of eligible and non-eligible passengers from the dataset.

---

## 🚑 Problem Statement
Airline lounges provide comfort and priority services to eligible passengers.  
Manual verification or rule-based checks can be inconsistent or slow, especially with a large volume of passengers.  

This project solves that by:
- Automatically predicting lounge eligibility using a trained ML model  
- Providing a **Streamlit app** for interactive predictions  
- Offering a **dashboard** to visualize eligibility distribution across classes

---

## 🔍 Solution
- **Random Forest Model** trained on airline passenger data  
- **Streamlit App** with sliders, dropdowns, and interactive predictions  
- **Dashboard** showing eligible vs. non-eligible passenger distributions  
- **Streamlit Cloud Deployment** for online access

---

## 🛠 Tech Stack
- **Language:** Python 3.8+  
- **Libraries:**  
  - `pandas`, `numpy` for data processing  
  - `scikit-learn` for ML model training  
  - `joblib` for model persistence  
  - `streamlit` for dashboard and web app  
- **Model:** Random Forest Classifier

---

## 📂 Project Structure

## 📂 Folder Structure

```text
passenger_lounge_prediction/
├── app.py                 # Streamlit app
├── requirements.txt       # Python dependencies
├── data/
│   ├── train.csv          # Training dataset
│   └── test.csv           # Test dataset
├── models/
│   └── lounge_model.pkl   # Trained Random Forest model
└── README.md              # This file
```

---

## 🚀 How to Run

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/vaishnavinandikanti/passenger_lounge_prediction.git
cd passenger_lounge_prediction

2️⃣ Create Virtual Environment
# Linux / Mac
python -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py
Open your browser at http://localhost:8501 to view the app.
```
## ☁️ Deployment
To deploy the app on Streamlit Cloud:
1. Push your repository to GitHub
2. Go to https://streamlit.io/cloud
3. Click "New App" → Select Repository → Branch → app.py → Deploy
Your app will now be live at a shareable URL.

## 📊 Model Performance
- Algorithm: Random Forest Classifier
- Accuracy on test set: ~92%
- Precision / Recall / F1-score: Balanced across classes

```
👩‍💻 Author
Sree Vaishnavi Nandikanti
GitHub: https://github.com/vaishnavinandikanti
```
