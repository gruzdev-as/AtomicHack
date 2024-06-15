import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO
import os


model = YOLO("../temp/best (1).pt")  #сюда вставить .pt файл модели которую скинем
class_descriptions = {
    'adj': 'прилегающие дефекты',
    'int': 'дефекты целостности',
    'geo': 'дефекты геометрии',
    'pro': 'дефекты постобработки',
    'non': 'дефекты невыполнения'
}

def show_detected_image(img_path):
    img = cv2.imread(img_path)
    results = model(img)
    detect_img = results[0].plot()
    detect_img = cv2.cvtColor(detect_img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(10, 10))
    plt.imshow(detect_img)
    plt.axis('off')
    processed_folder = os.path.join(os.getcwd(), 'tmp\\processed')
    processed_path = os.path.join(processed_folder, "processed_" + os.path.basename(img_path))
    plt.savefig(processed_path, bbox_inches='tight', pad_inches=0.1)
    os.remove(img_path)
    return processed_path
