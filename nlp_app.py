# %% [markdown]
# Part 1.1

# %%
import streamlit as st
# NLP Pkgs
from textblob import TextBlob
from nltk.stem.wordnet import WordNetLemmatizer
import re

st.title("NLP App")
text = st.text_area("Enter word to be lamatized")
click = st.button("Analyze")


#Keeping only Text and digits
text = re.sub(r"[^A-Za-z0-9]", " ", text)
#Removes Whitespaces
text = re.sub(r"\'s", " ", text)
# Removing Links if any
text = re.sub(r"http\S+", " link ", text)
# Removes Punctuations and Numbers
text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)
# Splitting Text
text = text.split()
# Lemmatizer
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
text = " ".join(lemmatized_words)

if click:
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0.6:
        custom_emoji = ':blush:'
        st.success(f'Happy : {text}')
    elif sentiment_score < 0.4:
        custom_emoji = ':disappointed:'
        st.warning(f'Sad : {text}')
    else:
        custom_emoji = ':confused:'
        st.info(f'Confused : {text}')
    st.success(f"Polarity Score is: {sentiment_score}")



