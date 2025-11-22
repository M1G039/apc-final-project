# Diabetes Risk Prediction - Machine Learning Project

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange.svg)](https://scikit-learn.org/)

Final project for M.EEC006 Machine Learning course

> **Quick Start**: See [QUICKSTART.md](QUICKSTART.md) for a 5-minute setup guide!

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
├── notebooks/                     # Jupyter notebooks
│   ├── 01_data_exploration.ipynb  # Data exploration and visualization
│   └── 02_binary_classification.ipynb  # Binary classification models
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

3. Connect your venv kernel to Jupyter
```bash
python -m ipykernel install --user --name=your_env_name
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Launch Jupyter Notebook:
```bash
jupyter notebook
```

6. Navigate to the `notebooks/` directory and start with `01_data_exploration.ipynb`

## Dataset
This project uses the **Diabetes Health Indicators Dataset** from the CDC's Behavioral Risk Factor Surveillance System (BRFSS) 2015.

**Source:** [Kaggle - Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/mohankrishnathalla/diabetes-health-indicators-dataset/data)

### Dataset Overview
- Contains 253,680 survey responses from the cleaned BRFSS 2015 survey
- Features 21 predictor variables and 1 target variable (Diabetes_binary)
- The dataset is balanced with an equal 50-50 split of respondents with no diabetes versus those with prediabetes or diabetes
- Target variable: **Diabetes_binary** (0 = no diabetes, 1 = prediabetes or diabetes)

### Features (21 variables)
The dataset includes the following health and lifestyle indicators:

**Health Conditions:**
- `HighBP` - High blood pressure
- `HighChol` - High cholesterol
- `BMI` - Body Mass Index (only continuous variable)
- `Stroke` - History of stroke
- `HeartDiseaseorAttack` - Coronary heart disease or myocardial infarction
- `GenHlth` - General health status (1-5 scale)
- `PhysHlth` - Physical health (number of days in past 30 days)
- `MentHlth` - Mental health (number of days in past 30 days)
- `DiffWalk` - Difficulty walking or climbing stairs

**Lifestyle & Behaviors:**
- `Smoker` - Smoking status
- `PhysActivity` - Physical activity in past 30 days
- `Fruits` - Fruit consumption
- `Veggies` - Vegetable consumption
- `HvyAlcoholConsump` - Heavy alcohol consumption

**Healthcare Access:**
- `AnyHealthcare` - Has any healthcare coverage
- `NoDocbcCost` - Unable to see doctor due to cost
- `CholCheck` - Cholesterol check in past 5 years

**Demographics:**
- `Sex` - Biological sex
- `Age` - Age category (1-13 scale)
- `Education` - Education level
- `Income` - Income level


## Results

Results will be documented in the notebooks and saved in the `results/` directory.

## Contributors

- M1G039
- MafaldaBarros
- Kyunha

## License

This project is created for educational purposes as part of the M.EEC006 Machine Learning course.
