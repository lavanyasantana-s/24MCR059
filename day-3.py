import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load dataset
data = pd.read_csv('D:/24MCR059/StudentsPerformance.csv')

# 2. Preprocessing
# One-Hot Encode categorical features
data_encoded = pd.get_dummies(data, columns=['race/ethnicity', 'parental level of education', 'lunch', 'test preparation course'], drop_first=True)

# Encode target variable (gender)
data_encoded['gender'] = data_encoded['gender'].map({'female': 0, 'male': 1})

# Separate features and target
X = data_encoded.drop('gender', axis=1)
y = data_encoded['gender']

# 3. Scale numerical feature
scaler = StandardScaler()
X[['math score', 'reading score', 'writing score']] = scaler.fit_transform(X[['math score', 'reading score', 'writing score']])

# 4. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 6. Predict and Evaluate
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy of Logistic Regression model: {accuracy*100:.2f}%\n")

# 7. Confusion Matrix and Classification Report
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
