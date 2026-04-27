# Smart Agriculture Crop Yield Prediction

A simple Python project that predicts crop yield based on environmental factors using Linear Regression.

## Project Structure

```
smart_agriculture_crop_yield_prediction/
├── main.py              # Main execution file with user interaction
├── data.py              # Dataset loading and management
├── analysis.py          # Data analysis, visualization, and prediction model
├── crop_data.csv        # Dataset with environmental factors and crop yields
├── requirements.txt     # Required Python packages
├── run_project.bat      # Easy execution script (Windows)
└── README.md           # This file
```

## Features

- **Data Analysis**: Summary statistics and correlation analysis
- **Visualization**: Graphs showing relationships between factors and crop yield
- **Prediction Model**: Linear Regression for crop yield prediction
- **User Interaction**: Command-line interface for input and predictions
- **Factor Analysis**: Shows how each environmental factor affects crop yield

## Dataset

The dataset contains 50 records with the following columns:
- `rainfall`: Rainfall in millimeters
- `temperature`: Temperature in Celsius
- `soil_quality`: Soil quality rating (1-10 scale)
- `crop_yield`: Crop yield in tons per hectare (target variable)

## Installation and Running

### Method 1: Using run_project.bat (Recommended for Windows)

1. Double-click `run_project.bat`
2. The script will:
   - Create a virtual environment
   - Install required packages
   - Run the main program

### Method 2: Manual Setup

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:
   ```bash
   python main.py
   ```

## Usage

1. Run the program using one of the methods above
2. The program will display data analysis results
3. Enter environmental factors when prompted:
   - Rainfall (mm)
   - Temperature (°C)
   - Soil Quality (1-10 scale)
4. View the predicted crop yield
5. Choose to make another prediction or exit

## Sample Output

```
SMART AGRICULTURE CROP YIELD PREDICTION SYSTEM
============================================================

=== Summary Statistics ===
       rainfall   temperature  soil_quality  crop_yield
count  50.000000    50.000000     50.000000  50.000000
mean  122.254000    24.846000      6.520000   4.126000
std    28.634234     2.134567      1.876543   0.876543
...

=== Correlations with Crop Yield ===
soil_quality: 0.987
rainfall: 0.876
temperature: 0.765

=== Regression Coefficients ===
Intercept: -1.2345
Feature Coefficients:
rainfall: 0.0123 (positive impact)
temperature: 0.0987 (positive impact)
soil_quality: 0.4567 (positive impact)

=== Feature Importance (%) ===
soil_quality: 65.2%
rainfall: 24.1%
temperature: 10.7%

Enter rainfall (mm): 120
Enter temperature (°C): 25
Enter soil quality (1-10 scale): 7

Predicted Crop Yield: 4.15 tons/hectare
```

## How Prediction Works

The system uses Linear Regression to:
1. Analyze historical relationships between environmental factors and crop yields
2. Learn mathematical patterns from the dataset
3. Apply these patterns to predict yields for new conditions

The model identifies how changes in rainfall, temperature, and soil quality have historically affected crop production, then uses these relationships to make predictions.

## Dependencies

- pandas==2.0.3: Data manipulation and analysis
- matplotlib==3.7.1: Data visualization
- scikit-learn==1.3.0: Machine learning algorithms
- numpy==1.24.3: Numerical computing

## Technical Details

- **Algorithm**: Linear Regression
- **Features**: Rainfall, Temperature, Soil Quality
- **Target**: Crop Yield (tons/hectare)
- **Evaluation**: Mean Squared Error, R² Score
- **Data Split**: 80% training, 20% testing

## Notes

- The dataset is synthetic and created for demonstration purposes
- Real-world agricultural data would require more complex models
- The system provides educational insights into basic machine learning concepts
- Visualizations are generated using matplotlib and will display in separate windows
