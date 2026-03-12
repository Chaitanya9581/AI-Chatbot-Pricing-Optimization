import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("dataset.csv")

X = data[["demand", "competitor_price", "season"]]
y = data["price"]

model = LinearRegression()
model.fit(X, y)

def predict_price(demand, competitor_price, season):
    prediction = model.predict([[demand, competitor_price, season]])
    return round(prediction[0], 2)
