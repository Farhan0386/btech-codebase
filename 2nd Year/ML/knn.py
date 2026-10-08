from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Initialize and fit
model = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
model.fit(X_scaled, y)

# Scale test data
X_test_scaled = scaler.transform(X_test)

# Predict
predictions = model.predict(X_test_scaled)