# Dragon-Fruit-Disease-Detection-System-using-CNN
# Overview

This project focuses on classifying Dragon fruit into different categories based on their health conditions, such as "Fresh Dragon Fruit and Diseased Dragon Fruit ". The goal is to build a machine learning model that can accurately identify and classify fruits into these categories using image data.

# The project involves:

Data preprocessing and augmentation.
Training a deep learning model (e.g., CNN) for image classification.
Evaluating the model using metrics like precision, recall, and F1-score.
Addressing class imbalance and improving model performance for minority classes.

# Dataset

The dataset consists of images of fruits categorized into the following classes:

Fresh Dragon Fruit
Rust Spot
Soft Rot Fruit
Stem Canker
Dataset Statistics

Class	Number of Samples
Fresh Dragon Fruit	2000
Rust Spot	642
Soft Rot Fruit	4050
Stem Canker	32
Dataset Source

The dataset is created by us.

# Project Structure

fruit-disease-classification/
├── data/                    # Folder containing the dataset
├── models/                  # Saved models
├── notebooks/               # Jupyter notebooks for experimentation
├── scripts/                 # Python scripts for training and evaluation
├── utils/                   # Utility functions and helpers
├── requirements.txt         # List of dependencies
├── README.md                # Project documentation
└── .gitignore               # Files and folders to ignore in Git

1. Data Preprocessing
2. Training the Model
3. Evaluating the Model

# Model Performance

The model's performance is evaluated using precision, recall, and F1-score. Below are the results:

Class	Precision	Recall	F1-Score	Support
Fresh Dragon Fruit	0.95	0.87	0.91	2000
Rust Spot	0.51	0.95	0.66	642
Soft Rot Fruit	0.99	0.91	0.95	4050
Stem Canker	0.00	0.00	0.00	32
Accuracy: 90%
Macro Avg F1-Score: 0.63
Weighted Avg F1-Score: 0.91

# Key Observations

The model performs well for majority classes (Fresh Dragon Fruit, Soft Rot Fruit).
Poor performance for the minority class (Stem Canker) due to class imbalance.
Recommendations for improvement include addressing class imbalance and collecting more data for minority classes.

# Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new branch for your feature or bugfix.
Commit your changes and push to the branch.
Submit a pull request.

# For questions or feedback, please contact:

Name : Shruti Sakhare
Email: shrutirsakhare.com
GitHub:https://github.com/shrutisakhare21

