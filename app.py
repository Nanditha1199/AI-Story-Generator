import streamlit as st
import google.generativeai as genai
import os

# -----------------------------
# PAGE CONFIG (MUST BE FIRST)
# -----------------------------
st.set_page_config(
    page_title="📖 AI Story Generator",
    page_icon="📖",
    layout="centered"
)

# -----------------------------
# GEMINI API KEY
# -----------------------------
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("❌ Gemini API key not found!")
    st.info("Add GEMINI_API_KEY in Streamlit Cloud → App Settings → Secrets.")
    st.stop()

genai.configure(api_key=API_KEY)

# -----------------------------
# MODEL
# -----------------------------
generation_config = {
    "temperature": 0.9,
    "top_p": 0.95,
    "top_k": 40,
}

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    generation_config=generation_config
)

# -----------------------------
# STORY TYPES
# -----------------------------
story_types = {
    "Romance ❤️": "romantic love story",
    "Horror 👻": "scary horror story",
    "Adventure 🗺️": "exciting adventure journey",
    "Fantasy 🧙‍♂️": "magical fantasy world story",
    "Comedy 😂": "funny comedy story",
    "Sci-Fi 🚀": "futuristic science fiction story",
    "Thriller 🔪": "suspense thriller story",
    "Mystery 🕵️‍♀️": "detective mystery story",
    "Drama 🎭": "emotional drama story",
    "Historical 📜": "historical era story",
    "Inspirational ✨": "motivational inspiring story",
    "Fairy Tale 🧚‍♀️": "magical fairy tale story",
    "Crime 🧑‍⚖️": "crime investigation story",
    "Action 💥": "action-packed story"
}

# -----------------------------
# UI
# -----------------------------
st.title("📖 AI Story Generator")
st.write("Create amazing AI-generated stories!")

story_type = st.selectbox(
    "📚 Choose Story Type",
    list(story_types.keys())
)

genre = story_types[story_type]

name = st.text_input("🧑 Main Character Name")

mood = st.selectbox(
    "😊 Select Story Mood",
    [
        "Happy",
        "Sad",
        "Emotional",
        "Mysterious",
        "Exciting",
        "Dark",
        "Romantic"
    ]
)

length = st.slider(
    "📏 Story Length (words)",
    100,
    1000,
    300
)

idea = st.text_area("✍️ Enter Story Idea")