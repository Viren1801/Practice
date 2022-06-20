import os
import cv2


def iter_valid_files(path):
    for subdir, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(subdir, file)
            aux = file_path.rpartition("_")
            file_name = aux[0]
            file_number, delimiter, file_ext = aux[2].rpartition(".")
            image = cv2.imread(file_name + "_" + file_number + ".jpg")
            img_height, img_width, img_channels = image.shape
            image = cv2.resize(image, (800, int(800 / img_width * img_height)))
            img_height, img_width, img_channels = image.shape
            with open(file_name + "_" + file_number + ".txt", 'r') as fh:
                for line in fh:
                    cat, cx, cy, w, h = line.split(" ")
                    cx, cy, w, h = float(cx), float(cy), float(w), float(h)
                    start_point = (int((cx - w / 2) * img_width), int((cy - h / 2) * img_height))
                    end_point = (int((cx + w / 2) * img_width), int((cy + h / 2) * img_height))
                    labeled_img = cv2.rectangle(image, start_point, end_point, (255, 0, 0), 2)
            cv2.imshow("Checking bounding boxes", labeled_img)
            cv2.waitKey()

iter_valid_files("E:\coco dataset\coco_v0")
