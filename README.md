# Mnist Digit Recognizer

A simple digit recognition application built with Python, Tkinter, and PyTorch. The app allows users to draw digits and predict them using a pre-trained Convolutional Neural Network (CNN) model on the MNIST dataset.

## Features

- **Draw Digits**: Users can draw digits on a canvas.
- **Predict Digits**: The drawn digit is processed and predicted by a pre-trained CNN model.
- **Easy-to-use GUI**: Built using Tkinter for a smooth user experience.

## Technologies Used

- **Python**: The main programming language.
- **Tkinter**: For building the graphical user interface (GUI).
- **PyTorch**: For the Convolutional Neural Network (CNN) model.
- **NumPy**: For array operations.
- **Pillow (PIL)**: For image processing (e.g., resizing, inversion).

## Setup Instructions

### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/BaghinyanArt/Mnist_Digit_Recognizer.git
```
### Navigate into the project directory

After cloning the repository, navigate into the project directory:

```bash
cd Mnist_Digit_Recognizer
```
### Install Dependencies
This project requires Python dependencies to run. You can install them by using the following command:

```bash
pip install torch numpy pillow
```
### Download the Model File
You need the pre-trained model file mnist_cnn.pth. If you don't have it yet, you can download it from your Google Colab environment or any other source where you've saved it.
Here’s how you can download it from Google Colab (if you're using Colab):

```python 
from google.colab import files
files.download('mnist_cnn.pth')
```
### Running the Application
To run the application, use the following command:

```bash
python Draw_predict_CNN.py
```
This will open a Tkinter window where you can draw digits and predict them using the model.


### How to Use
1.Draw on the Canvas: Use the mouse to draw a digit on the canvas.

2.Click "Predict": Once you finish drawing, click the "Predict" button to see the digit predicted by the model.

3.Clear: If you want to clear the canvas and draw again, click the "Clear" button.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contact
For questions or feedback, please open an issue on this repository.
