# Hunters Arena: A choose your own adventure

A gentle reminder to all - to open links in a new tab,
hold 'Ctrl' (or '⌘' on Apple devices) as you click!

![Multiple Device Demo](./readme-content/images/desktop-mockup.png)

## Live Site

[Hunters Arena](link)

## Repository

---

## Table of Contents

- [Hunters Arena](#hunters-arena)
  - [Live Site](#live-site)
  - [Repository](#repository)
  - [Table of Contents](#table-of-contents)
  - [Objective](#objective)
  - [Brief](#brief)
    - [**H**unters **A**rena](#hunters-arena)
  - [UX; User Experience Design](#ux--user-experience-design)
    - [User Requirements](#user-requirements)
      - [First Time User](#first-time-user)
      - [Returning User](#returning-user)
      - [Interested Party](#interested-party)
    - [Initial Concept](#initial-concept)
      - [Wireframes](#wireframes)
        - [Desktop](#desktop)
        - [Mobile](#mobile)
      - [Colour Scheme](#colour-scheme)
      - [Typography](#typography)
      - [Imagery](#imagery)
  - [Logic](#logic)
    - [Initial Flow](#initial-flow)
    - [Python Logic](#python-logic)
  - [Features](#features)
    - [Existing Features](#existing-features)
      - [UX](#ux)
      - [Keywords](#keywords)
    - [Features Left to Implement](#features-left-to-implement)
  - [Data Model](#data-model)
  - [Technologies Used](#technologies-used)
    - [Python Packages](#python-packages)
    - [Other Tech](#other-tech)
      - [VSCode Extensions](#vscode-extensions)
  - [Testing](#testing)
    - [Python Testing](#python-testing)
      - [Manual Python Testing](#manual-python-testing)
        - [Manual Testing Documentation](#manual-testing-documentation)
      - [PEP8 Testing](#pep8-testing)
      - [Other Python Testing](#other-python-testing)
    - [W3C Validator](#w3c-validator)
      - [HTML](#html)
      - [CSS](#css)
    - [JSHint](#jshint)
    - [Lighthouse](#lighthouse)
  - [Bugs](#bugs)
    - [Current](#current)
    - [Resolved](#resolved)
  - [Development](#development)
    - [GitHub](#github)
    - [VSCode](#vscode)
      - [Cloning](#cloning)
      - [Editing](#editing)
    - [Working With Python](#working-with-python)
      - [Venv](#venv)
      - [Packages](#packages)
      - [Debugging](#debugging)
    - [Google Sheets](#google-sheets)
      - [Creating Sheets](#creating-sheets)
      - [API Credentials](#api-credentials)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
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
## UX &#8722; User Experience Design

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

#### Wireframes

Due to the nature of this project the program suggested to use 

##### Desktop

![Desktop Wireframe](./readme-content/wireframes/index.png)  

---

#### Colour Scheme

The colour scheme for this project relies heavily on the colours available
through the `colorama` package within Python. I chose the color Cyan for 
the pyfiglet font and the package has allowed a few colours to be applied 
to text within the terminal environment. The colours outside the terminal 
are designed based around a classic CRT style monitor. Contrast checks 
have been done to ensure the 'Run Program' button and text present are 
of a high enough contrast to be easily read.

---

#### Typography


---


### Initial Flow

![Lucid Chart](./readme-content/images/lucidchart.jpg)

---

### Python Logic



---
## Features

### Existing Features

#### UX

