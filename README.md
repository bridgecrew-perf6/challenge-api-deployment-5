<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">project_title</h3>
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
    <li><a href="#authors">Authors</a></li>
    <li><a href="#logbook">Logbook</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Here's a blank template to get started:
**To avoid retyping too much info. Do a search and replace with your text editor for the following:**
`github_username`, `repo_name`, `twitter_handle`, `email`, `project_title`, `project_description`


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



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_




### Input of the API

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


### Output of the API

```json
{
    "prediction": Optional[float],
    "error": Optional[str]
}
```
Don't forget to provide an error if something went wrong (in this case, you can also provide an HTTP status code. For more information about that, check the [Flask documentation](https://www.flaskapi.org/api-guide/status-codes/).)




<!-- Authors -->
## Authors
* **Dilara Parry**
* **Sravanthi**
* **Joachim Kotek**
* **Mikael Dominguez** - *BeCoder and Dancer* - [Wiiki](https://github.com/wiiki09)



<!-- Logbook -->
## Logbook

### Project preparation



#### Pre-processing pipeline
This python module will contain all the code to preprocess your data. Make sure to think about what will be the format of your data to fit the model.
Also, be sure to know which information HAVE to be there and which one can be empty (NAN).

In `preprocessing` folder:
* Create a file `cleaning_data.py` that will contain all the code that will be used to preprocess the data you will receive to predict a new price. (fill the nan, handle text data,...).
    * Your file should contain a function `preprocess()` that will take a new house's data as input and return those data preprocessed as output.
    * If your data doesn't contain the required information, you should return an error to the user.

#### Fit the data

In the `predict` folder:
* Create a file `prediction.py` that will contain all the code used to predict a new house's price.
    * Your file should contain a function `predict()` that will take your preprocessed data as an input and return a price as output.

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

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)





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
