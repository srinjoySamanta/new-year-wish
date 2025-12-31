import streamlit as st
import time

# 1. Page Configuration (The Tab Title and Icon)
st.set_page_config(
    page_title="For Jayanti ❤️",
    page_icon="💌",
    layout="centered"
)

# 2. Custom CSS to make it look pretty
st.markdown("""
    <style>
    .stButton>button {
        color: white;
        background-color: #ff4b4b;
        border-radius: 20px;
        height: 3em;
        width: 100%;
        font-size: 20px;
    }
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
    }
    .text-body {
        font-size: 18px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. The Logic
def show_surprise():
    # Progress bar for suspense
    progress_text = "Loading surprise..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    
    time.sleep(0.5)
    my_bar.empty()
    
    # The Celebration
    st.balloons()  # This releases balloons on the screen!
    st.snow()      # A bit of winter magic
    
    st.markdown('<p class="big-font">Happy New Year, Jayanti! ✨💖</p>', unsafe_allow_html=True)
    
    st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3R6bWJ5aW16eGZ0a3Z5bW16eGZ0a3Z5bW16eGZ0a3Z5bW16eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o6fJcIM6mG3Ad6lAk/giphy.gif", caption="Here is to another year together!")
    
    st.markdown("""
    <p class="text-body">
    May this year bring you as much happiness as you bring into my life.<br>
    Keep smiling! <br>
    <br>
    <b>- Love, Srinjoy</b>
    </p>
    """, unsafe_allow_html=True)

# 4. The Initial UI
st.title("Hey Jayanti! 👋")
st.write("I have made a small digital gift for you.")
st.write("Click the button below to open it.")

if st.button("🎁 Click to Open Surprise"):
    show_surprise()