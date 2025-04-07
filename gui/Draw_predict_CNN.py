import tkinter as tk
from tkinter import Canvas, Button, Label
from PIL import Image, ImageDraw, ImageOps
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

# Define the same neural network model structure used during training
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.dropout = nn.Dropout(0.25)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)
        
    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 64 * 7 * 7)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x

# Load the saved model (make sure mnist_cnn.pth is in your project directory)
model = Net()
model.load_state_dict(torch.load("model\mnist_cnn.pth", map_location=torch.device('cpu')))
model.eval()

# Tkinter settings: Create a window for drawing
root = tk.Tk()
root.title("Draw and Predict Digit")

canvas_width = 200
canvas_height = 200
white = 255  # White color for the background
black = 0    # Black color for drawing

# Create a canvas widget
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.grid(row=0, column=0, columnspan=2, pady=2)

# Create a PIL image to capture drawing, with a white background
image1 = Image.new("L", (canvas_width, canvas_height), color=white)
draw = ImageDraw.Draw(image1)

def clear_canvas():
    """Clear the canvas and reset the PIL image."""
    canvas.delete("all")
    draw.rectangle([0, 0, canvas_width, canvas_height], fill=white)

def predict_digit():
    """Preprocess the drawn image, feed it to the model, and display the prediction."""
    # Resize to 28x28 pixels (MNIST format)
    img = image1.resize((28, 28))
    # Invert image: convert white background to black and vice versa
    img = ImageOps.invert(img)
    # Convert the image to a NumPy array and normalize pixel values to [0, 1]
    img_array = np.array(img) / 255.0
    # Convert to a PyTorch tensor and add batch and channel dimensions: shape [1, 1, 28, 28]
    tensor_img = torch.tensor(img_array, dtype=torch.float32).unsqueeze(0).unsqueeze(0)
    
    # Get the model's prediction
    output = model(tensor_img)
    pred = output.argmax(dim=1, keepdim=True).item()
    result_label.config(text="Prediction: " + str(pred))

def paint(event):
    """Draw on the canvas and update the PIL image simultaneously."""
    # Define the brush size
    brush_size = 8
    # Coordinates for the oval (brush stroke)
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    # Draw on the Tkinter canvas
    canvas.create_oval(x1, y1, x2, y2, fill='black', outline='black')
    # Draw on the PIL image (ensure consistency)
    draw.ellipse([x1, y1, x2, y2], fill=black)

# Bind mouse motion to drawing
canvas.bind("<B1-Motion>", paint)

# Create buttons for clearing the canvas and predicting the digit
clear_button = Button(root, text="Clear", command=clear_canvas)
clear_button.grid(row=1, column=0, pady=2)

predict_button = Button(root, text="Predict", command=predict_digit)
predict_button.grid(row=1, column=1, pady=2)

# Label to display prediction result
result_label = Label(root, text="Prediction: None", font=("Helvetica", 16))
result_label.grid(row=2, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()
