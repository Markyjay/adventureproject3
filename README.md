# Hunters Arena: A choose your own adventure

![Demo](.devcontainer/readme-content/images/huntersarena.jpg)

## Live Site

[Hunters Arena](https://hunters-arena-p3-b9fa9043e5cb.herokuapp.com/)


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
    - [Removed Features](#removed-features)
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

  The primary objective of creating a "Choose Your Own Adventure" Python game for this project is to showcase the depth of Python knowledge acquired during the course at Code Institute. This project serves as a practical demonstration of the skills and techniques learned, encompassing aspects such as data structures, conditional statements, loops, and interactive user input. By developing an engaging and interactive game, I aim to exhibit my proficiency in Python programming and my ability to apply these skills in a creative and practical manner. Additionally, the game provides a platform to demonstrate problem-solving capabilities and the capacity to design and implement a complex, branching narrative, where user choices significantly influence the course of the story. Ultimately, this project is a testament to my expertise in Python and my capacity to create engaging, interactive experiences through coding.

---

## Brief

### **H**unters **A**rena

The aim of this website is to offer an engaging adventure game with multiple paths and scenarios. 
The end product should meet the following criteria:

- Be free of programming errors.
- Be developed using Python.
- Feature paths that lead to an ending, which circles back to the beginning to ensure replayability.
- Handle all user input errors effectively.
- Provide clear and concise instructions on usage and valid inputs.

---
## UX - User Experience Design

### How To Play
Hunters Arena is a choose your own adventure game. You can read more about the general theme on [Wikipedia](https://en.wikipedia.org/wiki/Text-based_game). This game is based on "The Running Man" theme by Stephen King only in this case if the protagonist survives they win 10 million. The player enters their name in the console, and they are transported to a holding cell deep inside an arena. They must escape the holding cell to begin their ordeal. The code is based on the name they entered previously. The user has three attempts to enter the code correctly otherwise they get locked in the holding cell and must stat the game again. If they do guess correctly they escape the cell to a new area which they can explore. The user has many paths to follow, a large percent ending in death but they must escape through the exit of the arena to win the game. Hunters similar to the general public in stephen king book are hostile and ready to kill, they are not to be trusted.  

There are different ways to win and lose, depending on the player's memory, luck, and skills.

### User Requirements

Some example user stories which will affect the design

#### First Time User

 * "As an adult, I would like to be able to input experience the nostalgia of reading a choose your own adventure book"

 * "As a child, I would like to experince a captivating storyline that has easy accessibility "

 * "As someone who has never used a CLI before, I would like to know my inputs are valid"

 * "As a programmer, I would like to see the diversity and flexibility of the python language"

#### Returning User

 * "As a returning user, I would like to experience different paths and different stories"

 * "I would like to feel a sense of achievement at the end for remembering the story and path correctly"

 * "If I return to play again, I would like to be able to take a different path but still win the game"

---

### Initial Concept

I'm planning to create a "Choose Your Own Adventure" game, inspired by the books I enjoyed as a child. Since I have a passion for writing short stories, I came up with the idea of using an API, similar to the one demonstrated in the sample project, to input the different pages or scenarios of the story, representing them as cells in a spreadsheet. This approach will allow me to craft a somewhat intricate narrative, where the user's input shapes the unfolding story. The idea for the story revolves around an escape room scenario, which provides an excellent opportunity to demonstrate various Python commands that I've learned throughout the sample project. This escape room concept served as the foundation for the narrative. 

The overall story has a similar theme to Stephen Kings novel "The Running Man".


### Story Flow

To create and maintain the story path lines the online application Lucid chart was used.
Lucidchart is an online diagramming and visual communication tool that allows users to create various types of diagrams and visual representations. 
It's widely used for a range of purposes, from business process modeling to flowcharts, wireframes, network diagrams, org charts, and more.

![Lucid Chart](.devcontainer/readme-content/images/lucidchart.jpg)

---

### Python Logic
![Python Logic](.devcontainer/readme-content/images/pythonlogic.jpg)
Throughout this program the while loop structure was used to generate the users personal story.
In Python, a while loop is a control flow structure that allows you to repeatedly execute a block of code as long as a specified condition remains true. 
Here's the basic structure of a while loop:

1. Condition: The loop begins by evaluating the specified condition (an expression that results in a Boolean value, either True or False). If the condition is initially True, the code block within the loop will be executed. If the condition is initially False, the code block will be skipped, and the loop will terminate immediately.

2. Code Block: The indented code block following the while statement is the body of the loop. This code is executed repeatedly as long as the condition remains True.

3. Loop Execution: After executing the code block, the program returns to the while statement and reevaluates the condition. If the condition is still True, the loop iterates, and the code block is executed again. This process continues until the condition becomes False.

4. Exiting the Loop: The loop will exit when the condition becomes False. This can happen in two ways:

The condition becomes False before the loop starts (e.g., the condition is initially False).
The condition becomes False during the loop's execution. This can occur if some code within the loop modifies variables or conditions in a way that eventually makes the original condition False.
It's essential to ensure that the condition inside a while loop eventually becomes False to prevent an infinite loop. Infinite loops can consume all available CPU resources and crash the program or system.

---
## Features

### Removed Features

* Use of Google Spreadsheets API to request specific cells containing a scenario for each user input.
    - This feature was removed due to an un fixable error that occured on some devices and also when running the iamresponsive online application. 
      - A Google API 429 error is an HTTP status code that indicates that the client, which could be an application has sent too many requests in a given time frame to a Google API service and has exceeded the API's rate limit. This error is also    commonly referred to as "Rate Limit Exceeded."
  Because I only discovered this error after I had created the program and sent out the deployed link to friends they were reporting this error. I also noticed it later when I used iamresponsive to generate an image of various devices. 

  I replaced this feature by creating a new .JSON file containing the information in the spreadsheet then created a function in the run.py to draw from the new .JSON file.
 

### Existing Features

* The program initially questions the user whether they wish to start adventure or not. The game starts after the user inputs a 'y' to the console. 
  
  ![Adventure Start](.devcontainer/readme-content/images/beginning.jpg)



* The program asks the user to input a valid name. If the name is not valid the program returns - "Invalid name. Please enter only letters for your name".
  
  ![Valid Name Input](.devcontainer/readme-content/images/lettersonly2.jpg)



* Once a valid name has been input to the console the user is introduced to the first scenario where they must escape a holding cell of an arena.
  If the wrong code is inserted 3 times then the user is locked in and asked whether they wish to try again.

  ![Wrong Code](.devcontainer/readme-content/images/wrongcode.jpg)



* Once a valid code is input to the console the program returns Congratulations you have escaped the holding cell.

  ![Escape Code](.devcontainer/readme-content/images/escapecode.jpg)

  To exit the room remember your name 
    1. Last letter. 
    2. Amount of letters. 
    3. Second letter after alphabetically ordered 
    4. Input this and you will step into the arena.


  This escape code scenario was concocted to use python functions such as 

    1. name = name.lower(): Converts the input name to lowercase. This ensures that the case (uppercase or lowercase) of the name doesn't affect the resulting escape code.

    2. last_letter = name[-1]: It extracts the last letter of the lowercase name by using indexing. This letter will be used as the first part of the escape code.

    3. num_letters = len(name): It calculates the number of letters in the name by using the len function. This count is used as the second part of the escape code.

    4. alpha_name = ''.join(sorted(name)): It takes the lowercase name, sorts its letters alphabetically, and then joins them back together into a single string. 
        This ensures that the characters in the name are in a consistent order, regardless of the original order in which they were entered. 
        This sorted string is used to find the third and final part of the escape code.

    5. second_letter = alpha_name[1]: It extracts the second letter from the sorted alpha_name. This letter will be used as the final part of the escape code.

    6. escape_code = f"{last_letter}{num_letters}{second_letter}": Creates the escape code by concatenating the last_letter, num_letters, and second_letter in that order. 
        The resulting code is a combination of the last letter, the number of letters in the name, and the second letter of the alphabetically sorted name.

    The final escape_code is a unique code that depends on the user's input name, making it specific to each user. 
    This code is then used within the program, allowing users to enter it to progress in the adventure game, as seen in the start_adventure function.

### Future Features

The project could include the following elements for an enhanced user experience:

* A counter to keep track of the number of times a user needs to restart before successfully completing the game.
* A choice of stories, presented in an Excel spreadsheet containing multiple pages of distinct narratives. Users can select their preferred story at the outset, with a unified Python codebase for all stories.
* The incorporation of additional puzzles and code-breaking scenarios within the stories to challenge and engage the users.
* The development of an inventory system that allows users to access items such as a pocket knife or rope, which can be used to open locks or surmount obstacles like cliffs.
* A well-structured implementation of classes to manage different instances of the game, ensuring organized and efficient handling of various storylines and user interactions.

## Data Model

For the data model of the "Choose Your Own Adventure" project, a text-based approach has been selected. This text-based data model serves as the foundation for the mechanics, user interactions, and the flow of the story. In this model, the entire adventure is represented using text inputs and outputs, making it an easily accessible and comprehensible format. The user navigates through the story by making choices presented as text prompts, and the system responds with text-based outcomes, providing a dynamic and interactive narrative experience. This approach not only simplifies the implementation of different storylines and user interactions but also enhances the portability and versatility of the project, as it can be run in any environment capable of handling text input and output. This text-based data model effectively captures the essence of classic "Choose Your Own Adventure" storytelling, where the power of imagination and decision-making takes center stage.

## Technologies Used

### Python Packages

[Python Snippets 3 (Pro)](EricSia.pythonsnippets3pro) - New auto suggestion for Python updated in 2023
[Python Path](mgesbert.python-path) - Python imports utils.

### VSCode Extensions

[Error Lens](usernamehw.errorlens) - Improve highlighting of errors, warnings and other language diagnostics.
[Live Server](ritwickdey.LiveServer) - Launch a development local Server with live reload feature for static & dynamic pages

## Testing

### Manual Testing

In the "Choose Your Own Adventure" project, it's crucial to handle user inputs and responses effectively to ensure a smooth and engaging user experience. Here's an elaboration and improvement of the responses to different user input scenarios:

* Input Incorrect Character When Receiving the "Start Your Adventure?" Prompt:
    - Response: If the user enters an invalid character when prompted to start their adventure, the system should provide a clear and informative error message such as "Invalid input. Please enter 'Y' for yes or 'N' for no." 
      The user is then prompted to re-enter a valid character, ensuring that they understand the available choices.
  
* Input Incorrect Character When Making a Choice of Direction:
    - Response: When a user inputs an incorrect character while making a choice in the story, the system should respond with a user-friendly error message like "Invalid input. Please select a valid option (e.g., 'A' for left or 'B' for right)." 
      The user is then encouraged to enter the correct character to proceed.
  
* Input Incorrect Type of Characters When Choosing a Name:
    - Response: If the user provides an invalid name (e.g., using special characters or numbers), the system should detect this and respond with an error message such as "Invalid input. Please enter a valid name using letters only." 
      The user is then given another opportunity to enter a valid name.
  
* Entering the Incorrect Code Three Times Results in the Holding Cell Remaining Permanently Locked:
    - Response: If the user enters the incorrect escape code three times in the escape room scenario, the system should inform the user that the holding cell is now permanently locked. 
      The system should also ask the user if they would like to try again or if they would like to exit the room. This approach maintains engagement while making it clear that repeated incorrect attempts lead to the cell staying locked.


### PEP8 Testing

Pylint is a Python static code analysis tool which looks for programming errors, 
helps enforcing a coding standard, sniffs for code smells and offers simple refactoring suggestions.

[CI Python Linter](.devcontainer/readme-content/images/pylint.jpg)

### Bugs

#### Current

A reported issue involves the escape code input, which seems to be entering random values when the user tries to input their escape code. This problem has been reported by a user who is running the program on a mobile device. However, the issue could not be replicated or verified on other devices, making it challenging to identify the root cause.

Possible Solutions:

- Device-specific Investigation: If possible, perform tests on the user's device to determine if there are device-specific factors causing the issue.
- Logging and Error Handling: Implement more detailed logging and error handling to capture any unexpected behavior or inputs related to the escape code.
- User Feedback: Encourage the user who reported the issue to provide more details about their device, operating system, and any specific steps that trigger the problem.
- Cross-Device Testing: If applicable, conduct further testing on different devices to identify any patterns or potential issues.


#### Resolved

* Issue: Invalid input return repetition

    Explanation: There were two instances of the same variable, so when one instance was called the code returned invalid.
    Solution: Change the variable name of one. There are three scenarios where the user had a choice to go for a weapon 
    or to hide so using the letters wh or hw in the variable choice_hw a third option needed to be created and i chose choice_nh.

* Issue: PEP8 - E501 line too long (83 > 79 characters) issue: 

    Explanation: After completing the general structure of the game code I ran the program through PEP8 CI Python Linter and found that 
    there were many instances of the E501 error. I thought a clever idea might be to continue splitting the loops into various def's 
    and it worked but it was clear that it was becoming complicated.
           

* Issue: I encountered an issue with Google API requests that led to Error 429. This error typically occurs when our application sends too many requests to the Google API in a short amount of time, exceeding the rate limits imposed by Google.

    Explanation: To address the Error 429 issue, I implemented a workaround. I created a new .JSON file that contains all the information from the Google spreadsheet as a list. Additionally, I introduced a function in the main run.py file that connects this new .JSON file to the application. This approach removed the need for the Google API, and so no encountering of the Error 429. Instead of fetching data from the Google Sheets API each time it's needed, the application relies on the locally stored .JSON file.
            

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

The need for this program was removed but i have included it to show case my original intention of using Google API as shown in the Love Sandwiches Sample Project.
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

