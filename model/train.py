import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

def load_data():
    X_train = pd.read_csv("data/train_features.csv")
    X_test = pd.read_csv("data/test_features.csv")
    y_train = pd.read_csv("data/train_target.csv").squeeze()  # Convert to Series
    y_test = pd.read_csv("data/test_target.csv").squeeze()
    return X_train, X_test, y_train, y_test

def train_model():
    X_train, X_test, y_train, y_test = load_data()
    
    # Start an MLflow run to log parameters and metrics
    with mlflow.start_run():
        # Train a simple logistic regression model
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)
        
        # Evaluate the model
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        mlflow.log_metric("accuracy", accuracy)
        print(f"Model Accuracy: {accuracy}")
        
        # Log the model to MLflow
        mlflow.sklearn.log_model(model, "model")
        
        # Ensure the model directory exists locally
        os.makedirs("model", exist_ok=True)
        # Save the model for later use in the API
        joblib.dump(model, "model/churn_model.pkl")
        
        return model

if __name__ == "__main__":
    train_model()
