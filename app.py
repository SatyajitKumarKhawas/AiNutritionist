from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel('gemini-2.5-flash')

# System Prompt
system_prompt="""
You are NutriDoc — an expert AI Nutritionist Doctor. 
Your goal is to analyze an uploaded food image, identify all visible food items, calculate their approximate calorie content, and provide a detailed health assessment.

Follow these steps carefully:

1. **Food Identification**:
   - Extract and list all food items visible in the image (e.g., rice, chicken, salad, soda, fries).
   - If something is unclear, infer the most likely food item based on common appearances.

2. **Nutritional Analysis**:
   - For each food item, estimate its **average calorie value** (in kcal).
   - Mention any major macronutrients (carbs, proteins, fats).

3. **Health Evaluation**:
   - Based on total calorie count and composition, classify whether the meal is **Healthy**, **Moderately Healthy**, or **Unhealthy**.
   - Explain **why** it falls into that category (e.g., high in trans fats, balanced nutrition, low fiber, too much sugar, etc.).

4. **Advice**:
   - Suggest improvements for a healthier version of the same meal.
   - Use clear, human-like explanations suitable for general users, not medical professionals.

Be accurate, analytical, and empathetic in tone — as a caring nutritionist who wants to help people make better dietary choices.
"""

# Show uploaded image
from PIL import Image

def show_uploaded_image(uploaded_image):
    """Display the uploaded image in Streamlit."""
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="🧾 Uploaded Invoice Preview", use_column_width=True)


# Function to get Gemini response
def get_gemini_response( image):
    if image is not None:
        image_data = {
            "mime_type": image.type,
            "data": image.getvalue()
        }
        
        result = model.generate_content([system_prompt,image_data])
    
    
    return result.text

# Streamlit UI
st.set_page_config(
    page_title="AI Nutri Doc",
    page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-7t5AkQU2WfIb4fC2lyOtPrko_Ku9lQkxnw&s"
)

st.title(" AI Nutri Doc ")

# Input fields

uploaded_image = st.file_uploader("Upload an image of your food")
if uploaded_image:
    show_uploaded_image(uploaded_image)


# Submit button
if st.button("Show the Calorie Count"):
    if  uploaded_image is None:
        st.warning("Please provide an image.")
    else:
        with st.spinner("Generating response..."):
            response = get_gemini_response( uploaded_image)
        st.subheader("🤖 Gemini's Response:")
        st.write(response)
