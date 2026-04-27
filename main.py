"""
Smart Agriculture Crop Yield Prediction
Main execution file for the crop yield prediction system.
"""

from data import load_dataset, get_dataset_info, display_sample_data
from analysis import CropYieldAnalyzer
import sys

def get_user_input():
    """
    Get user input for environmental factors.
    Returns:
        tuple: (rainfall, temperature, soil_quality)
    """
    print("\n" + "="*60)
    print("CROP YIELD PREDICTION - INPUT ENVIRONMENTAL FACTORS")
    print("="*60)
    
    try:
        # Get rainfall input
        while True:
            rainfall = input("Enter rainfall (mm): ")
            try:
                rainfall = float(rainfall)
                if rainfall < 0:
                    print("Rainfall cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number for rainfall.")
        
        # Get temperature input
        while True:
            temperature = input("Enter temperature (°C): ")
            try:
                temperature = float(temperature)
                # Allow reasonable temperature range
                if temperature < -50 or temperature > 60:
                    print("Temperature seems unrealistic. Please enter a value between -50°C and 60°C.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number for temperature.")
        
        # Get soil quality input
        while True:
            soil_quality = input("Enter soil quality (1-10 scale): ")
            try:
                soil_quality = float(soil_quality)
                if soil_quality < 1 or soil_quality > 10:
                    print("Soil quality must be between 1 and 10. Please try again.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number for soil quality.")
        
        return rainfall, temperature, soil_quality
        
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
        sys.exit(0)

def display_prediction_result(prediction, rainfall, temperature, soil_quality):
    """
    Display the prediction result in a formatted way.
    Args:
        prediction (float): Predicted crop yield
        rainfall (float): Input rainfall
        temperature (float): Input temperature
        soil_quality (float): Input soil quality
    """
    print("\n" + "="*60)
    print("PREDICTION RESULT")
    print("="*60)
    print(f"Input Factors:")
    print(f"  • Rainfall: {rainfall:.1f} mm")
    print(f"  • Temperature: {temperature:.1f} °C")
    print(f"  • Soil Quality: {soil_quality:.1f}/10")
    print()
    print(f"Predicted Crop Yield: {prediction:.2f} tons/hectare")
    print("="*60)

def explain_prediction():
    """
    Provide a brief explanation of how the prediction works.
    """
    print("\n" + "="*60)
    print("HOW PREDICTION WORKS")
    print("="*60)
    print("This system uses Linear Regression to predict crop yield based on:")
    print("  • Historical data of environmental factors")
    print("  • Mathematical relationships between factors and yield")
    print("  • Statistical patterns learned from the dataset")
    print()
    print("The model analyzes how changes in rainfall, temperature, and soil")
    print("quality have historically affected crop yields, then applies these")
    print("patterns to predict yields for new conditions.")
    print("="*60)

def main():
    """
    Main execution function.
    """
    print("SMART AGRICULTURE CROP YIELD PREDICTION SYSTEM")
    print("="*60)
    print("Welcome to the Crop Yield Prediction System!")
    print("This tool helps predict crop yield based on environmental factors.")
    
    # Load dataset
    print("\nLoading dataset...")
    dataset = load_dataset()
    
    if dataset is None:
        print("Error: Could not load the dataset. Please check if 'crop_data.csv' exists.")
        sys.exit(1)
    
    # Display dataset information
    info = get_dataset_info(dataset)
    print(f"Dataset loaded successfully!")
    print(f"Dataset contains {info['shape'][0]} records with {info['shape'][1]} columns")
    
    # Display sample data
    display_sample_data(dataset, num_rows=3)
    
    # Initialize and run analyzer
    print("Running data analysis and training prediction model...")
    analyzer = CropYieldAnalyzer(dataset)
    
    # Run complete analysis (without visualizations for cleaner console output)
    print("\n" + "="*60)
    print("DATA ANALYSIS RESULTS")
    print("="*60)
    
    analyzer.display_summary_statistics()
    analyzer.display_correlations()
    analyzer.train_model()
    analyzer.display_coefficients()
    
    # Explain how prediction works
    explain_prediction()
    
    # Get user input and make prediction
    while True:
        try:
            # Get user input
            rainfall, temperature, soil_quality = get_user_input()
            
            # Make prediction
            prediction = analyzer.predict_yield(rainfall, temperature, soil_quality)
            
            if prediction is not None:
                # Display result
                display_prediction_result(prediction, rainfall, temperature, soil_quality)
                
                # Ask if user wants to make another prediction
                print("\nWould you like to make another prediction?")
                choice = input("Enter 'y' for yes or 'n' for no: ").lower().strip()
                
                if choice != 'y' and choice != 'yes':
                    print("\nThank you for using the Crop Yield Prediction System!")
                    break
            else:
                print("Error: Could not make prediction. Please try again.")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()
