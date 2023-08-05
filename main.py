import streamlit as st
from PIL import Image


with st.expander("Start the camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert a pillow image to greyscale
    gray_img = img.convert("1")

    # Render the grayscale image on the website
    st.image(gray_img)

