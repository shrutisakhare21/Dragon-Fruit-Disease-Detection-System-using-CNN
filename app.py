import streamlit as st
import tensorflow as tf
import numpy as np

# TensorFlow model prediction function
def model_prediction(test_image):
    model = tf.keras.models.load_model('trained_model.h5')
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to a batch
    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)  # Return index of max element
    return result_index

# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Choose a section", ["Home", "About", "Disease Recognition", "Disease Info"])  # Fixed Name

# Home Page
if app_mode == "Home":
    st.header("Dragon Fruit Disease Detection System Using CNN")
    image_path = "home.jpg"
    st.image(image_path, use_container_width=True)  # Updated parameter

    st.markdown("""
    Welcome to the Dragon Fruit Disease Detection System Using CNN! 🌿🔍
    Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases.
    
    ### How It Works
    1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Results:** View the results and recommendations for further action.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **Disease Recognition** page in the sidebar to upload an image and experience the power of our Plant Disease Recognition System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
    """)

# About Page
elif app_mode == "About":
    st.header("About")
    st.markdown("""
    #### About Dataset
    This dataset is created by us using offline augmentation from the original dataset. This dataset consists of images of healthy and diseased leaves which is categorized into 4 different classes. The total dataset is divided into an 80/20 ratio of training and validation set preserving the directory structure. A new directory containing 20 test images is created later for prediction purposes.

    #### Content
    1. Train 
    2. Valid 
    3. Test 
    """)

# Disease Recognition (Prediction Page)
elif app_mode == "Disease Recognition":
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")
    
    if test_image:
        if st.button("Show Image"):
            st.image(test_image, use_container_width=True)
    
        if st.button("Predict"):
            with st.spinner("Please Wait..."):
                result_index = model_prediction(test_image)
                class_names = ['Fresh Dragon Fruit', 'Rust Spot', 'Soft Rot Fruit', 'Stem Canker']
                st.success(f"Model is Predicting it's a **{class_names[result_index]}**")

# Disease Info Page
elif app_mode == "Disease Info":
    st.header("Information on Dragon Fruit Diseases")

    # Rust Spot
    st.subheader("1. Rust Spot")
    st.write("Rust spots on Dragon Fruits are caused by the fungal disease **Botryosphaeria** or **Brown Stem Spot**.")
    st.markdown("""
    **Causes:**
    - More common in rainy seasons with high humidity.
    - Fungal spores spread through air, especially in foggy conditions.
    """)

    # Stem Canker
    st.subheader("2. Stem Canker")
    st.write("Caused by the fungus **Neoscytalidium dimidiatum**, it leads to sunken, orangish-brown spots on stems and fruits.")
    st.markdown("""
    **Symptoms:**
    - Black fruiting bodies on affected areas.
    - Yellow halos around infected spots.
    - White-yellow spots turning orange to brown.
    """)

    # Soft Rot
    st.subheader("3. Soft Rot")
    st.write("Infected areas appear as soft, watery lesions, causing fruit to rot.")
    st.markdown("""
    **Causes:**
    - Caused by **Enterobacter cloacae** and fungi like **Fusarium & Alternaria**.
    - Favored by warm, humid conditions.
    - Mature and ripe fruits are more vulnerable.
    """)
