import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("farm_irrigation_system.pkl")

st.title("Smart Sprinkler System")
st.subheader("Enter scaled sensor values (0 to 1) to predict sprinkler status")

# Collect sensor inputs (scaled values)
sensor_values = []
for i in range(20):
	val = st.slider(f"Sensor {i+1}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
	sensor_values.append(val)

# Predict button
if st.button("Predict Sprinklers"):
	input_array = np.array(sensor_values).reshape(1, -1)
	prediction = model.predict(input_array)[0]

	st.markdown("### Prediction:")
	for i, status in enumerate(prediction):
		st.write(f"Sprinkler {i+1} (parcel_{i+1}): {'ON' if status else 'OFF'}")