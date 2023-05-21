### VIN-code Classification Documentation

## Overview
This documentation provides information about the VIN classification project, including the data used, the methods and ideas employed, and the accuracy achieved. It also includes usage instructions and author information.
#### The project was created on Windows 10.

## Data
The dataset used for training and scoring is loaded with pytorch and consists of black and white images that show handwritten letters 0–9 A–Z a–z. Each image contains one handwritten character.

## Model Architecture
The VIN classification neural network model is built using the AlexNet architecture. The architecture of the model consists of multiple convolution and pooling layers followed by fully connected layers. The model architecture details are as follows:

- Entrance: Square black-and-white image of the field with the VIN-code, size 28x28.
- Convolutional part:
    - Convolutional Layer 1: 32 filters, kernel size 5x5, stride 1, padding 1, ReLU activation
    - Convolutional Layer 2: 64 filters, kernel size 3x3, padding 1, ReLU activation
    - Max Pooling layer 1: pooling size 2x2, stride 2
    - Convolutional Layer 3: 96 filters, kernel size 3x3, padding 1, ReLU activation
    - Convolutional Layer 4: 64 filters, kernel size 3x3, padding 1, ReLU activation
    - Convolutional Layer 5: 32 filters, kernel size 3x3, padding 1, ReLU activation
    - Max Pooling layer 1: pooling size 2x2, stride 2
- Classifier part:
    - Fully connected layer 1: 2048 units, ReLU activation
    - Fully connected layer 2: 1024 units, ReLU activation
    - Output layer: 47 units (corresponds to the number of VIN characters), linear activation

## Training
The model is trained on the provided dataset using the following configuration:
- Optimizer: Adam
- Learning rate: 0.01
- Loss function: cross-entropy loss
- Batch size: 4096
- Number of epochs: 40

## Accuracy
After training, the model achieved an accuracy of 90% on the validation set.

## Usage
To use the trained model for VIN classification, follow the instructions below:

1. Build docker image using command:.
 ```bash
docker build path -t "image_name"
```
### Example:
```bash
docker build D:\Esobes -t "vin"
```
2. Run the provided inference script `inference.py` using command:
```bash
docker run -it --rm --gpus=all -v "source":destination image_name python3 inference.py --input destination
```
### Example:
```bash
docker run -it --rm --gpus=all -v "D:\im":/app/images sobes python3 inference.py --input /app/images
```
4. The script will process the images and output the classification results in CSV format, with each line containing the ASCII index of the predicted character and the POSIX path to the image sample.

### Example output:
    53, 0_00030.png
    55, 0_00180.png
    64, 0_00330.png
    38, 0_00360.png
## Author
This VIN-code classification project was developed by Namchuk Maksym. If you have any questions, please contact with me: namchuk.maksym@gmail.com


