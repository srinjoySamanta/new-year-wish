import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="For Atasi 🌸",
    page_icon="✨",
    layout="centered"
)

# 2. Styling (CSS) - Aesthetic, Soft, and Sweet
st.markdown("""
    <style>
    .stButton>button {
        color: white;
        background-color: #FF8FAB; /* Soft Pink */
        border-radius: 25px;
        height: 3em;
        width: 100%;
        font-size: 20px;
        font-weight: bold;
        border: 2px solid #FFC2D1;
    }
    .stButton>button:hover {
        background-color: #FB6F92;
    }
    .header-text {
        font-size: 40px !important;
        font-weight: bold;
        color: #D63384; /* Deep Pink/Magenta */
        text-align: center;
        font-family: 'Comic Sans MS', 'Chalkboard SE', sans-serif; /* Playful font */
    }
    .quote-card {
        background-color: #FFF0F5; /* Lavender Blush */
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        font-size: 18px;
        color: #555;
        border: 2px dashed #FF8FAB;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .highlight {
        color: #D63384;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. The Surprise Logic
def show_surprise():
    # Progress bar
    progress_text = "Gathering sparkles..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    
    time.sleep(0.3)
    my_bar.empty()
    
    # Celebration Effects (Flowers and magic)
    st.balloons()
    
    # The Wish
    st.markdown('<h1 class="header-text">Happy New Year, Atasi! 🦋</h1>', unsafe_allow_html=True)
    
    # Cute/Aesthetic GIF (Flowers or sparkles)
    st.image("https://media.giphy.com/media/26AHqZc14YJHKjApy/giphy.gif", caption="Wishing you a magical year")
    
    st.markdown("""
    <div class="quote-card">
    To my loveliest friend, <br>
    <br>
    Thank you for bringing so much brightness into my life. <br>
    May your 2026 be as <span class="highlight">beautiful and kind</span> as you are.<br>
    <br>
    Keep smiling, because your smile is the best! ✨<br>
    <br>
    <b>- Srinjoy</b>
    </div>
    """, unsafe_allow_html=True)

# 4. The Initial UI
st.title("A Little Surprise for Atasi 💌")
st.write("Because you deserve a special wish.")

if st.button("🌸 Click to Open"):
    show_surprise()