import pandas as pd
import os

def load_dataset():
    """
    Load the crop dataset from CSV file.
    Returns:
        pandas.DataFrame: Dataset containing agricultural data
    """
    # Get the current directory and construct file path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, 'crop_data.csv')
    
    try:
        # Load dataset
        df = pd.read_csv(csv_path)
        return df
    except FileNotFoundError:
        print(f"Error: Dataset file not found at {csv_path}")
        return None
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def get_dataset_info(df):
    """
    Get basic information about the dataset.
    Args:
        df (pandas.DataFrame): The dataset
    Returns:
        dict: Dataset information
    """
    if df is None:
        return None
    
    info = {
        'shape': df.shape,
        'columns': list(df.columns),
        'missing_values': df.isnull().sum().to_dict(),
        'data_types': df.dtypes.to_dict()
    }
    return info

def display_sample_data(df, num_rows=5):
    """
    Display sample data from the dataset.
    Args:
        df (pandas.DataFrame): The dataset
        num_rows (int): Number of rows to display
    """
    if df is None:
        return
    
    print(f"\n=== Sample Data (First {num_rows} rows) ===")
    print(df.head(num_rows))
    print()

if __name__ == "__main__":
    # Test the data loading
    dataset = load_dataset()
    if dataset is not None:
        print("Dataset loaded successfully!")
        info = get_dataset_info(dataset)
        print(f"Dataset shape: {info['shape']}")
        print(f"Columns: {info['columns']}")
        display_sample_data(dataset)
