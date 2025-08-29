import streamlit as st
import pandas as pd
import joblib

st.title("✈️ Lounge Eligibility Prediction & Dashboard")

# ------------------------------
# 1️⃣ User Input for Prediction
# ------------------------------
st.header("Predict Lounge Eligibility for a Passenger")

age = st.slider("Age", 7, 85, 30)
flight_distance = st.slider("Flight Distance", 50, 5000, 500)
customer_type = st.selectbox("Customer Type", ["Loyal Customer", "disloyal Customer"])
class_type = st.selectbox("Class", ["Eco", "Eco Plus", "Business"])
wifi = st.slider("Inflight wifi service", 0, 5, 3)

input_data = pd.DataFrame({
    "Age": [age],
    "Flight Distance": [flight_distance],
    "Customer Type": [customer_type],
    "Class": [class_type],
    "Inflight wifi service": [wifi]
})

# ------------------------------
# 2️⃣ Quick Rule-Based Prediction
# ------------------------------
def lounge_eligibility(row):
    # Rule: Eligible if Loyal Customer OR Business Class
    if row["Customer Type"] == "Loyal Customer" or row["Class"] == "Business":
        return 1
    else:
        return 0

input_data["LoungeEligible"] = input_data.apply(lounge_eligibility, axis=1)

if st.button("Check Eligibility"):
    if input_data["LoungeEligible"][0] == 1:
        st.success("✅ Eligible for Lounge Access")
    else:
        st.error("❌ Not Eligible for Lounge Access")

# ------------------------------
# 3️⃣ Show Distribution for Train Dataset
# ------------------------------
st.header("Lounge Eligibility Distribution (Train Dataset)")

# Load full train dataset
df = pd.read_csv("data/train.csv")
df.columns = df.columns.str.strip()

# Create LoungeEligible column using same rule
df["LoungeEligible"] = df.apply(lounge_eligibility, axis=1)

# Ensure both categories exist
df["LoungeEligible"] = pd.Categorical(df["LoungeEligible"], categories=[0, 1])

# Show counts
counts = df["LoungeEligible"].value_counts().sort_index()
st.write("✅ 1 = Eligible, ❌ 0 = Not Eligible")
st.bar_chart(counts)

# Optional: Breakdown by Class
st.subheader("Breakdown by Class")
grouped = df.groupby(["Class", "LoungeEligible"]).size().unstack(fill_value=0)
st.bar_chart(grouped)
