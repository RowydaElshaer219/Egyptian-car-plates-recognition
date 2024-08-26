# Egyptian-car-plates-recognition


# Egyptian Car Plates Recognition in Real-Time

This project implements a real-time system for detecting and recognizing Egyptian car license plates using YOLOv8 for object detection and EasyOCR for optical character recognition (OCR). The system processes video frames, detects cars and their corresponding license plates, and extracts the license plate numbers with high accuracy.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The main goal of this project is to develop an efficient real-time system that can detect and recognize Egyptian car plates from video streams. The system utilizes YOLOv8 for detecting cars and license plates and EasyOCR for reading the license plate numbers.

## Features

- **Real-time detection**: Process video frames in real-time.
- **High accuracy**: Corrects OCR errors using predefined mappings specific to Egyptian license plates.
- **CSV Logging**: Saves detection results to a CSV file.

## Requirements

- Python 3.x
- OpenCV
- PyTorch
- EasyOCR
- YOLOv8 (Ultralytics)

You can install the required Python libraries using the `requirements.txt` file.

