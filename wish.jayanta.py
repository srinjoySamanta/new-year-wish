import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="For Dad ❤️",
    page_icon="🙏",
    layout="centered"
)

# 2. Styling (CSS) - Elegant, Royal, and Warm
st.markdown("""
    <style>
    .stButton>button {
        color: white;
        background-color: #B8860B; /* Dark Golden Rod */
        border-radius: 10px;
        height: 3.5em;
        width: 100%;
        font-size: 20px;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        background-color: #DAA520;
    }
    .header-text {
        font-size: 38px !important;
        font-weight: bold;
        color: #003366; /* Midnight Blue */
        text-align: center;
        font-family: 'Times New Roman', serif; /* Classic font */
    }
    .name-text {
        font-size: 28px;
        color: #B8860B;
        text-align: center;
        font-weight: bold;
        margin-top: -20px;
    }
    .message-card {
        background-color: #fdfbf7; /* Off-white paper look */
        padding: 30px;
        border-radius: 10px;
        border: 1px solid #ddd;
        text-align: center;
        font-size: 19px;
        color: #444;
        line-height: 1.6;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    }
    .signature {
        margin-top: 30px;
        text-align: center;
        font-style: italic;
        color: grey;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. The Surprise Logic
def show_surprise():
    # Progress bar
    progress_text = "Sending love and respect..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.015) # Slightly slower for dramatic effect
        my_bar.progress(percent_complete + 1, text=progress_text)
    
    time.sleep(0.5)
    my_bar.empty()
    
    # Celebration Effects (Snow feels more peaceful/elegant than balloons)
    st.snow()
    
    # The Header
    st.markdown('<h1 class="header-text">Happy New Year 2026</h1>', unsafe_allow_html=True)
    st.markdown('<p class="name-text">Mr. Jayanta Kumar Samanta</p>', unsafe_allow_html=True)
    
    # Elegant Fireworks GIF
    st.image("https://media.giphy.com/media/U3qYN8S0j3bpK/giphy.gif", caption="Wishing you the best year ahead")
    
    # The Heartfelt Message
    st.markdown("""
    <div class="message-card">
    <b>Dearest Baba,</b> <br>
    <br>
    Thank you for being my strength and my guide. <br>
    May this coming year bring you excellent health, peace, and endless joy.<br>
    <br>
    I am grateful for everything you do for me.<br>
    <br>
    With love and respect,<br>
    <b>Srinjoy</b>
    </div>
    """, unsafe_allow_html=True)

# 4. The Initial UI
st.title("A Message for You, Baba 📩")
st.write("Please click the button below.")

if st.button("🌟 Open Greeting"):
    show_surprise()