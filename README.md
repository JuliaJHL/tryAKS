[![CI](https://github.com/JuliaJHL/IDS721-Proj1-flask/actions/workflows/ci.yml/badge.svg)](https://github.com/JuliaJHL/IDS721-Proj1-flask/actions/workflows/ci.yml)
[![CD](https://github.com/JuliaJHL/IDS721-Proj1-flask/actions/workflows/main_iris-species-prediction-flask.yml/badge.svg)](https://github.com/JuliaJHL/IDS721-Proj1-flask/actions/workflows/main_iris-species-prediction-flask.yml)
## Cloud Continuous Delivery of Microservice (MLOps Focused)

In this project, I wrote an Iris species prediction model in python and built the microservice using flask. GitHub Actions and Azure App Services were applied to build CI/CD. The containerized version of the project has been published to DockerHub. 
![structure](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj1/structure.png)

### Requirements
* Create a Microservice in Flask or Fast API
* Push source code to GitHub
* Configure Build System to Deploy changes
* Use IaC (Infrastructure as Code) to deploy code
* Use either AWS, Azure, GCP (recommended services include Google App Engine, AWS App Runner or Azure App Services)
* Containerization is optional, but recommended

### Dataset and Model
* I used Iris data set (`load_iris` in `sklearn.datasets`) which is made by Ronald Fisher in his 1936 paper. The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris versicolor and Iris virginica). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. 
* I applied `RandomForestClassifier()` as the model for training and prediction.

### Run Project Locally
1. Clone the repo and cd into it:
```
$ git clone https://github.com/JuliaJHL/IDS721-Proj1-flask.git
$ cd IDS721-Proj1-flask
```
2. Create and source the virtual environment:
```
$ python3 -m venv env
$ source env/bin/activate
```
3. Install packages
```
$ make install
```
4. Run the app locally
```
$ python app.py
```

### CI/CD
* Set workflow in GitHub Actions 
  * [![CI](https://github.com/JuliaJHL/IDS721-Proj1-flask/actions/workflows/ci.yml/badge.svg)](https://github.com/JuliaJHL/IDS721-Proj1-flask/actions/workflows/ci.yml)
  * do automatically code format, lint and test.
  * based on `Makefile` and `workflows/ci.yml`
* Use Iac to deploy code on Azure App Services
  * [![CD](https://github.com/JuliaJHL/IDS721-Proj1-flask/actions/workflows/main_iris-species-prediction-flask.yml/badge.svg)](https://github.com/JuliaJHL/IDS721-Proj1-flask/actions/workflows/main_iris-species-prediction-flask.yml)
  * This is the overview of the project deployment. 
    ![azure](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj1/overview.jpg)
    In the deployment center, we can check the deployment settings and logs.
    ![deployment](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj1/deployment.png)
  * We can directly access the microservice using the url (https://iris-species-prediction-flask.azurewebsites.net) 
* Any changes to the main branch will automatically trigger CI/CD

### Examples
When you run the project locally or click [url](https://iris-species-prediction-flask.azurewebsites.net) directly, you will enter this page. 
![start](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj1/start.png)
You need to enter the length and the width of the sepals and petals respectively according to the prompt. Then click the  `Predict` button to get the prediction result of the iris species.
![r1](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj1/r1.png)
![r2](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj1/r2.png)
![r3](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj1/r3.png)

### Containerization (optional)
* Build the image 
```
$ docker build -t iris-species-prediction:v1 .
```
* Run the docker container
```
$ docker run -d -p 8080:8080 --name test-iris iris-species-prediction:v1
```
* Publish in [DockerHub](https://hub.docker.com/repository/docker/juliajhl/iris-species-prediction/general)
   ![docker](https://github.com/JuliaJHL/imgs_readme/blob/main/ids721proj1/docker.png)

### References
* [mlops-python-template](https://github.com/nogibjj/python-template)
* [flask-docs](https://flask.palletsprojects.com/en/2.2.x/)
* [Deploy to Azure App Service using GitHub Actions](https://learn.microsoft.com/en-us/azure/app-service/deploy-github-actions?tabs=applevel)
* [docker-docs](https://docs.docker.com/docker-hub/)