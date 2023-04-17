import streamlit as st
from textblob import TextBlob

def analyze_text(text):
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity
    if sentiment_polarity <= 0:
        return "The text contains language associated with depression."
    else:
        return "The text does not contain language associated with depression."

def run_app():
    # Set page width and page title
    st.set_page_config(page_title="Depression Analysis App", page_icon=":smiley:", layout="wide")
    
    # Set background color
    page_bg = '''
    <style>
    body {
        background-color: #ff99cc;
        background-image: linear-gradient(315deg, #ff99cc 0%, #ffe8e8 74%);
    }
    h1, h2, h3 {
        color: #FFFFFF;
    }
    </style>
    '''
    st.markdown(page_bg, unsafe_allow_html=True)

    # Set app title and subtitle
    st.title("Depression Analysis App")
    st.markdown("*Analyze text to determine if it contains language associated with depression.*")

    # Create text input and analyze button
    text = st.text_area("Enter your text:", height=150)
    if st.button("Analyze"):
        result = analyze_text(text)
        st.write(result, unsafe_allow_html=True)

if __name__ == "__main__":
    run_app()
