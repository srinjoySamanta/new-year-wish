import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="Hey Chotu! 🎮",
    page_icon="😎",
    layout="centered"
)

# 2. Styling (CSS) - Fun and Energetic Theme
st.markdown("""
    <style>
    .stButton>button {
        color: white;
        background-color: #ff9f1c; /* Bright Orange */
        border-radius: 20px;
        height: 3em;
        width: 100%;
        font-size: 20px;
        font-weight: bold;
        border: 2px solid #ffffff;
    }
    .header-text {
        font-size: 45px !important;
        font-weight: 800;
        color: #2ec4b6; /* Teal */
        text-align: center;
        text-shadow: 2px 2px #000;
    }
    .sub-text {
        font-size: 18px;
        text-align: center;
        color: #fff;
        background-color: #011627; /* Dark background */
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #ff9f1c;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. The Surprise Logic
def show_surprise():
    # Progress bar with a funny message
    progress_text = "Loading coolness..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    
    time.sleep(0.3)
    my_bar.empty()
    
    # Celebration Effects
    st.balloons()
    
    # The Wish
    st.markdown('<h1 class="header-text">Happy New Year, Chotu! 😎</h1>', unsafe_allow_html=True)
    
    # Funny Minion or Cool GIF
    st.image("https://media.giphy.com/media/11sBLVxNs7v6WA/giphy.gif", caption="Let's rock 2026!")
    
    st.markdown("""
    <div class="sub-text">
    Happy New Year to my favorite Chotu! ⚡<br>
    <br>
    Hope you have a blast this year.<br>
    Study hard, play hard, and don't be too naughty! 😉<br>
    <br>
    <b>- Your Big Bro, Srinjoy</b>
    </div>
    """, unsafe_allow_html=True)

# 4. The Initial UI
st.title("Surprise for Chotu 🎁")
st.write("I have a special message for you.")

if st.button("🔥 Tap to Open"):
    show_surprise()