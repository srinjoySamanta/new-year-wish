import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="For Sourav 🍻",
    page_icon="🎉",
    layout="centered"
)

# 2. Styling (CSS) - Bold and Cool
st.markdown("""
    <style>
    .stButton>button {
        color: white;
        background-color: #6f42c1; /* Indigo/Purple */
        border-radius: 12px;
        height: 3.5em;
        width: 100%;
        font-size: 20px;
        font-weight: bold;
        border: 2px solid #fff;
        box-shadow: 0px 0px 10px rgba(111, 66, 193, 0.5);
    }
    .stButton>button:hover {
        background-color: #5a32a3;
    }
    .header-text {
        font-size: 45px !important;
        font-weight: 800;
        color: #e83e8c; /* Pinkish-Red */
        text-align: center;
        text-shadow: 1px 1px #333;
    }
    .message-box {
        background-color: #212529; /* Dark Grey */
        color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 18px;
        border-left: 5px solid #e83e8c;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. The Surprise Logic
def show_surprise():
    # Progress bar
    progress_text = "Unlocking festivities..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    
    time.sleep(0.3)
    my_bar.empty()
    
    # Celebration Effects
    st.balloons()
    
    # The Wish
    st.markdown('<h1 class="header-text">Happy New Year, Sourav! 🎸</h1>', unsafe_allow_html=True)
    
    # Funny "Party" GIF (The Office or similar funny dance)
    st.image("https://media.giphy.com/media/l2JIdnF6aJcNqaUwxV/giphy.gif", caption="Mood for 2026!")
    
    st.markdown("""
    <div class="message-box">
    Sourav bhai! <br>
    <br>
    Wishing you a crazy good year ahead.<br>
    May you get everything you want this year (including good grades/salary). 💰<br>
    <br>
    <i>P.S. Party kab de raha hai? (When is the treat?)</i> 😂<br>
    <br>
    <b>- Srinjoy</b>
    </div>
    """, unsafe_allow_html=True)

# 4. The Initial UI
st.title("Message for Sourav 📩")
st.write("I have coded a surprise for you.")

if st.button("🎁 Open Gift"):
    show_surprise()