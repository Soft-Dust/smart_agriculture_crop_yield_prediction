import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

class CropYieldAnalyzer:
    def __init__(self, dataset):
        """
        Initialize the analyzer with dataset.
        Args:
            dataset (pandas.DataFrame): The crop dataset
        """
        self.dataset = dataset
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        
    def display_summary_statistics(self):
        """Display summary statistics of the dataset."""
        print("\n=== Summary Statistics ===")
        print(self.dataset.describe())
        print()
        
        # Calculate and display averages
        print("=== Average Values ===")
        print(f"Average Rainfall: {self.dataset['rainfall'].mean():.2f} mm")
        print(f"Average Temperature: {self.dataset['temperature'].mean():.2f} °C")
        print(f"Average Soil Quality: {self.dataset['soil_quality'].mean():.2f}")
        print(f"Average Crop Yield: {self.dataset['crop_yield'].mean():.2f} tons/hectare")
        print()
    
    def display_correlations(self):
        """Display correlation matrix and correlations with crop yield."""
        print("\n=== Correlation Matrix ===")
        correlation_matrix = self.dataset.corr()
        print(correlation_matrix)
        print()
        
        print("=== Correlations with Crop Yield ===")
        correlations = self.dataset.corr()['crop_yield'].sort_values(ascending=False)
        for factor, corr in correlations.items():
            if factor != 'crop_yield':
                print(f"{factor}: {corr:.3f}")
        print()
    
    def create_visualizations(self):
        """Create and display visualization plots."""
        # Set up the figure with subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Rainfall vs Crop Yield
        ax1.scatter(self.dataset['rainfall'], self.dataset['crop_yield'], 
                   alpha=0.6, color='blue')
        ax1.set_xlabel('Rainfall (mm)')
        ax1.set_ylabel('Crop Yield (tons/hectare)')
        ax1.set_title('Rainfall vs Crop Yield')
        ax1.grid(True, alpha=0.3)
        
        # Temperature vs Crop Yield
        ax2.scatter(self.dataset['temperature'], self.dataset['crop_yield'], 
                   alpha=0.6, color='red')
        ax2.set_xlabel('Temperature (°C)')
        ax2.set_ylabel('Crop Yield (tons/hectare)')
        ax2.set_title('Temperature vs Crop Yield')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
    
    def train_model(self):
        """Train the linear regression model."""
        # Prepare features and target
        features = ['rainfall', 'temperature', 'soil_quality']
        X = self.dataset[features]
        y = self.dataset['crop_yield']
        
        # Split the data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train the model
        self.model = LinearRegression()
        self.model.fit(self.X_train, self.y_train)
        
        # Make predictions on test set
        y_pred = self.model.predict(self.X_test)
        
        # Calculate metrics
        mse = mean_squared_error(self.y_test, y_pred)
        r2 = r2_score(self.y_test, y_pred)
        
        print("\n=== Model Performance ===")
        print(f"Mean Squared Error: {mse:.4f}")
        print(f"R² Score: {r2:.4f}")
        print()
    
    def display_coefficients(self):
        """Display regression coefficients and explain their impact."""
        if self.model is None:
            print("Model not trained yet!")
            return
        
        features = ['rainfall', 'temperature', 'soil_quality']
        coefficients = self.model.coef_
        intercept = self.model.intercept_
        
        print("\n=== Regression Coefficients ===")
        print(f"Intercept: {intercept:.4f}")
        print()
        
        print("Feature Coefficients:")
        for feature, coef in zip(features, coefficients):
            impact = "positive" if coef > 0 else "negative"
            print(f"{feature}: {coef:.4f} ({impact} impact)")
        
        print("\n=== How Each Factor Affects Crop Yield ===")
        print("• Rainfall: Higher rainfall generally increases crop yield")
        print("• Temperature: Higher temperature generally increases crop yield")
        print("• Soil Quality: Better soil quality significantly increases crop yield")
        print()
        
        # Calculate feature importance (absolute coefficients)
        importance = np.abs(coefficients)
        total_importance = np.sum(importance)
        feature_importance = importance / total_importance * 100
        
        print("=== Feature Importance (%) ===")
        for feature, imp in zip(features, feature_importance):
            print(f"{feature}: {imp:.1f}%")
        print()
    
    def predict_yield(self, rainfall, temperature, soil_quality):
        """
        Predict crop yield based on input factors.
        Args:
            rainfall (float): Rainfall in mm
            temperature (float): Temperature in °C
            soil_quality (float): Soil quality (1-10 scale)
        Returns:
            float: Predicted crop yield in tons/hectare
        """
        if self.model is None:
            print("Model not trained yet!")
            return None
        
        # Create input DataFrame with proper column names
        input_data = pd.DataFrame({
            "rainfall": [rainfall],
            "temperature": [temperature],
            "soil_quality": [soil_quality]
        })
        
        # Make prediction
        prediction = self.model.predict(input_data)[0]
        
        return prediction
    
    def run_complete_analysis(self):
        """Run the complete analysis pipeline."""
        print("=== SMART AGRICULTURE CROP YIELD ANALYSIS ===")
        print("=" * 50)
        
        self.display_summary_statistics()
        self.display_correlations()
        self.train_model()
        self.display_coefficients()
        
        # Create visualizations
        print("Generating visualizations...")
        self.create_visualizations()

if __name__ == "__main__":
    # Test the analyzer
    from data import load_dataset
    
    dataset = load_dataset()
    if dataset is not None:
        analyzer = CropYieldAnalyzer(dataset)
        analyzer.run_complete_analysis()
        
        # Test prediction
        test_rainfall = 120.0
        test_temperature = 25.0
        test_soil_quality = 7
        
        prediction = analyzer.predict_yield(test_rainfall, test_temperature, test_soil_quality)
        if prediction is not None:
            print(f"\nTest Prediction:")
            print(f"Input: Rainfall={test_rainfall}mm, Temperature={test_temperature}°C, Soil Quality={test_soil_quality}")
            print(f"Predicted Crop Yield: {prediction:.2f} tons/hectare")
