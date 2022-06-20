from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.models import Model
import numpy as np
from os import listdir, walk
from os.path import isfile, join
import itertools
from itertools import permutations, combinations, product
from numpy import dot
from numpy.linalg import norm
from tqdm.auto import tqdm
import csv
import pandas as pd

similar_list = []


def getAllFilesInDirectory(directoryPath: str):
    return [(directoryPath + "/" + f) for f in listdir(directoryPath) if isfile(join(directoryPath, f))]


def predict(img_path: str, model: Model):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    return preds


def findDifference(f1, f2):
    # print(np.linalg.norm(f1 - f2))
    return dot(f1, f2) / (norm(f1) * norm(f2))


def calculations(keys):
    for k in keys:
        for v in keys:
            yield (k, v)


def driver():
    feature_vectors: dict = {}
    model = ResNet50(weights='imagenet')
    for img_path in getAllFilesInDirectory(r"E:\datasets\Training data"):
        feature_vectors[img_path] = predict(img_path, model)[0]
    keys = [k for k, v in feature_vectors.items()]
    for k, v in calculations(keys):
        if k != v:
            diff = findDifference(feature_vectors[k], feature_vectors[v])
            if diff >= 0.98:
                similar_list.append(v)
                print(k, "is similar to ", v)


print(similar_list)

driver()
