import pandas as pd
from sklearn.model_selection import train_test_split
import os

def load_and_split_data(csv_path):
    # Load the dataset
    df = pd.read_csv(csv_path)
    # Basic cleaning: drop rows with missing values
    df = df.dropna()
    
    # For this example, assume the target column is 'Churn'
    # and that all other columns are features.
    X = df.drop(columns=["Churn"])
    y = df["Churn"]
    
    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Ensure the data directory exists
    os.makedirs("data", exist_ok=True)
    
    # Save the splits to CSV files
    X_train.to_csv("data/train_features.csv", index=False)
    X_test.to_csv("data/test_features.csv", index=False)
    y_train.to_csv("data/train_target.csv", index=False)
    y_test.to_csv("data/test_target.csv", index=False)
    print("Data ingestion and splitting complete.")

if __name__ == "__main__":
    csv_path = "data/churn.csv"
    load_and_split_data(csv_path)
