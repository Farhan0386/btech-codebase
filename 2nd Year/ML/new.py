for i in range(epocks):
    for j in range(len(X_train)):
        # Forward pass
        z1 = np.dot(X_train[j], W1) + b1
        a1 = sigmoid(z1)
        z2 = np.dot(a1, W2) + b2
        a2 = sigmoid(z2)

        # Compute loss (mean squared error)
        loss = np.mean((a2 - y_train[j]) ** 2)

        # Backward pass
        dz2 = a2 - y_train[j]
        dW2 = np.dot(a1.T, dz2)
        db2 = dz2

        dz1 = np.dot(dz2, W2.T) * sigmoid_derivative(a1)
        dW1 = np.dot(X_train[j].T, dz1)
        db1 = dz1

        # Update weights and biases
        W1 -= learning_rate * dW1
        b1 -= learning_rate * db1
        W2 -= learning_rate * dW2
        b2 -= learning_rate * db2

    if i % 100 == 0:
        print(f'Epoch {i}, Loss: {loss}')
