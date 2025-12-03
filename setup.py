"""
Setup script for the Diabetes Risk Prediction project.
This script helps users set up the project environment and download sample data.
"""
import os
import sys
import subprocess


def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 7):
        print("Error: Python 3.7 or higher is required.")
        return False
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True


def install_dependencies():
    """Install required Python packages."""
    print("\nInstalling dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("✗ Failed to install dependencies")
        return False


def check_directory_structure():
    """Verify project directory structure."""
    directories = [
        "data/raw",
        "data/processed",
        "notebooks",
        "models",
        "results"
    ]
    
    print("\nChecking directory structure...")
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            print(f"  Created: {directory}")
        else:
            print(f"  ✓ {directory}")
    return True


def print_next_steps():
    """Print next steps for the user."""
    print("\n" + "="*60)
    print("Setup Complete!")
    print("="*60)
    print("\nNext steps:")
    print("1. Download the Diabetes Health Indicators Dataset from:")
    print("   https://www.kaggle.com/datasets/mohankrishnathalla/diabetes-health-indicators-dataset")
    print("\n2. Place the dataset file in the 'data/raw/' directory")
    print("   Expected filename: 'diabetes_binary_health_indicators_BRFSS2015.csv'")
    print("\n3. Launch Jupyter Notebook:")
    print("   jupyter notebook")
    print("\n4. Open 'notebooks/01_data_exploration.ipynb' to get started")
    print("\nDataset Information:")
    print("- 253,680 survey responses from CDC BRFSS 2015")
    print("- 21 predictor variables + 1 target variable")
    print("- Balanced dataset (50-50 split)")
    print("- Features include health conditions, lifestyle, and demographics")
    print("\nAlternatively, the notebooks will generate sample data if no")
    print("dataset is found, allowing you to explore the project structure.")
    print("="*60)


def main():
    """Main setup function."""
    print("="*60)
    print("Diabetes Risk Prediction - Project Setup")
    print("="*60)
    
    if not check_python_version():
        return
    
    if not check_directory_structure():
        return
    
    response = input("\nWould you like to install dependencies? (y/n): ").strip().lower()
    if response in ['y', 'yes']:
        if not install_dependencies():
            return
    else:
        print("\nSkipping dependency installation.")
    
    print_next_steps()


if __name__ == "__main__":
    main()