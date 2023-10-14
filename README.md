# Hunters Arena: A choose your own adventure

![Multiple Device Demo](./readme-content/images/responsive.jpg)

## Live Site

[Hunters Arena](link)


## Table of Contents

- [Hunters Arena](#hunters-arena)
  - [Live Site](#live-site)
  - [Table of Contents](#table-of-contents)
  - [Objective](#objective)
  - [Brief](#brief)
    - [**H**unters **A**rena](#hunters-arena)
  - [UX - User Experience Design](#ux-user-experience-design)
    - [How To Play](#how-to-play)
    - [User Requirements](#user-requirements)
      - [First Time User](#first-time-user)
      - [Returning User](#returning-user)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
  - [Data Model](#data-model)
  - [Technologies Used](#technologies-used)
    - [Python Packages](#python-packages)
    - [VSCode Extensions](#vscode-extensions)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [PEP8 Testing](#pep8-testing)
  - [Bugs](#bugs)
    - [Current](#current)
    - [Resolved](#resolved)
  - [Development](#development)
    - [GitHub](#github)
    - [VSCode](#vscode)
    - [Google Sheets](#google-sheets)
      - [Creating Sheets](#creating-sheets)
      - [API Credentials](#api-credentials)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
  - [Credits](#credits)
     - [Acknowledgements](#acknowledgements)

---

## Objective

Design an interactive choose your own adventure game.
The project is deployed on Heroku, using Python.
---

## Brief

### **H**unters **A**rena

The goal of this site is to provide an interactive adventure game with various paths and scenarios.
The final product should:

- be programmatically error free.
- be written using Python.
- have paths leading to an ending that returns to beginning to allow replayability.
- handle all user input errors appropriately.
- give clear instructions regarding use and valid inputs.

---
## UX - User Experience Design

### How To Play
Hunters Arena is a choose your own adventure game. You can read more about the general theme on [Wikipedia](https://en.wikipedia.org/wiki/Text-based_game). This game is based on "The Running Man" theme by Stephen King only in this case if the protagonist survives they win 10 million. The player enters their name in the console, and they are transported to a holding cell deep inside an arena. They must escape the holding cell to begin their ordeal. The code is based on the name they entered previously. The user has three attempts to enter the code correctly otherwise they get locked in the holding cell and must stat the game again. If they do guess correctly they escape the cell to a new area which they can explore. The user has many paths to follow, a large percent ending in death but they must escape through the exit of the arena to win the game. Hunters similar to the general public in stephen king book are hostile and ready to kill, they are not to be trusted.  

There are different ways to win and lose, depending on the player's memory, luck, and skills.

### User Requirements

Some example user stories which will affect the design

#### First Time User

> *"As an adult, I would like to be able to input experience the nostalgia 
> of reading a choose your own adventure book"*
>
> *"As a child, I would like to experince a captivating storyline that has easy accessibility "*
>
> *"As someone who has never used a CLI before, I would like to know my inputs
> are valid"*
> 
> *"As a programmer, I would like to see the diversity and flexibility of the python language"*

#### Returning User

> *"As a returning user, I would like to experience different paths and different stories"*
>
> *"I would like to feel a sense of achievement at the end for remembering the story and path correctly"*
>
> *"If I return to play again, I would like to be able to take a different path but still win the game"*

---

### Initial Concept

I intend to make a choose your own adventure game, i used to read these books as a child
and i like to write short stories. I thought of the idea of using the API as shown in 
the sample project for inputing the pages or scenarios of the story like pages to each cell
in the spreadsheet. I would create a somewhat complex path through a short story for which 
the user input creates the story. I thought of an escape room scenario that provided an 
opportunity to showcase various python commands learned through out the sample project. 
The story developed from this escape room concept.


### Story Flow

![Lucid Chart](./readme-content/images/lucidchart.jpg)

---

### Python Logic



---
## Features

### Existing Features

* Use of Google Spreadsheets API to request specific cells containing a scenario for each user input.
* An escape code scenario to use python functions such as

### Future Features

* A counter of the number of deaths or restarts a user need before game completion.
* A choice of stories, excel spreadsheet containing multiple pages of different stories, the user can choose at the begining of adventure, same python code for each story.
* Implement more puzzles and and code breaking scenariosto the stories.
* Create an inventory the user can draw from to open locks or scale cliffs, like pocket knife and rope for example.
* Properly integrate classes for different instances of the game.

## Data Model

I decided to use a text-based data model. The mechanics, interactions, and story progression are implemented using text-based input and output.

## Technologies Used

### Python Packages

[Python Snippets 3 (Pro)](EricSia.pythonsnippets3pro) - New auto suggestion for Python updated in 2023
[Python Path](mgesbert.python-path) - Python imports utils.

### VSCode Extensions

[Error Lens](usernamehw.errorlens) - Improve highlighting of errors, warnings and other language diagnostics.
[Live Server](ritwickdey.LiveServer) - Launch a development local Server with live reload feature for static & dynamic pages

## Testing

### Manual Testing

* Input incorrect character when receiving the "Do you want to start your adventure?" prompt.
    * Response: Receive an Invalid input message and prompted to enter the character again.

* Input incorrect character when making choice direction.
    * Response: Receive an Invalid input message and prompted to enter the correct character.

* Input correct typre of characters when choosing name.
    * Response: Receive an Invalid input message and prompted to enter the correct type of characters.

* Entering the incorrect code 3 times returns the holding cell permenantly locked.
    * Response: Receive a message promting that the holding cell is locked and asks user would they like to try again.


### PEP8 Testing

[CI Python Linter](https://pep8ci.herokuapp.com/) - Pylint is a Python static code analysis tool which looks for programming errors, 
helps enforcing a coding standard, sniffs for code smells and offers simple refactoring suggestions.


### Bugs

#### Current

* Python & Sheet | Code 429: Quota exceeded for quota metric 'Read requests' - being new to coding and working with API's i discovered 
late into my project that each spreadsheet created by a user has a limited number of read requests. 


#### Resolved

* Issue: Invalid input return repetition

    Explanation: There were two instances of the same variable, so when one instance was called the code returned invalid.
    Solution: Change the variable name of one. There are three scenarios where the user had a choice to go for a weapon 
    or to hide so using the letters wh or hw in the variable choice_hw a third option needed to be created and i chose choice_nh.

* Issue: PEP8 - E501 line too long (83 > 79 characters) issue: 

    Explanation: After completing the general structure of the game code I ran the program through PEP8 CI Python Linter and found that 
    there were many instances of the E501 error. I thought a clever idea might be to continue splitting the loops into various def's 
    and it worked but it was clear that it was becoming complicated.
           

* Issue: 

    Explanation: 
    
        

* Issue: 

    Explanation:

      

* Issue: 

    Explanation: 

       

* Issue: 

    Explanation:


### Validator Testing

* PEP8
   * Error-free code checked on [CI Python Linter](https://pep8ci.herokuapp.com/#).
   * Errors for character length below 80 characters. Made new def functions to contract the story loops in to smaller manageable parts.

## Development

### Github

GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.
[GitHub](https://github.com/)

### VSCode

Visual Studio Code is a streamlined code editor with support for development operations like debugging, task running, and version control. 
It aims to provide just the tools a developer needs for a quick code-build-debug cycle and leaves more complex workflows to fuller featured IDEs, such as Visual Studio IDE.
[VSCode](https://code.visualstudio.com/)
### Google Sheets

https://docs.google.com/spreadsheets/d/1cJHaqoYuqxiKFB8QcVqwG2K4haJS-2Zf4yPUj7eF3QE/edit#gid=0

[Google Sheets API](https://console.cloud.google.com/marketplace/browse?filter=partner:Google%20Enterprise%20API&project=adventureproject3)
The Google Sheets API is a RESTful interface that lets you read and modify a spreadsheet's data. The most common uses of this API include the following tasks:

* Create spreadsheets
* Read and write spreadsheet cell values
* Update spreadsheet formatting
* Manage Connected Sheets

#### Creating Sheets

The primary object in Google Sheets that can contain multiple sheets, each with structured information contained in cells. 
A Spreadsheet resource represents every spreadsheet and has a unique spreadsheetId value, containing letters, numbers, hyphens, or underscores. 
You can find the spreadsheet ID in a Google Sheets URL: https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0

#### API Credentials

Credentials are used to obtain an access token from Google's authorization servers so your app can call Google Workspace APIs. This guide describes how to choose and set up the credentials your app needs.

To obtain credentials for your service account:

* In the Google Cloud console, go to Menu menu > IAM & Admin > Service Accounts.
* Go to Service Accounts and select your service account.
* Click Keys > Add key > Create new key.
* Select JSON, then click Create.
Your new public/private key pair is generated and downloaded to your machine as a new file. Save the downloaded JSON file as credentials.json in your working directory. 

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku:

* Steps for local deployment:
   * Clone the adventureproject3 GitHub repository.
   * Ensure Python is installed and updated to version 3.11.1.
   * Install Colorama, time, os and pyfiglet use pip install to update to the latest version.
   * Enter python3 run.py into the terminal to start the game.

* Steps for deployment to Heroku:
   * pip3 freeze > requirements.txt to pass colorama and other imports to Heroku.
   * Create a new Heroku app.
   * Set Config vars key to "PORT" and value to "8000".
   * Set buildpacks to Python and NodeJS in that order.
   * Link the Heroku app to my GitHub repository.
   * Click on deploy.

## Credits

