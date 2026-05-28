# 🚦 AI-Based Traffic Control Using Raspberry Pi

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/YOLOv5-Object%20Detection-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Raspberry%20Pi-4B-red?style=for-the-badge&logo=raspberry-pi" />
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-orange?style=for-the-badge&logo=opencv" />
  <img src="https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?style=for-the-badge&logo=pytorch" />
</p>

> **Major Project | B.Tech in Electronics and Communication Engineering**
> G. Pulla Reddy Engineering College (Autonomous), Kurnool
> Affiliated to JNTUA, Ananthapuramu | 2025–2026

---

## 📌 Overview

An intelligent, adaptive traffic signal control system that uses **computer vision** and **deep learning** to monitor real-time vehicle density across multiple lanes and dynamically adjust traffic signal timings — replacing inefficient fixed-time traffic systems.

Instead of equal green time for all lanes, this system **gives priority to the lane with the most traffic**, reducing congestion, fuel wastage, and unnecessary waiting time.

---

## 🧠 How It Works

```
Camera / Video Input
        ↓
 YOLOv5 Model (Vehicle Detection & Count)
        ↓
 Send Data to Raspberry Pi via TCP/IP
        ↓
 Real-Time Communication Available?
   ├── YES → Calculate Signal Timing Based on Vehicle Density
   └── NO  → Use Predefined Backup Timing Mode
        ↓
 Control Traffic Lights via GPIO Pins
```

---

## ✨ Key Features

- 🔍 **Real-time vehicle detection** using YOLOv5
- ⏱️ **Dynamic signal timing** based on lane-wise vehicle density
- 🔁 **Backup mode** with fixed timings when communication fails
- 🔌 **Hardware control** via Raspberry Pi GPIO pins (Red, Yellow, Green LEDs)
- 📡 **TCP/IP communication** between AI detection system and Raspberry Pi
- 🔄 **Continuous loop** — adapts to changing traffic in real time

---

## 🛠️ Hardware Components

| Component | Description |
|---|---|
| Raspberry Pi 4 Model B | Main controller (BCM2711, Quad-core, 1.5GHz) |
| 5mm LEDs (Red, Yellow, Green) | Represent traffic lights for 3 lanes |
| Resistors (220Ω / 330Ω) | Current-limiting for LEDs |
| Jumper Wires | GPIO-to-breadboard connections |
| Breadboard | Temporary circuit prototyping |
| Camera / Input Video File | Traffic data input source |

---

## 💻 Software & Tools

| Tool | Purpose |
|---|---|
| Python 3.x | Primary programming language |
| YOLOv5 | Real-time vehicle detection & counting |
| OpenCV | Video capture and frame processing |
| PyTorch | Deep learning framework for YOLOv5 inference |
| Socket (TCP/IP) | Communication between PC and Raspberry Pi |
| JSON | Data format for transmitting vehicle counts |
| RPi.GPIO | Raspberry Pi GPIO pin control |
| Raspberry Pi OS | Linux-based OS on Raspberry Pi |
| VNC Viewer | Remote access to Raspberry Pi |
| Thonny / VS Code | IDE for Python development |

---

## 📁 Project Structure

```
ai-traffic-control-raspberry-pi/
│
├── detection/
│   ├── detect_vehicles.py        # YOLOv5 vehicle detection script
│   ├── send_data.py              # TCP/IP client to send counts to Pi
│   └── lane_results/             # Saved detection output images
│
├── raspberry_pi/
│   ├── traffic_controller.py     # Main signal control logic on Pi
│   └── backup_mode.py            # Fallback fixed-timing mode
│
├── assets/
│   └── circuit_diagram.jpg       # Hardware setup image
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/ai-traffic-control-raspberry-pi.git
cd ai-traffic-control-raspberry-pi
```

### 2. Install Dependencies (PC / Detection System)

```bash
pip install -r requirements.txt
```

**requirements.txt** should include:
```
torch
torchvision
opencv-python
numpy
Pillow
```

### 3. Clone YOLOv5

```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

### 4. On Raspberry Pi

```bash
pip install RPi.GPIO
```

Make sure both the PC and Raspberry Pi are on the **same network**.

---

## 🚀 Running the Project

### Step 1 — Start the Raspberry Pi controller

```bash
python3 raspberry_pi/traffic_controller.py
```

### Step 2 — Run vehicle detection on PC

```bash
python3 detection/detect_vehicles.py --source <video_or_image_path>
```

The detection script will automatically send vehicle counts to the Raspberry Pi via TCP/IP. Signal timings will be adjusted dynamically based on the received data.

---

## 📊 Results

- ✅ YOLOv5 successfully detected vehicles across 3 lanes
- ✅ Vehicle counts transmitted to Raspberry Pi via TCP/IP
- ✅ Traffic LEDs controlled sequentially based on lane density
- ✅ Backup mode activated correctly on communication failure

**Sample vehicle counts sent:**
```json
{"lane_1": 36, "lane_2": 27, "lane_3": 12}
```

---

## 🔮 Future Scope

- 🚑 Emergency vehicle detection (ambulance / fire truck priority)
- ☁️ Cloud connectivity and IoT-based multi-intersection control
- 🌧️ Improved AI models for different weather/lighting conditions
- 📱 Mobile app integration for real-time traffic updates
- 🚔 Automatic traffic violation detection

---

## 👥 Team

| Name | Roll Number |
|---|---|
| Dasari Gouri Chandana | 239X5A04J5 |
| Yanadi Harshavardhan | 229X1A0458 |
| Makam Sampath Kumar | 229X1A04G6 |

**Project Guide:** Dr. G. Venkata Ramana Sagar, M.Tech, Ph.D — Associate Professor, ECE Dept
**HOD:** Dr. K. Suresh Reddy, M.Tech, Ph.D — Professor & Head, ECE Dept

**Institution:** G. Pulla Reddy Engineering College (Autonomous), Kurnool
*(Accredited by NBA of AICTE and NAAC of UGC with A⁺ grade)*

---

## 📚 References

- [YOLOv5 Documentation](https://docs.ultralytics.com/yolov5/)
- [YOLOv5 GitHub](https://github.com/ultralytics/yolov5)
- [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/)
- [Running YOLOv5 on Raspberry Pi 4](https://jordan-johnston271.medium.com/tutorial-running-yolov5-machine-learning-detection-on-a-raspberry-pi-4-3938add0f719)

---

## 📄 License

This project was developed as an academic major project for B.Tech ECE at G. Pulla Reddy Engineering College, Kurnool (2025–2026). For academic and educational use only.
