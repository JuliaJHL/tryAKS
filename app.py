import numpy as np
from flask import Flask, request, render_template
import pickle


app = Flask(__name__)
Model = pickle.load(open("model.pkl", "rb"))


def predict_species(features, model):
    """
    predict the species based on features
    :param features: the input feature
    :param model: the classifier
    :return:
    """
    prediction = model.predict(features)[0]
    pred_mapping = {0: "setosa", 1: "versicolor", 2: "virginica"}
    species = pred_mapping[prediction]
    return species


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # read the input data
    features = [float(x) for x in request.form.values()]
    features = [np.array(features)]
    # predict the species
    species = predict_species(features, Model)
    return render_template(
        "index.html", prediction_text="It is {} ^_^!".format(species)
    )


if __name__ == "__main__":
    app.run(debug=True)
