# challenge-api-deployment
Becode AI Project #5

# API deployment

* Repository: `challenge-api-deployment`
* Type of Challenge: `Learning`
* Duration: `5 days`
* Deadline: `08/12/2020 17:00` **(code)**
* Presentation: `14/12/2020 10:00`
* Team challenge : 4


## Mission objectives 
* Be able to deploy a machine learning model.
* Be able to create a Flask API that can handle a machine learning model.
* Deploy an API to Heroku with Docker.

## The Mission
The real estate company "ImmoEliza" is really happy about your regression model. They would like you to create an API to let their web-devs create a website around it.

## Preparation
In any API use case the first thing to decide *(for each route)*, is the **input** and the **output** you want.
Your very first step will be to decide that.

Here as you will work with a web dev team so you **don't want** to collect your data with a form provided by Flask.
You want to get data in **json format** and to return the data in the same format.

### Input
Your input is:
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
            "swimmingpool": Opional[bool],
            "furnished": Opional[bool],
            "open-fire": Optional[bool],
            "terrace": Optional[bool],
            "terrace-area": Optional[int],
            "facades-number": Optional[int],
            "building-state": Optional["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"]
    }
}
```
Don't forget to specify which param will be required or not.

### Output
Your output should look something like that:
**(This is an example, you will need to decide the format of the prediction (float or string))**
```json
{
    "prediction": Optional[float],
    "error": Optional[str]
}
```
Don't forget to provide an error if something went wrong (in this case, you can also provide an HTTP status code. For more information about that, check the [Flask documentation](https://www.flaskapi.org/api-guide/status-codes/).)


### Must-have features
#### Step 1: Project preparation
* Create a folder to handle your project.
* Create a file `app.py` that will contain the code for your API.
* Create a folder `preprocessing` that will contain all the code to preprocess your data.
* Create a folder `model` that will contain your model.
* Create a folder `predict` that will contain all the code to predict a price.


#### Step 2: Pre-processing pipeline
* Part done by Mikael.
``This python module will contain all the code to preprocess your data. Make sure to think about what will be the format of your data to fit the model.
Also, be sure to know which information HAVE to be there and which one can be empty (NAN).

In `preprocessing` folder:
* Create a file `cleaning_data.py` that will contain all the code that will be used to preprocess the data you will receive to predict a new price. (fill the nan, handle text data,...).
    * Your file should contain a function `preprocess()` that will take a new house's data as input and return those data preprocessed as output.
    * If your data doesn't contain the required information, you should return an error to the user.``

#### Step 3: Fit your data!
* Part done by Joachim & Mikael(?).

``In the `predict` folder:
* Create a file `prediction.py` that will contain all the code used to predict a new house's price.
    * Your file should contain a function `predict()` that will take your preprocessed data as an input and return a price as output.``

#### Step 4: Create your API
* Part done by Joachim.
``In your `app.py` file, create a Flask API that contains:
* A route at `/` that accept:
    * `GET` request and return "alive" if the server is alive.
* A route at `/predict` that accept:
    * `POST` request that receives the data of a house in json format.
    * `GET` request returning a string to explain what the `POST` expect (data and format).``

#### Step 5: Create a Dockerfile to wrap your API
* Part done by Sravanthi.
    ``* Ubuntu
    * Python 3.8
    * Flask
    * All the other dependencies you will need
    * All the files of your project in an `/app` folder that you will previously create.
* Run your `app.py` file with python``

#### Step 6: Deploy your Docker image in Heroku
* Part done by Dilara.
   * Account creation.
   * Sample testing the link between Heroku and Docker.
   * Logging and solving ``P0RT`` issue.
    

#### Step 7: Document your API

You will present your API to a group of web devs, make sure to create a clear readme to explain to them where your API is hosted and how to interact with it. Don't forget to mention:
    * What routes are available? With which methods?
    * What kind of data is expected (How should they be formatted? What is mandatory or not?)
    * What is the output of each route in case of success? What is the output in case of error?
* You have to make a nice presentation **with a professional design** for them.
* You should not show them your code.
* Be ready to answer their questions.


## Deliverables
1. Pimp up the readme file:
    * What, Why, When, How, Who.
    * Pending things to do
2. Use Docker to wrap your API
3. Your API is deployed on Heroku

## Evaluation criterias
| Criteria       | Indicator                                                                             | Yes/No |
|----------------|---------------------------------------------------------------------------------------|--------|
| 1. Is complete | Your API works                                                                        |   [ ]  |
|                | Your API is wrapped in a Docker image                                                 |   [ ]  |
|                | Pimp up the readme. (what, why, how, who)                                              |   [ ]  |
|                | Your model predict                                                                    |   [ ]  |
|                | Your API is deployed on Heroku                                                        |   [ ]  |
| 2. Is good     | The repo doesn't contain unnecessary files.                                           |   [ ]  |
|                | You used typing.                                                                      |   [ ]  |
|                | The presentation is clean.                                                            |   [ ]  |
|                | The web-dev group understood well how your API works.                                 |   [ ]  |



![You've got this!](https://media.giphy.com/media/YSTLV9MkR248Qvxjz3/giphy.gif)
