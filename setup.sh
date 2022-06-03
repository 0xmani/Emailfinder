#!/bin/bash

sudo apt update
sudo apt-get install libleptonica-dev tesseract-ocr libtesseract-dev libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn -y
sudo pip3 install -r requirements.txt
