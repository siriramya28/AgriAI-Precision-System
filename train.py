import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

print("1. Loading dataset...")
df = pd.read_csv("Crop_recommendation.csv")

# Extract inputs (features) and output (target label)
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

# 80% training data, 20% testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("2. Training Decision Tree baseline...")
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)
dt_acc = accuracy_score(y_test, dt.predict(X_test))
print(f"   -> Decision Tree Accuracy: {dt_acc * 100:.2f}%")

print("3. Training Random Forest classifier...")
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_preds = rf.predict(X_test)
rf_acc = accuracy_score(y_test, rf_preds)
print(f"   -> Random Forest Accuracy: {rf_acc * 100:.2f}%")

print("\n--- Detailed Performance Metrics ---")
print(classification_report(y_test, rf_preds))

# Save the trained model to disk
joblib.dump(rf, "crop_model.pkl")
print("\nSuccess: Trained model saved as 'crop_model.pkl'!")