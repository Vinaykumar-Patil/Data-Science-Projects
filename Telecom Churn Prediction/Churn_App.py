# Ignore anoying warnings
import warnings
warnings.filterwarnings('ignore')

# Importing all usefull libraries
import streamlit as st
import joblib 
import pandas as pd
from PIL import Image

# Loading the saved model
model = joblib.load(r"C:\Users\Vinaykumar\OneDrive\Desktop\DS Projects\Telecom Churn Prediction\Churn_Pipeline.pkl")

# Creating the function to make predictions
def predict_churn(customer_data):
    prediction = model.predict(customer_data)
    return prediction

# Creating Streamlit app
def app():
    # Inserting image
    image = Image.open("C:\\Users\\Vinaykumar\\OneDrive\\Desktop\\DS Projects\\Telecom Churn Prediction\\churn.png")
    st.image(image, width=400)

    # Creating a form for the user to input customer data
    st.title("Telecom Churn Prediction")
    st.write("\nPrediction for new data :")
    st.sidebar.subheader("Enter the following details of the customer :")

    account_length = st.sidebar.number_input("Account length", 0, 250)
    voice_messages = st.sidebar.number_input("Number of voice messages", 0, 50)
    intl_plan = st.sidebar.selectbox("International plan", ["Yes","No"])
    intl_mins = st.sidebar.number_input("International minutes", 0, 50)
    intl_calls = st.sidebar.number_input("International calls", 0, 20)
    day_mins = st.sidebar.number_input("Day minutes", 0, 500)
    eve_charge = st.sidebar.number_input("Evening charge", 0, 60)
    night_mins = st.sidebar.number_input("Night minutes", 0, 500)
    customer_calls = st.sidebar.number_input("Customer service calls", 0, 10)

    customer_data = pd.DataFrame({
        "account_length": [account_length],
        "voice_messages": [voice_messages],
        "intl_plan": [intl_plan],
        "intl_mins": [intl_mins],
        "intl_calls": [intl_calls],
        "day_mins": [day_mins],
        "eve_charge": [eve_charge],
        "night_mins": [night_mins],
        "customer_calls": [customer_calls]
    })

    # Converting the "intl_plan" column in numerical form
    customer_data['intl_plan'] = customer_data['intl_plan'].apply(lambda x: 1 if x == 'Yes' else 0)

    # Make a prediction & display the result
    if st.button("Predict"):
        with st.spinner('Making prediction...'):
            result = predict_churn(customer_data)
            if result == 0:
                st.write("This customer is not likely to churn...🙂")
            else:
                st.write("This customer is likely to churn...🤔")

# Calling the app function to run the Streamlit app
if __name__ == '__main__':
    app()
