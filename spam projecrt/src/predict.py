import joblib

model = joblib.load("../model.pkl")
vectorizer = joblib.load("../vectorizer.pkl")

msg = "Happy birthday! Have a great day."

vec = vectorizer.transform([msg])

prediction = model.predict(vec)

print(prediction)