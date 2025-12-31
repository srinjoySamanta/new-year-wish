import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="For Twisha ✨",
    page_icon="📩",
    layout="centered"
)

# 2. Styling (CSS) - Soft and Friendly Theme
st.markdown("""
    <style>
    .stButton>button {
        color: white;
        background-color: #0083B0; /* Nice Blue for friendship */
        border-radius: 20px;
        height: 3em;
        width: 100%;
        font-size: 20px;
        font-weight: bold;
        border: none;
    }
    .header-text {
        font-size: 40px !important;
        font-weight: bold;
        color: #00B4DB;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
    }
    .sub-text {
        font-size: 18px;
        text-align: center;
        color: #444;
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. The Surprise Logic
def show_surprise():
    # Progress bar
    progress_text = "Sending best wishes..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    
    time.sleep(0.3)
    my_bar.empty()
    
    # Celebration Effects
    st.balloons()
    
    # The Wish
    st.markdown('<h1 class="header-text">Happy New Year, Twisha! 🥳</h1>', unsafe_allow_html=True)
    
    # A fun/friendly GIF
    st.image("https://media.giphy.com/media/s2qXK8wAvkGT6/giphy.gif", caption="Time to celebrate!")
    
    st.markdown("""
    <div class="sub-text">
    Wishing you a fantastic year ahead filled with happiness and success.<br>
    Thank you for being such a great friend. <br>
    <br>
    Here's to achieving all your goals in 2026! 🚀<br>
    <br>
    <b>- Srinjoy</b>
    </div>
    """, unsafe_allow_html=True)

# 4. The Initial UI
st.title("Special Delivery for Twisha 📨")
st.write("I created this web page just to wish you.")

if st.button("✨ Click to Open Your Gift"):
    show_surprise()