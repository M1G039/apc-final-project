# Diabetes Risk Prediction - Machine Learning Project

Final project for M.EEC006 Machine Learning course

## Project Overview

This project explores various confidence estimation techniques for diabetes classification under both binary (diabetes presence/absence) and multiclass (stage) scenarios.

### Objectives

- **Binary Classification**: Predict diabetes presence or absence
- **Multiclass Classification**: Predict diabetes stages
- **Confidence Estimation**: Implement and compare various confidence estimation techniques
- **Model Evaluation**: Comprehensive evaluation of model performance and uncertainty

## Project Structure

```
apc-final-project/
├── data/                          # Data directory
│   ├── raw/                       # Raw data files
│   └── processed/                 # Processed data files
├── notebooks/                     # Jupyter notebooks
│   ├── 01_data_exploration.ipynb  # Data exploration and visualization
│   ├── 02_binary_classification.ipynb  # Binary classification models
│   └── 03_multiclass_classification.ipynb  # Multiclass classification models
├── models/                        # Saved models
├── results/                       # Results and visualizations
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/M1G039/apc-final-project.git
cd apc-final-project
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Launch Jupyter Notebook:
```bash
jupyter notebook
```

5. Navigate to the `notebooks/` directory and start with `01_data_exploration.ipynb`

## Dataset

This project uses diabetes-related datasets. Common sources include:
- **Pima Indians Diabetes Database** (UCI Machine Learning Repository)
- **CDC Diabetes Health Indicators Dataset**
- Or custom datasets with relevant features

### Features typically include:
- Glucose levels
- Blood pressure
- BMI (Body Mass Index)
- Age
- Insulin levels
- Family history
- And other relevant health indicators

## Methodology

### 1. Data Exploration
- Statistical analysis of features
- Visualization of distributions
- Correlation analysis
- Missing data handling

### 2. Binary Classification
- Models: Logistic Regression, Random Forest, SVM, Neural Networks
- Performance metrics: Accuracy, Precision, Recall, F1-Score, ROC-AUC
- Confidence estimation techniques

### 3. Multiclass Classification
- Classification into diabetes stages (e.g., Normal, Pre-diabetes, Type 1, Type 2)
- Multi-class performance metrics
- Confidence estimation for multi-class predictions

### 4. Confidence Estimation Techniques
- Prediction probabilities
- Bootstrap aggregating
- Calibration techniques (Platt scaling, Isotonic regression)
- Ensemble methods
- Bayesian approaches (if applicable)

## Results

Results will be documented in the notebooks and saved in the `results/` directory, including:
- Model performance comparisons
- Confidence interval visualizations
- ROC curves and confusion matrices
- Feature importance analysis

## Contributors

- M1G039

## License

This project is created for educational purposes as part of the M.EEC006 Machine Learning course.
