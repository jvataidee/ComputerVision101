![Project Image](CV101.png)
# Computer Vision 101 Repository by João Ataíde

João Ataíde is a Data Scientist at Imagem Esri. This repository is dedicated to his practices from the course "Computer Vision 1: Introduction (Python)".

## Course Link
You can access the course at [Computer Vision 1: Introduction (Python)](https://opencv.org/courses)

## Certificate
João Ataíde has successfully completed the course and received a certificate. You can view the certificate [here](https://courses.opencv.org/certificates/8a56e3b3421945f799361f3f28cf44fe).

## Projects
- [`Instagram_filters-project.ipynb`](https://github.com/jvataidee/ComputerVision101/blob/main/Instagram_filters-project.ipynb):This project aims to replicate how Instagram filters work. Users created two Instagram-like filters: a pencil sketch filter, which generates a sketch of the existing image, and a cartoon filter, which produces a "cartoonized" version of the input image.
- [`blemish-project.py`](https://github.com/jvataidee/ComputerVision101/blob/main/blemish-project.py):This project utilizes the OpenCV library to remove imperfections from an image using the inpaint function. It allows the user to click on blemishes, creating a mask that is used to inpaint the image and remove the imperfections. The program also provides instructions for the user, including resetting the image, adjusting the brush radius, and exiting the program.
- [`cromakey-project.py`](https://github.com/jvataidee/ComputerVision101/blob/main/cromakey-project.py):This project involves applying chroma keying to a video by replacing a specified color patch with a background image. The program reads frames from an input video, applies chroma keying using trackbars for color patch, tolerance, and smoothing, and writes the processed frames to an output video. The resulting frames are displayed in real-time, and the program can be exited by pressing 'q'. The chroma keying process includes converting the frames to HSV, creating a mask based on the color patch and tolerance, applying morphological operations for smoothing, and combining the foreground and background images. Optionally, color projection can be enabled for further adjustment of the result.
- [`assigment-QR-Code-Detector.ipynb`](https://github.com/jvataidee/ComputerVision101/blob/main/assigment-QR-Code-Detector.ipynb):This project implements a QR Code Detector and Decoder using OpenCV. The goal is to read an image, detect the QR Code in the image, draw a bounding box around the detected QR Code, print the decoded text, and save and display the result image.
- [`assigment_featureimagealignment.ipynb`](https://github.com/jvataidee/ComputerVision101/blob/main/assigment_featureimagealignment.ipynb):This project addresses the restoration of misaligned historical images, feature detection and matching, homography calculation, and warping to achieve an aligned, colorized image. It's an application of computer vision to preserve history and visual memory. Users work with the Prokudin-Gorskii collection, which contains some of the earliest color images in history.
- [`assigment_panorama.ipynb`](https://github.com/jvataidee/ComputerVision101/blob/main/assigment_panorama.ipynb):This project focuses on creating panoramic images using OpenCV. Images are read and stitched together to create a larger panoramic image, which is then saved and returned.
- [`assignment-autofocus.ipynb`](https://github.com/jvataidee/ComputerVision101/blob/main/assigment_panorama.ipynb):This project focuses on implementing measures of focus for determining the sharpest image in a video sequence. Two methods are implemented: the Variance of absolute values of Laplacian and the Sum Modified Laplacian. The implementation involves calculating the sharpness measure for each frame in the video, comparing them, and identifying the frame with the highest measure of focus. The assignment also includes manually specifying the Region of Interest (ROI) for the flower region in the frame. The grading rubric consists of implementing both methods, and an overall submission evaluation.

## Repository Content
The repository contains various Jupyter notebooks related to the course.

## Additional Information
- No releases published
- No packages published
