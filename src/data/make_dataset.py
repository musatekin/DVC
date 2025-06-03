import pandas as pd
from sklearn.datasets import load_iris
import os

def download_data():
    """Download the Iris dataset and save it as CSV."""
    # Create data directory if it doesn't exist
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)
    
    # Load Iris dataset
    iris = load_iris()
    data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    data['target'] = iris.target
    
    # Save raw data
    data.to_csv('data/raw/iris.csv', index=False)
    print("Raw data saved to data/raw/iris.csv")
    
    # Save processed data (normalized features)
    processed_data = data.copy()
    for column in iris.feature_names:
        processed_data[column] = (processed_data[column] - processed_data[column].mean()) / processed_data[column].std()
    
    processed_data.to_csv('data/processed/iris_processed.csv', index=False)
    print("Processed data saved to data/processed/iris_processed.csv")

if __name__ == '__main__':
    download_data() 