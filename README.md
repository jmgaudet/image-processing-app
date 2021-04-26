# Covid-19 Radiology Segmentation & Classification

A project for COMP 478
<br>
Author: Jeremy Gaudet

## How to run jupyter:
You will need jupyter to run the notebook. Install by issuing the following command (assuming Python is installed)
```script 
$ pip install jupyter
```
You can then launch jupyter by typing `jupyter notebook` or `jupyter lab` in the terminal, and going to the directory of where this notebook is located.

## How to run this is particular notebook:
The first thing you will need in the dataset. It can be found [here](https://www.kaggle.com/tawsifurrahman/covid19-radiography-database). It will need to be extracted first before use. Once extracted, pass its directory to the PATH variable located in the third cell if running locally; if using Google Colab, you will need to mount the zip onto your drive first, extract it, and then `cd` into its location.

Next, choose your settings in the global variables box. Image size has been tested between values of (64, 64) to (299, 299). The images themselves are 299x299, so you cannot go above that.

## Other information:
* This project was tested with Python 3.8.6 on a MacBook Pro M1 running TensorFlow natively, and because of such, the requirements.txt file should **NOT** necessarily be followed or installed. It is likely best to create your own Python virtual environment with TensorFlow 2.0+ already installed on it.
* Numpy versions below 1.20 are not compatible with this MacOS version of TensorFlow, and so errors can occur.