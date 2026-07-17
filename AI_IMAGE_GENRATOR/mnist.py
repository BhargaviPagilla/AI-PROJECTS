import time
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

digits = load_digits()
x = digits.data
y = digits.target
x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.7,
    random_state=42
)

print("Training Random Forest Classifier...")
start_time = time.time()
model = RandomForestClassifier(n_estimators=100, random_state=50)
model.fit(x_train, y_train)
training_time = time.time()-start_time

predictions = model.predict(x_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy*100:.2f}%")
print(f"training Time: {training_time:.2f} seconds")

sample = 4
plt.imshow(x_test[sample].reshape(8, 8), cmap='gray')
plt.title(f"Prediction: {predictions[sample]}, Actual: {y_test[sample]}")
plt.axis('off')
plt.show()
