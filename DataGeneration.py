import random

def featureGenration(k):
    features = [1] if random.random() >= 0.5 else [0]
    for i in range(1, k):
        if random.random() >= 0.25:
            features.append(features[i - 1])
        else:
            features.append(1 -features[i - 1])
    return features

def weightGeneration(k):
    a = [0.9**i for i in range(2, k+1)]
    denominator = sum(a)
    weights = []
    for i in range(k - 1):
        weights.append(0.9**(i + 2)/denominator)
    return weights    

def dataPointGeneration(k):
    feature = featureGenration(k)
    weight = weightGeneration(k)
    condition = sum(map(lambda x : x[0]*x[1], zip(feature[1:], weight)))
    y = feature[0] if condition >= 0.5 else 1 - feature[0]
    dataPoint = [feature, y]
    return dataPoint

def dataGeneration(k, m):
    data = []
    for i in range(m):
        data.append(dataPointGeneration(k))
    return data