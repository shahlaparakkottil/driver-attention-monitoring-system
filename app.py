import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load model
model = load_model("model/driver_attention_model.h5")

IMG_SIZE = 128  # use same size as training

st.title("🚗 Driver Attention Monitoring System")

st.write("Upload a student image to detect attention level.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    img = img.resize((IMG_SIZE, IMG_SIZE))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array)

    if prediction[0][0] > 0.5:
        st.error("⚠ Driver is DROWSY / INATTENTIVE")
    else:
        st.success("✅ Driveris ALERT")