import torch
import cv2
import os
import json
import socket
import threading
import time

# ----------------------------
# CONFIG
# ----------------------------
PI_IP = "10.184.29.210"
PORT = 5005
BUFFER = 12   # send before last 10–15 sec

IMG_DIR = "lane_images"
OUTPUT_DIR = "lane_results"

os.makedirs(OUTPUT_DIR, exist_ok=True)

lane_images = {
    "lane1": os.path.join(IMG_DIR, "lane1.jpg"),
    "lane2": os.path.join(IMG_DIR, "lane2.jpg"),
    "lane3": os.path.join(IMG_DIR, "lane3.jpg")
}

# ----------------------------
# GLOBAL
# ----------------------------
cycle_time = None

# ----------------------------
# LOAD YOLO MODEL
# ----------------------------
model = torch.hub.load(
    'ultralytics/yolov5',
    'custom',
    path='best_windows.pt',
    source='github'
)

print("✅ YOLO model loaded")

# ----------------------------
# CONNECT TO PI
# ----------------------------
client = socket.socket()
client.connect((PI_IP, PORT))
print(f"✅ Connected to Pi {PI_IP}:{PORT}")

# ----------------------------
# RECEIVE THREAD
# ----------------------------
def receive():
    global cycle_time
    buffer = ""

    while True:
        try:
            data = client.recv(1024)
            if not data:
                continue

            buffer += data.decode()

            while "\n" in buffer:
                msg, buffer = buffer.split("\n", 1)

                try:
                    parsed = json.loads(msg)
                    cycle_time = parsed.get("cycle_time")

                    print(f"\n📥 Cycle Time Received: {cycle_time}s")

                except:
                    pass

        except Exception as e:
            print("⚠ Receive error:", e)
            break

threading.Thread(target=receive, daemon=True).start()

# ----------------------------
# DETECTION FUNCTION
# ----------------------------
def detect_vehicles():
    all_counts = {}

    for lane, img_path in lane_images.items():

        img = cv2.imread(img_path)

        if img is None:
            print(f"❌ Image not found: {img_path}")
            all_counts[lane] = 0
            continue

        results = model(img)
        df = results.pandas().xyxy[0]

        count = len(df)
        all_counts[lane] = count

        # draw boxes
        for _, row in df.iterrows():
            x1, y1, x2, y2 = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)

        save_path = os.path.join(OUTPUT_DIR, f"{lane}_detected.jpg")
        cv2.imwrite(save_path, img)

    return all_counts

# ----------------------------
# COUNTDOWN (SAME LINE ONLY)
# ----------------------------
def countdown(seconds):
    while seconds >= 0:
        print(f"\r{seconds:03d}", end="", flush=True)
        time.sleep(1)
        seconds -= 1

# ----------------------------
# MAIN LOOP
# ----------------------------
while True:

    # 1️⃣ DETECT VEHICLES
    counts = detect_vehicles()

    # 2️⃣ SEND DATA
    try:
        msg = json.dumps(counts) + "\n"
        client.sendall(msg.encode())

        print("\n📤 Sent counts:", counts)

    except Exception as e:
        print("❌ Send error:", e)
        break

    # 3️⃣ WAIT FOR CYCLE TIME
    while cycle_time is None:
        time.sleep(0.5)

    # 4️⃣ CALCULATE WAIT TIME
    wait_time = max(cycle_time - BUFFER, 1)

    print(f"⏳ Countdown starts from {wait_time}s")

    # 5️⃣ COUNTDOWN (SAME LINE)
    countdown(wait_time)

    # 6️⃣ RESET
    cycle_time = None