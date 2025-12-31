import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="For Subham 🥂",
    page_icon="🚀",
    layout="centered"
)

# 2. Styling (CSS) - Sleek and Modern
st.markdown("""
    <style>
    .stButton>button {
        color: white;
        background-color: #28a745; /* Success Green */
        border-radius: 8px;
        height: 3em;
        width: 100%;
        font-size: 20px;
        font-weight: bold;
        border: none;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        background-color: #218838;
    }
    .header-text {
        font-size: 42px !important;
        font-weight: 800;
        color: #17a2b8; /* Cyan/Blue */
        text-align: center;
    }
    .card {
        background-color: #f8f9fa;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1);
        text-align: center;
        color: #333;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. The Surprise Logic
def show_surprise():
    # Progress bar
    progress_text = "Loading the party..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    
    time.sleep(0.3)
    my_bar.empty()
    
    # Celebration Effects
    st.balloons()
    
    # The Wish
    st.markdown('<h1 class="header-text">Happy New Year, Subham! 🥂</h1>', unsafe_allow_html=True)
    
    # Classic "Cheers" GIF (Leonardo DiCaprio) - Use a direct link or similar
    st.image("https://media.giphy.com/media/BPJmthQ3YRwD6QqcVD/giphy.gif", caption="Cheers to 2026!")
    
    st.markdown("""
    <div class="card">
    Yo Subham! <br>
    <br>
    Wishing you a year full of success, growth, and good times.<br>
    Let's crush our goals this year, bro! 👊<br>
    <br>
    <b>- Srinjoy</b>
    </div>
    """, unsafe_allow_html=True)

# 4. The Initial UI
st.title("Hey Subham! 👋")
st.write("Check out this message I coded for you.")

if st.button("🚀 Launch Surprise"):
    show_surprise()