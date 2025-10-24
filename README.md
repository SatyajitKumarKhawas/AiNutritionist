# 🩺 AI Nutri Doc — AI-Powered Nutritionist

**AI Nutri Doc** is a smart AI nutritionist app built using **Google Gemini 2.5 Flash** and **Streamlit**.
It analyzes food images, identifies the items present, estimates their calorie content, and evaluates how healthy the meal is — just like a real nutritionist!

---

## 🚀 Features

* 🖼️ **Image-based Food Recognition:** Upload a photo of your meal, and the model identifies all visible food items.
* 🔢 **Calorie Estimation:** Automatically estimates average calorie values for each item.
* ❤️ **Health Evaluation:** Classifies the meal as *Healthy*, *Moderately Healthy*, or *Unhealthy* based on total calories and nutrients.
* 💡 **Personalized Advice:** Provides suggestions for improving the meal to make it healthier.
* ⚡ **Powered by Gemini 2.5 Flash:** Uses Google’s multimodal generative AI to analyze both text and images.

---

## 🧠 Tech Stack

| Component                 | Description                                          |
| ------------------------- | ---------------------------------------------------- |
| **Frontend**              | Streamlit                                            |
| **Model**                 | Gemini 2.5 Flash (via `google-generativeai` library) |
| **Language**              | Python                                               |
| **Environment Variables** | `.env` file for API key management                   |

---

## 📦 Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ai-nutri-doc.git
   cd ai-nutri-doc
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On Mac/Linux
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File**

   Create a file named `.env` in the project root and add your Gemini API key:

   ```bash
   GOOGLE_API_KEY=your_api_key_here
   ```

5. **Run the App**

   ```bash
   streamlit run app.py
   ```

---

## 🧾 Example Usage

1. Launch the app in your browser (`http://localhost:8501`).
2. Upload an image of a meal (e.g., a plate with rice, chicken, and salad).
3. Click **"Show the Calorie Count"**.
4. Get an AI-generated analysis that includes:

   * Detected food items
   * Estimated calories
   * Health rating
   * Improvement advice

---

## 🧩 File Structure

```
AI-Nutri-Doc/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── .env                  # Contains your Gemini API key
└── README.md             # Project documentation
```

---

## 🧪 Sample Output

**Uploaded Image:** 🥗
**Detected Items:**  Salad, Bread
**Estimated Calories:** 480 kcal
**Health Status:** 🟢 Healthy
**Reason:** Balanced protein and fiber content with moderate calories.
**Suggestion:** Add a portion of fruit for better vitamin intake.

---

## ⚙️ Requirements

* Python 3.10+
* Streamlit
* google-generativeai
* python-dotenv
* Pillow

You can create a `requirements.txt` file with:

```txt
streamlit
google-generativeai
python-dotenv
Pillow
```

---

## 🧠 Future Enhancements

* 🧍 Personalized calorie tracking based on user’s BMI or goals
* 📊 Daily diet summary with charts
* 📱 Mobile-responsive UI
* 🧾 Save meal logs for future comparison

---

## 👨‍⚕️ Author

**Developed by:** [Satyajit Kumar Khawas]
