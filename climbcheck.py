import os
import sys
import argparse
import cv2
import numpy as np
from ultralytics import YOLO

# Argumenty wejściowe
parser = argparse.ArgumentParser()
parser.add_argument('--model', required=True)  
parser.add_argument('--source', required=True) 
parser.add_argument('--thresh', default=0.7)  # Pewność detekcji
args = parser.parse_args()

model_path = args.model
img_source = args.source
min_thresh = float(args.thresh)

if not os.path.exists(model_path):
    print('ERROR: Model path is invalid.')
    sys.exit(0)

# Ładowanie modelu YOLO
model = YOLO(model_path, task='detect')
labels = model.names 

vid_ext_list = ['.avi', '.mov', '.mp4', '.mkv', '.wmv']

if os.path.isfile(img_source):
    _, ext = os.path.splitext(img_source)
    if ext in vid_ext_list:
        source_type = 'video'
    else:
        print(f'File extension {ext} is not supported.')
        sys.exit(0)
elif 'usb' in img_source:
    source_type = 'usb'
    usb_idx = int(img_source[3:])
else:
    print(f'Input {img_source} is invalid.')
    sys.exit(0)

# Inicjalizacja wideo
if source_type == 'video':
    cap = cv2.VideoCapture(img_source)
elif source_type == 'usb':
    cap = cv2.VideoCapture(usb_idx)

# Kolory dla prostokątów wokół wykrytych obiektów
bbox_colors = [(164, 120, 87), (68, 148, 228), (93, 97, 209), (178, 182, 133), (88, 159, 106)]

# Pętla przetwarzania klatek
while True:
    ret, frame = cap.read()  # Odczyt klatki
    if not ret:
        break  # Zakończenie, jeśli brak klatek

    # Wykrywanie obiektów za pomocą modelu YOLO
    results = model(frame, verbose=False) 
    detections = results[0].boxes

    safe = True
    danger_detected = False  # Flaga wykrycia zagrożenia
    for i in range(len(detections)):
        xyxy = detections[i].xyxy.cpu().numpy().squeeze().astype(int)  # Współrzędne prostokąta
        xmin, ymin, xmax, ymax = xyxy
        classidx = int(detections[i].cls.item())  # Indeks klasy
        classname = labels[classidx]  # Nazwa klasy
        conf = detections[i].conf.item()  # Pewność detekcji

        if conf > min_thresh:  # Sprawdzenie progu pewności
            color = bbox_colors[classidx % len(bbox_colors)]  # Kolor prostokąta
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 2)  # Rysowanie prostokąta
            label = f'{classname}: {int(conf * 100)}%'  # Etykieta z nazwą klasy i pewnością
            labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            label_ymin = max(ymin, labelSize[1] + 10)
            cv2.rectangle(frame, (xmin, label_ymin - labelSize[1] - 10), 
                          (xmin + labelSize[0], label_ymin + baseLine - 10), color, cv2.FILLED)
            cv2.putText(frame, label, (xmin, label_ymin - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
            if classname == "human_without_rope":  # Wykrycie osoby bez liny
                danger_detected = True 

    # Wyświetlenie komunikatu o zagrożeniu
    if danger_detected:
        text = "Danger"
        font_scale = 2
        thickness = 3
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)[0]
        text_x = (frame.shape[1] - text_size[0]) // 2
        text_y = frame.shape[0] - 50
        cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 255), thickness)

    # Wyświetlenie przetworzonej klatki
    cv2.imshow('YOLO detection results', frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):  # Wyjście po naciśnięciu 'q'
        break

# Zwolnienie zasobów
cap.release()
cv2.destroyAllWindows()
