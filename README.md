
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


Egyptian Car Plates Recognition in Real-Time
This project is focused on the detection and recognition of Egyptian car license plates in real-time using the YOLOv8 model and Optical Character Recognition (OCR) techniques. The system is designed to accurately identify vehicles and read license plate numbers in various conditions.

## Project Overview
Features:
YOLOv8 Model: Used for detecting vehicles in real-time.
OCR with EasyOCR: For reading and interpreting the license plate numbers.
SORT Tracking Algorithm: To maintain consistent tracking of vehicles across frames.

Workflow:
Vehicle Detection: The YOLOv8 model detects vehicles within the video feed.
License Plate Detection: A custom-trained YOLOv8 model identifies license plates on the detected vehicles.
License Plate Recognition: The EasyOCR library reads the license numbers, applying format checks and corrections for better accuracy.
Tracking: The SORT algorithm keeps track of vehicles across frames, ensuring accurate association of license plates with the correct vehicles.

## Requirements

- Python 
- OpenCV
- PyTorch
- EasyOCR
- YOLOv8 (Ultralytics)

You can install the required Python libraries using the `requirements.txt` file.

## Research Paper
This project is based on research conducted on Egyptian car plate recognition systems. You can read the full paper ([here](https://lnkd.in/dk25WRCp
)).

