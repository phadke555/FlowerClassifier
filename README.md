# Flower Classifier
This repository contains code and resources for a deep learning image classifier that utilizes convolutional neural networks (CNN) and the Transformers library to classify different types of flowers.

### Task Overview
The goal of this project is to build an image classifier that can accurately identify 12 different types of flowers. The flowers included in the classification task are: 'sunflower', 'rose', 'orchid', 'gladiolus', 'dahlia', 'hydrangea', 'anemone', 'lily', 'tulip', 'daisy', 'carnation', and 'daffodil'. By utilizing deep learning techniques and state-of-the-art image models, we aim to achieve high accuracy in flower classification.

### Model and Libraries Used
To perform the image classification task, we employed the 'convnext_tiny_in22k' image model, a compact and efficient CNN model suitable for various image recognition tasks. The model architecture and training process are detailed in the provided Python Notebook.

In implementing the model, we utilized several libraries in Python:

FastAI: A deep learning library built on top of PyTorch, which simplifies the process of training and deploying deep learning models.
PyTorch: A popular deep learning framework that provides powerful tools and utilities for building and training neural networks.
Pandas: A versatile data manipulation library that aids in data preprocessing and analysis.
### Repository Structure
notebooks/: This directory contains the Python Notebook that details the creation of the image classification model. It includes the model architecture, data preprocessing steps, image download, and evaluation using a cross-validation matrix.
app.py: The Python script to run the web application, allowing users to input an image and obtain the predicted class of the flower.
requirements.txt: A file specifying the required dependencies for running the code in this repository.
### Web Application
The trained model is hosted as a web application on HuggingFace Spaces, accessible at the following link: Flower Classifier Web App. Simply upload an image of a flower, and the application will return the predicted class of the flower.
