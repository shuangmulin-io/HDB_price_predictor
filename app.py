import numpy as np
import pickle
import streamlit as st

# 1. Load our trained HDB prediction brain
with open("house_model.pkl", "rb") as f:
    model = pickle.load(f)

# 2. Design the localized App Interface
st.title("🏡 Singapore HDB Resale Price Predictor")
st.write(
    "Input the flat's structural attributes below to calculate its estimated market value."
)

# 3. Create input parameters matching local HDB profiles
sqm = st.slider(
    "Floor Area (Square Metres - sqm)",
    min_value=30,
    max_value=160,
    value=90,
    step=1,
)
lease_year = st.slider(
    "Lease Commencement Year",
    min_value=1970,
    max_value=2025,
    value=2000,
    step=1,
)
floor = st.slider(
    "Floor Level (Storey)", min_value=1, max_value=50, value=5, step=1
)

# 4. Perform calculation on submission
if st.button("Predict Resale Price"):
    # Format user parameters to match training data positions
    input_data = np.array([[sqm, lease_year, floor]])

    # Generate calculation
    prediction = model.predict(input_data)[0]

    # Display localized output
    st.success(f"🇸🇬 Estimated Resale Price: S${prediction:,.2f}")