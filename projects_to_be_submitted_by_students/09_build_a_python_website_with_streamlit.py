import streamlit as st
import requests

def fetch_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        data = response.json()
        quote = data[0]["q"]
        author = data[0]["a"]
        return quote, author
    except Exception as e:
        return None, None

st.title("Random Quote Generator")
st.subheader("By ZenQuotes API :")

st.write("Click the button to fetch a motivational quote.")

if st.button("🎲 Generate Quote"):
    quote, author = fetch_quote()
    if quote:
        st.success(f"**{quote}**")
        st.markdown(f"— *{author}*")
    else:
        st.error("⚠️ Could not fetch quote. Please try again later.")

