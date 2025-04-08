MNIST Digit Recognizer
A handwritten digit recognition application built with TensorFlow and Tkinter that uses a Convolutional Neural Network (CNN) trained on the MNIST dataset to classify hand-drawn digits.
Show Image
Features

Train a CNN model on the MNIST dataset
Interactive GUI for drawing digits and getting real-time predictions
Save and load trained models
Simple and user-friendly interface

Requirements

Python 3.6+
TensorFlow 2.x
NumPy
Matplotlib
Tkinter (included in standard Python installation)
PIL/Pillow

Installation

Clone this repository:

git clone https://github.com/BaghinyanArt/Mnist_Digit_Recognizer.git
cd Mnist_Digit_Recognizer

Install required packages:

pip install tensorflow numpy matplotlib pillow
Project Structure

cnn_model.py: Contains the CNN model architecture
train.py: Script for training the model on MNIST dataset
gui.py: Tkinter-based GUI application for drawing digits and getting predictions
utils.py: Utility functions for data processing and visualization
saved_models/: Directory to store trained models

Usage
Training the Model
Run the training script:
python train.py
You can modify training parameters in the script, including:

Number of epochs
Batch size
Learning rate

Using the GUI
Launch the digit recognition application:
python gui.py
Instructions:

Draw a digit (0-9) on the canvas using your mouse
The application will automatically predict the digit
Use the "Clear" button to reset the canvas

Model Details
The CNN model architecture consists of:

2 convolutional layers with max pooling
Flatten layer
Dense hidden layer with ReLU activation
Output layer with softmax activation

This architecture achieves approximately 99% accuracy on the MNIST test set.
Future Improvements

Add model evaluation metrics display
Implement data augmentation for better training
Add confidence scores for predictions
Support for training on custom datasets

License
This project is licensed under the MIT License - see the LICENSE file for details.
Contact
For questions or feedback, please open an issue on this repository.
