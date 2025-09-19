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
# 2️⃣ Updated Rule-Based Prediction
# ------------------------------
def lounge_eligibility(row):
    # Rule 1: Business class → always eligible
    if row["Class"] == "Business":
        return 1
    # Rule 2: Loyal customers → always eligible
    elif row["Customer Type"] == "Loyal Customer":
        return 1
    # Rule 3: Disloyal + Eco/Eco Plus → eligible only if flight distance > 2500 km
    elif row["Customer Type"] == "disloyal Customer" and row["Class"] in ["Eco", "Eco Plus"] and row["Flight Distance"] > 2500:
        return 1
    # Otherwise not eligible
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

# Apply updated rule
df["LoungeEligible"] = df.apply(lounge_eligibility, axis=1)

# Ensure both categories exist
df["LoungeEligible"] = pd.Categorical(df["LoungeEligible"], categories=[0, 1])

# Show counts
counts = df["LoungeEligible"].value_counts().sort_index()
st.write("✅ 1 = Eligible, ❌ 0 = Not Eligible")
st.bar_chart(counts)

# Breakdown by Class
st.subheader("Breakdown by Class")
grouped = df.groupby(["Class", "LoungeEligible"]).size().unstack(fill_value=0)
st.bar_chart(grouped)
