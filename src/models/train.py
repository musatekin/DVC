import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os
import yaml

def train_model():
    """Train a Random Forest model on the Iris dataset."""
    # Create models directory if it doesn't exist
    os.makedirs('models', exist_ok=True)
    
    # Load processed data
    data = pd.read_csv('data/processed/iris_processed.csv')
    
    # Split features and target
    X = data.drop('target', axis=1)
    y = data['target']
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)
    
    # Save model
    joblib.dump(model, 'models/iris_model.joblib')
    
    # Save metrics
    os.makedirs('metrics', exist_ok=True)
    with open('metrics/metrics.yaml', 'w') as f:
        yaml.dump({
            'accuracy': float(accuracy),
            'classification_report': report
        }, f)
    
    print(f"Model accuracy: {accuracy:.4f}")
    print("Model saved to models/iris_model.joblib")
    print("Metrics saved to metrics/metrics.yaml")

if __name__ == '__main__':
    train_model() 