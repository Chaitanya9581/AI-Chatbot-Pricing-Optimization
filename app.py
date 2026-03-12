import streamlit as st
from chatbot import chatbot_response
from price_model import predict_price

st.title("AI Chatbot & Price Optimization System")

menu = ["Chatbot", "Price Optimization"]
choice = st.sidebar.selectbox("Select Feature", menu)

# CHATBOT
if choice == "Chatbot":
    st.header("Customer Support Chatbot")

    user_input = st.text_input("Ask your question:")

    if st.button("Send"):
        response = chatbot_response(user_input)
        st.write("Bot:", response)

# PRICE OPTIMIZATION
elif choice == "Price Optimization":
    st.header("Dynamic Price Prediction")

    demand = st.slider("Demand", 50, 300, 100)
    competitor_price = st.slider("Competitor Price", 10, 50, 20)
    season = st.selectbox("Season", [1,2,3])

    if st.button("Predict Price"):
        price = predict_price(demand, competitor_price, season)
        st.success(f"Recommended Price: ${price}")
