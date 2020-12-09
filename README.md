<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/jotwo/challenge-api-deployment/">
    <img src="assets/immo_logo.svg" alt="Logo" width="150" height="150">
  </a>

  <h3 align="center">Belgian Real Estate Price Prediction
  
   API deployment</h3>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#api">API</a></li>
    <li><a href="#logbook">Logbook</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is the 5th project assigned during [Becode](https://becode.org/)'s AI bootcamp in Brussels. Based on previous projects where we had to scrap Belgian real estate websites, collect the data, clean it and then create a model to predict the prices of other properties, we have to build and deploy an API for one particular model.

This project is more about the deployment than it is about the model. For further discussion, please refer to [this repository](https://github.com/wiiki09/real_estate_regression).


### Built With

* [Python](https://www.python.org/)
* [JSON Schema](https://json-schema.org/)
* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Scikit-learn](https://scikit-learn.org/)
* [Docker](https://www.docker.com/)
* [Heroku](https://www.heroku.com/)



<!-- GETTING STARTED -->
## Getting Started

To work with this API, you have two options. Either work directly with the API at [this URL](https://predict-keras-api.herokuapp.com/), either build it yourself from the sources and deploy it in a Docker container on Heroku as it is explained in the next subsection.

### Prerequisites

You'll need the packages/software described above.

### Installation

#### HEROKU

* **Install the Heroku CLI:**
  * The Heroku Command Line Interface (CLI) makes it easy to create and manage your Heroku apps directly from the terminal.
It’s an essential part of using Heroku.
  ```sh
  sudo snap install --classic heroku
  ```
* **Deployment on Heroku:**
  * Heroku favours Heroku CLI therefore using command line is (ensure the CLI is up-to-date) crucial at this step. 
  ```sh
  heroku login
  ```
  * After logging in to the respective Heroku account, the container needs to be registered with Heroku using 
  ```sh
  heroku container:login
  ```
  * Once the container has been registered, a Heroku repo would be required to push the container which could be created : 
  ```sh
  heroku create <yourapplicationname>
  ```
  **NOTE**: If there is no name stated after '_create_', a random name will be assigned.
  
  * When there is an application repo to push the container, it is time to push the container to web : 
  ```sh
  heroku container:push web --app <yourapplicationname>
  ```
  * Following the 'container:push' , the container should be released on web to be visible with 
  ```sh
  heroku container:release web -app <yourapplicationname>
  ```
  * If the container has been released properly, it is available to see using 
  ```sh
  heroku open --app <yourapplicationname>
  ```
  * Logging is also critical especially if the application is experiencing errors : 
  ```sh
  heroku logs --tail <yourapplicationname>
  ```


**IMPORTANT NOTE:** While with _localhost_ and _Docker_ it is not mandatory to specify the PORT, if one would like to deploy on Heroku, the port needs to be specified within the 'app.py' to avoid crashes.

## API

Our REST API is deployed on Heroku, using a Docker container. It is available at [this address](https://predict-keras-api.herokuapp.com/).

Now, let's describe our simple little API's routes and endpoints and the different HTTP methods that can be used.

### `/`

This route is used with a `GET` method and returns a string "alive" in case the server is running and alive.

### `/predict`

There are two endpoints for this route. The most important one is reached with a `POST` method but it is also accessible with a `GET` method. Let's further discuss these methods.

#### `GET`

This endpoint does not need any input. It returns a string explaining the input data and their format that the `POST` method expects.


#### `POST`

This endpoint is the main one of this API. With it, you will be able to query a price prediction giving abritrary real estate property features. It needs and returns specifically formatted inputs and outputs that will be described below.

##### **Input**

The input is given in a JSON notation of this particular format:

```json
{
    "data": {
        "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
        "area": int,
        "rooms-number": int,
        "zip-code": int,
        "garden": Optional[bool],
        "garden-area": Optional[int],
        "terrace": Optional[bool],
        "terrace-area": Optional[int],
        "facades-number": Optional[int],
        "building-state": Optional["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"],
        "equipped-kitchen": Optional[bool],
        "furnished": Optional[bool],
        "open-fire": Optional[bool],
        "swimmingpool": Optional[bool],
        "land-area": Optional[int],
        "full-address": Optional[str]
    }
}
```

As you can see, the input is wrapped in an object associated to the property `data`. Inside this object, not all the fields are mandatory. The optional ones are clearly tagged and can be ommitted in a request. The names are pretty much self-explanatory.

##### **Output**

The general output of this endpoint can be described with this JSON notation:

```json
{
    "prediction": Optional {
        "price": [float],
        "r2_score":[float]
    }
    "error": Optional[str]
}
```

Both attributes `prediction` and `error` are optional and are in fact mutually exclusive: you either receive a prediction _or_ an error message.

* `prediction` itself contains itself two fields: 
    * `price`: this key is associated to the price predicted by our model
    * `r2_score`: this key is associated to the estimate of the model's R² score (coefficient of determination) based on a segregated test set. Its purpose is to estimate the accuracy of the underlying model in general and can be ignored if not needed.
    
    It is sent back along with a HTTP status code `200 OK`.

* `error` warns the client that it didn't post the input data as expected. It could be because of a mandatory attribute missing (such as `zip-code`) or wrong typing (such as floating number for `area` instead of an integer). All these errors are detected using **JSON Schema** validation according to the schema specified in [`assets/input_schema.json`](assets/input_schema.json).

    `error` contains a one-line string representation of the validation error that was produced using the JSON Schema package. It is written in human understandable English.
    
    It is sent back along with a HTTP status code `400 Bad Request`.


<!-- Authors -->
## Authors
* [**Sravanthi Tarani**](https://github.com/sravanthiai) - *BeCoder* 
* [**Dilara Parry**](https://github.com/trickydaze/) - *BeCoder* 
* [**Joachim Kotek**](https://github.com/jotwo/) - *BeCoder* 
* [**Mikael Dominguez**](https://github.com/wiiki09) - *BeCoder and Dancer* 



<!-- Logbook -->
## Logbook

### Project preparation


#### In `model` folder:

##### Pre-processing data

`data_cleaning.py` :

This class clean the data from the dataset used and create a new dataset that will be the format of your data to fit the model.

##### Modeling

`modeling.py` :

This class create a model from the clean dataset, the scaler and the degree we want for the PolynomialFeatures.
With the model created we can predict the price from estate and give the score of the prediction.

#### Creation of the API
In your `app.py` file, create a Flask API that contains:
* A route at `/` that accept:
    * `GET` request and return "alive" if the server is alive.
* A route at `/predict` that accept:
    * `POST` request that receives the data of a house in json format.
    * `GET` request returning a string to explain what the `POST` expect (data and format).

#### Dockerfile to wrap the API


The way to get our Python code running in a container is to pack it as a Docker image and then run a container based on it.

To generate a Docker image we need to create a Dockerfile which contains instructions needed to build the image. The Dockerfile is then processed by the Docker builder which generates the Docker image. 

* The Dockerfile creates an image with:
    * Ubuntu
    * Python 3.8
    * Flask
    * Gunicorn
    * Sklearn
    * Pandas
    * Numpy
    * All the other dependencies you will need

For each instruction or command from the Dockerfile, the Docker builder generates an image layer and stacks it upon the previous ones. Therefore, the Docker image resulting from the process is simply a read-only stack of different layers.

#### Deploy Docker image in Heroku

* **Preparation for Heroku:**
  * After completing the API part, firstly ```requirements.txt``` file is built with mandatory libraries to run the API. 
  * In order to wrap the API as a Docker container, Dockerfile is created with required Python version, ``app.py`` file and install the requirements using the ```requirements.txt```.
  * For Heroku to interpret which server and Flask direction to use, Procfile is created to use _app_ for Flask and _gunicorn_ on the web server.
  * Lastly, runtime.txt is important to signal Heroku which exact language and which version to use. In our case ```python 3.7.6```.


<!-- CONTACT -->
## Contact

Project Link: [https://github.com/jotwo/challenge-api-deployment](https://github.com/jotwo/challenge-api-deployment)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username

<p>Icônes conçues par <a href="https://www.flaticon.com/fr/auteurs/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/fr/" title="Flaticon">www.flaticon.com</a></p>
