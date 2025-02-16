import streamlit as st
import numpy as np
import time
import pandas as pd

map_data = {
    "City": [
        "Kathmandu",
        "Thamel",
        "Patan",
        "Bhaktapur",
        "Pokhara",
        "Lalitpur",
        "Bharatpur",
        "Biratnagar",
        "Birgunj",
        "Dharan",
        "Butwal",
        "Hetauda",
        "Janakpur",
    ],
    "lat": [
        27.7172,
        27.7149,
        27.6667,
        27.6710,
        28.2096,
        27.6667,
        27.6833,
        26.4831,
        27.0167,
        26.8126,
        27.7000,
        27.4167,
        26.7337,
    ],
    "lon": [
        85.3240,
        85.3123,
        85.3167,
        85.4278,
        83.9856,
        85.3167,
        84.4333,
        87.2833,
        84.8667,
        87.2833,
        83.4500,
        85.0333,
        85.9167,
    ],
}
if st.checkbox("Show Map"):
    st.map(map_data)
    # st.table(map_data)

x = st.slider("x")  # 👈 this is a widget
st.write(x, "squared is", x * x)


st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name
df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})

option = st.selectbox("Which number do you like best?", df["first column"])

"You selected: ", option


left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button("Press me!")

# # Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        "Sorting hat", ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
    )
    st.write(f"You are in {chosen} house!")


st.markdown("<h1>Starting a long computation...</h1>""",unsafe_allow_html=True)


# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f"Iteration {i + 1}")
    bar.progress(i + 1)
    time.sleep(0.01)

"...and now we're done!"

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")
