# Simple Robotic Hand Control
##### *THIS IS A PROJECT VERY PERSONALIZED, MAYBE NOT HELPFUL TO YOU*

## Introduction

This is a light project for College Students' Innovation and Entrepreneurship Competition. It is designed for the robotic hand made by our team.

This repository includes three parts. 

1. **C++ files**: They are in `forUNO` directory, which need to be flashed to Arduino Uno board in Arduino-IDE.
2. **Server**: There two connections in the Server. First is the connection between Arduino and the Server using port connection,  which is powered by `PySerial` module. Second is the connection between the Server and the Control Panel, which relies on `WebSocket` protocol. 
3. **Control Panel**: It is a Web Page powered by `Vue.js`. Its design is based on `Naive UI`.

## How to Use

### **Preparation**: Flash the C++ code into Arduino UNO board
Use the Arduino-IDE to flash the `forUNO.ino` file into the Arduino-IDE board
### **Start the Server**: Run the Python files to build WebSocket and Serial connections
Adjust the configurations (Port, BaudRate, etc.) in `config.py`. Then run the command
```python
python main.py
```
### **Open the Control Panel** Run the Web Page using **vite**
Open the `front-end-vite` directory in terminal, then run the following command
```
npm install
```
```
npx vite
```
*Notice: `Node.js` environment is needed.*
