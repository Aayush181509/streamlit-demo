import streamlit as st
import pandas as pd
# from sklearn.linear_model import LogisticRegression
import pickle


@st.cache_data
def load_data():
    data = pd.read_csv("data/train_titanic.csv")
    return pd.DataFrame(data)


# App title
st.title("Titanic Survival Prediction App")

# Load and display dataset
df = load_data()

if st.button("View Data"):
    st.write("## Titanic Dataset", df)


# Load model from pickle file
def load_model():
    with open("models/titanic_model.pkl", "rb") as f:
        return pickle.load(f)


model = load_model()


# Sidebar inputs
st.sidebar.header("Input Passenger Details")
age = st.sidebar.number_input("Age", min_value=0, max_value=100, value=25)
sibsp = st.sidebar.number_input(
    "Number of Siblings/Spouses Aboard", min_value=0, max_value=10, value=0
)
parch = st.sidebar.number_input(
    "Number of Parents/Children Aboard", min_value=0, max_value=10, value=0
)
fare = st.sidebar.number_input("Fare", min_value=0.0, max_value=600.0, value=10.0)
sex = st.sidebar.selectbox("Sex", ["male", "female"])

# Encode input data
sex_encoded = 1 if sex == "male" else 0


# Create input array
input_data = [
    [sex_encoded, age, sibsp, parch, fare]
]

# Make prediction using loaded model
prediction = model.predict(input_data)

# Make prediction
if st.button("Predict"):
    print(input_data)
    prediction = model.predict(input_data)

    # Display prediction
    if prediction[0] == 1:
        st.success("The passenger is predicted to survive.")
    else:
        st.error("The passenger is predicted to not survive.")
