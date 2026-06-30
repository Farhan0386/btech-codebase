import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import sklearn.metrics as metrics

# 1. Load the dataset
data = pd.read_csv('train.csv')

# 2. Set the correct target column for the House Prices dataset
y = data['SalePrice']

# 3. Clean up features (Drop the target and text columns for simplicity)
# Random Forest cannot handle text strings directly without encoding
X = data.drop('SalePrice', axis=1)
X = X.select_dtypes(exclude=['object']) 

# Fill any missing values (NaNs) with the column median so the model doesn't crash
X = X.fillna(X.median())

# 4. Split the data into training and validation sets
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=7)

# 5. Create a Regressor (not a Classifier) and fit it
model = RandomForestRegressor(random_state=7, n_estimators=100)
model.fit(train_X, train_y)

# 6. Predict house prices
pred_y = model.predict(val_X)

# 7. Calculate and print regression metrics
mae = metrics.mean_absolute_error(val_y, pred_y)
r2 = metrics.r2_score(val_y, pred_y)

print("\n=== MODEL PERFORMANCE ===")
print(f"Mean Absolute Error (MAE): ${mae:,.2f}")
print(f"R-squared Score: {r2:.4f}")
print("=========================\n")

# Show a few sample predictions vs actual values
sample_comparison = pd.DataFrame({'Actual': val_y, 'Predicted': pred_y}).head(10)
print("Sample Predictions:")
print(sample_comparison)