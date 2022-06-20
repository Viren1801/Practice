import csv
feature_vectors: dict = {}
feature_vectors1: dict = {}


reader = csv.reader(open(r"E:\datasets\peta\person\train.csv", "r"))
for rows in reader:
    k = rows[0]
    v = rows[1]
    feature_vectors[k] = v

reader1 = csv.reader(open(r"E:\datasets\peta\person\test.csv", "r"))
for rows in reader1:
    k1 = rows[0]
    v1 = rows[1]
    feature_vectors1[k1] = v1
    
for k, v in feature_vectors.items():
    print(k, v)