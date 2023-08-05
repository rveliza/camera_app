import streamlit as st
from PIL import Image

st.subheader("Color to grayscale converter")

# Create a file uploader component
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start the camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert a pillow image to greyscale
    gray_img = img.convert("L")

    # Render the grayscale image on the website
    st.image(gray_img)

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_uploaded_img = img.convert("L")
    st.image(gray_uploaded_img)

