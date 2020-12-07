<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/jotwo/challenge-api-deployment/">
    <img src="https://www.flaticon.com/svg/static/icons/svg/262/262815.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Belgian Real Estate Price Prediction API deployment</h3>
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

* []()
* []()
* []()



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
2. Install NPM packages
   ```sh
   npm install
   ```


## API

Our REST API is deployed on Heroku, using a Docker container. It is available at [this address](https://link/to/api).

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
            "area": int,
            "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
            "rooms-number": int,
            "zip-code": int,
            "land-area": Optional[int],
            "garden": Optional[bool],
            "garden-area": Optional[int],
            "equipped-kitchen": Optional[bool],
            "full-address": Optional[str],
            "swimmingpool": Optional[bool],
            "furnished": Optional[bool],
            "open-fire": Optional[bool],
            "terrace": Optional[bool],
            "terrace-area": Optional[int],
            "facades-number": Optional[int],
            "building-state": Optional["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"]
    }
}
```

As you can see, the input is wrapped in an object associated to the attribute `data`. 
Inside `data`, not all the fields are mandatory. The optional ones are clearly tagged and can be ommitted in a request. The names are pretty much self-explanatory.

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
    * `r2_score`: this key is associated to the estimate of the model's R² score (coefficient of determination) based on a segregated test set. Its purpose is to estimate the accuracy of the underlying model in general and can be ignored if not needed

* `error` itself are telling the API's user that he didn't post the input data as expected and can take two forms:
    * "features_missing_error": mandatory features were ommitted in the JSON input thus our model can't make a prediction
    * "formatting_error": general error for formatting issues, more particularily it is because input data was not wrapped inside an object associated with the key `data`



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

This class clean the data from the dataset used and create a new dataset
that will be the format of your data to fit the model.

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
To deploy your API, you will use Docker.
* Create a Dockerfile that creates an image with:
    * Ubuntu
    * Python 3.8
    * Flask
    * All the other dependencies you will need
    * All the files of your project in an `/app` folder that you will previously create.
* Run your `app.py` file with python

#### Deploy Docker image in Heroku

* Part done by Dilara.

   * Account creation.
   * Sample testing the link between Heroku and Docker.
   * Logging and solving ``P0RT`` issue.

Heroku will allow you to push your docker container on their server and to start it.

You will find more explanation on the process [here](https://github.com/becodeorg/BXL-Bouman-2.22/tree/master/content/05.deployment/4.Web_Application).

If you have an issue or need more information, the [heroku documentation](https://devcenter.heroku.com/articles/container-registry-and-runtime) is well made!

**WARNING:** [As explained here](https://github.com/becodeorg/BXL-Bouman-2.22/tree/master/content/05.deployment/4.Web_Application), when you deploy on a service like Heroku, you will not want to expose your API on `localhost` because localhost is only reachable from inside the server, also, on some services, the port you will deploy on could be dynamic! In this case, they usually provide you an environment variable that contains the port you can use. (`PORT` on Heroku)



#### API document
You will present your API to a group of web devs, make sure to create a clear readme to explain to them where your API is hosted and how to interact with it. Don't forget to mention:
    * What routes are available? With which methods?
    * What kind of data is expected (How should they be formatted? What is mandatory or not?)
    * What is the output of each route in case of success? What is the output in case of error?
* You have to make a nice presentation **with a professional design** for them.
* You should not show them your code.
* Be ready to answer their questions.



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
