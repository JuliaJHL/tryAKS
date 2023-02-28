import numpy as np
from app import predict_species
import pickle


def test_predict():
    model = pickle.load(open("model.pkl", "rb"))
    features_0 = np.array([4.9, 3.1, 1.5, 0.1], dtype=float).reshape(1, -1)
    features_1 = np.array([5.0, 2.3, 3.3, 1.0], dtype=float).reshape(1, -1)
    features_2 = np.array([6.4, 2.8, 5.6, 2.2], dtype=float).reshape(1, -1)
    assert predict_species(features_0, model) == "setosa"
    assert predict_species(features_1, model) == "versicolor"
    assert predict_species(features_2, model) == "virginica"
