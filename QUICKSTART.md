# Quick Start Guide - Diabetes Risk Prediction

Welcome to the Diabetes Risk Prediction project! This guide will help you get started quickly.

## What This Project Does

This machine learning project explores diabetes classification with confidence estimation:

- **Binary Classification**: Predicts whether a person has diabetes (yes/no)
- **Multiclass Classification**: Predicts diabetes stage (Normal, Pre-diabetes, Type 2 Moderate, Type 2 Severe)
- **Confidence Estimation**: Provides reliability scores for predictions using multiple techniques

## Quick Setup (5 minutes)

### Option 1: Automated Setup

```bash
# Clone the repository
git clone https://github.com/M1G039/apc-final-project.git
cd apc-final-project

# Run setup script
python setup.py
```

### Option 2: Manual Setup

```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

## Getting Started with Notebooks

The project includes 3 main notebooks in the `notebooks/` directory:

### 1. Data Exploration (`01_data_exploration.ipynb`)
- Load and explore the diabetes dataset
- Visualize feature distributions
- Analyze correlations
- Create multiclass labels

**Start here if you're new to the project!**

### 2. Binary Classification (`02_binary_classification.ipynb`)
- Train multiple ML models (Logistic Regression, Random Forest, SVM, etc.)
- Evaluate model performance
- Implement confidence estimation:
  - Prediction probabilities
  - Calibration curves
  - Bootstrap confidence intervals
- Compare model accuracies

### 3. Multiclass Classification (`03_multiclass_classification.ipynb`)
- Predict diabetes stages (4 classes)
- Multi-class model evaluation
- Stage-specific confidence analysis
- Calibrated predictions

## Dataset

### Using Real Data

Download the Pima Indians Diabetes Database from:
- [Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/diabetes)

Place `diabetes.csv` in the `data/raw/` directory.

### Using Sample Data

Don't have the dataset? No problem! The notebooks will automatically generate synthetic sample data for you to explore the project structure and methodology.

## What You'll Learn

- **Data Preprocessing**: Cleaning, scaling, and preparing health data
- **Classification Techniques**: Binary and multiclass classification
- **Model Evaluation**: Accuracy, precision, recall, F1-score, ROC-AUC
- **Confidence Estimation**: Multiple techniques for prediction reliability
- **Visualization**: Creating informative plots and confusion matrices

## Key Features

### Models Implemented
- Logistic Regression
- Random Forest
- Gradient Boosting
- Support Vector Machines (SVM)

### Confidence Estimation Techniques
1. **Prediction Probabilities**: Raw model confidence scores
2. **Calibration Curves**: Visualize prediction reliability
3. **Platt Scaling**: Calibrated probability estimates
4. **Bootstrap Methods**: Confidence intervals via resampling

### Visualizations
- Feature correlation heatmaps
- ROC curves
- Confusion matrices
- Calibration plots
- Confidence distributions

## Project Structure

```
apc-final-project/
├── notebooks/              # Jupyter notebooks (start here!)
│   ├── 01_data_exploration.ipynb
│   ├── 02_binary_classification.ipynb
│   └── 03_multiclass_classification.ipynb
├── data/
│   ├── raw/               # Original dataset
│   └── processed/         # Processed data
├── models/                # Saved models
├── results/               # Plots and results
├── requirements.txt       # Python dependencies
├── setup.py              # Setup script
├── README.md             # Full documentation
└── CONTRIBUTING.md       # Contribution guide
```

## Common Issues & Solutions

### Issue: Jupyter not found
```bash
pip install jupyter notebook
```

### Issue: Module not found
```bash
pip install -r requirements.txt
```

### Issue: Kernel crashes
- Check Python version (requires 3.7+)
- Restart kernel in Jupyter
- Reinstall dependencies in a fresh virtual environment

## Next Steps

1. ✅ Run `python setup.py` or install dependencies manually
2. ✅ Launch Jupyter Notebook: `jupyter notebook`
3. ✅ Open `notebooks/01_data_exploration.ipynb`
4. ✅ Run all cells (Cell → Run All)
5. ✅ Explore the visualizations and results
6. ✅ Move to binary classification notebook
7. ✅ Try multiclass classification
8. ✅ Experiment with different models and parameters!

## Getting Help

- **Questions?** Open an issue on GitHub
- **Contributing?** See `CONTRIBUTING.md`
- **Documentation?** Check `README.md`

## Credits

This project was created as a final project for the M.EEC006 Machine Learning course.

**Author**: M1G039

---

Happy Learning! 🎓🔬📊
