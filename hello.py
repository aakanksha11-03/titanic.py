
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("Student_performance_data_.csv")

print("First 5 Rows of Dataset:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

X = df[['Hours']]
y = df['Scores']
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42      # how many steps u r required for trailning purpose 
)


model = LinearRegression()   # using LR Show Accuracy


model.fit(X_train, y_train)

y_pred = model.predict(X_test)      #


print("\nRegression Equation")
print("----------------------")
print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)

mse = mean_squared_error(y_test, y_pred)
print("\nMean Squared Error (MSE):", mse)       # prediction and te4esting purpose

# Step 11: Calculate Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)
print("Root Mean Squared Error (RMSE):", rmse)

# Step 12: Compare Actual and Predicted Values
comparison = pd.DataFrame({
    'Actual': y_test.values,
    'Predicted': y_pred
})

print("\nActual vs Predicted Values")    
print(comparison)

# Step 13: Plot Best Fit Line
plt.figure(figsize=(8,6))

plt.scatter(X, y, color='blue', label='Actual Data')

plt.plot(X, model.predict(X), color='red', linewidth=2, label='Best Fit Line')

plt.xlabel('Study Hours')
plt.ylabel('Scores')
plt.title('Linear Regression Best Fit Line')
plt.legend()
plt.grid(True)

plt.show()