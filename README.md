
# Psychology Test for fun!
![header](/assets/images/run-program-screenshot.jpg)

This project utilizes well known psychological questionnaires to assess the level of Generalized Anxiety Disorder (GAD) of the user. It can be used for self assessment and includes two questionnaires with 7 and 20 questions. It is intended for educational purpose only. This program must NOT be used as a real, medical or psycholgical assessment. 

The deployed project live link is [HERE](https://psychology-test-17ac581f1251.herokuapp.com/) - ***Use Ctrl (Cmd) and click to open in a new window.*** 


## Contents

- [Introduction](#introduction)
- [Project](#project)
- [Features](#features)
- [Use of Google Sheets](#use-of-google-sheets)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Future Updates](#future-updates)  
- [Validation](#validation)
- [Deployment](#deployment)
- [Bugs](#bugs)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## Introduction

In this project, the user is asked to enter their name and then after a short greeting, they are asked to choose between a short (GAD-7, 7 questions) and a longer (SAS-20, 20 questions). Both questionnaires are meant to be a self assesment about the individual level of anxiety. After answering all questions the score and a its brief description is presented. At this poin the user can choose to get an advice according to their score. Wheher the user decides to get the advice or not, the program asks if they would like to redo one of the questionnaires. When the teh answer to this question is "no" the progream is exited. 

## Project 

The aim of this project is to:

- Give the user a chance to check out their anxiety level (for fun only). 
- Get to know real-life psycholgical questionnaires
- Get an idea of the different levels of anxiety and some possible advices according to the score (from questionnaire)

### User goals:

Have a chance to assess the user's level of anxiety and understand what a certain score in the questionnaires means. If the user desires, they can also get an advice that reflects their assessed level of anxiety.  

### Site owner goals

Present a program that gives clear instructions and information each time a user visits.
Present a program that gives clear feedbaks when inputting wrong data/choice
Read and write information from/to Google Sheets containing the questionnaires and various descriptions.
Give the user an idea of how anxiety assessment looks like

### Pre development

In order to see the general flow of the program I created a flow chart with all the main steps. 

![flow chart](/assets/images/flowchart.jpg)

### Development

The code was written based on the idea depicted in the flow chart above. Each section of the program was written sequentially, meaning that all necessary coding was written for the first functionality and every else was written according to the needs of the development. 
The first part of the program is dedicated to the imports and the declaration of variables. Particularly important was the idea to crate variables that contain the link to the GoogleSheet cells, in which the information for the questionnaires and the descriptions is stored. 

## Features

### Slow Typing Instructions

In order to display the information in a more readable way and more user friendly, I used a typing effect that prints the letters of each word in a slower motion. This is used througout the program. I actually created two functions for this purpose, one that prints the information a bit slower that the other. The slower function was used to display the information obtained from the GoogleSheet. For every other printing the other (a bit faster) function was used. 

### Colored Text Typing

In order to make the text and the providing of information more interesting and fun, in a few places I introduced a colored text.

![colored text](/assets/images/colored-text.jpg)


### Saved name

The name entered by the user is saved in the GoogleSheet so that can be retrieved later in the program if the user decides to re-run the program. At that poin the program greets the user with his name retrieved from the sheet.

![saved name](/assets/images/saved-name.jpg)


### Description of scope of program

The program starts by a brief description of the purpose of the project and a disclaimer (also visible in the screenshot above) to make sure this tool is only used for fun and not for medical purposes. 


### Selection of Questionnaire

The user has the chance to choose between two questionnaires which have a different length. One is composed of 7 and the other of 20 questions. 

![questionnaire choice](/assets/images/choice.jpg)


### Description of questionnaires and results

At all stages of the program a description of the the information is displayed. 
The questionnaires and the achieved score are briefly described.

![description questionnaire](/assets/images/q-description.jpg)


### Chance to get an advice

After the user has completed the chosen questionnaire and found out thier score, the program asks them if they wan to get an advise based on their score. If the participant chooses "yes" the program retrieves a piece of text from the GoogleSheet directly related to the score.
The advice is absolutely given for fun and has no medical or psychological value.

![advice option](/assets/images/advice.jpg)


### Chance to re-take the questionnaires

At the end of the program, regardless of whether the user decided to get the advice, they get the option to re-take the test, including the questionnaire choice.


### Error Handling

The error handling and data validation when the name of the user is entered and when choosing the questionnaire is dealt with the Python Try Except Exception Handling.

![error handling](/assets/images/error-handling.jpg)


## Use of Google Sheets

As already mentioned before, GoogleSheets were used in this project. The purpose was to store the various information such as questionnaires' questions and possible answers and all descriptions and to save the name of the user. In fact, there are two sheets called "questionnaires" and "descriptions".

![google sheets](/assets/images/google-sheet.jpg)


## Technologies Used

- The language used to code this program is Python
- Google API
- Google Sheets

### Resources

- Gitpod 
- Sublime
- GitHub 
- Heroku
- miro.com

### Libraries

[colorama Fore](https://pypi.org/project/colorama/) - for colored text

[typing effect](https://www.101computing.net/python-typing-text-effect/) - for slow motion typing

[datetime](https://docs.python.org/3/library/time.html) - for time functions 

[sleep](https://realpython.com/python-sleep/) - for providing sleep pauses capabilities


## Testing

The code has been tested and the results can be found [here - TESTING](https://github.com/todiane/corri-construction-p3/blob/main/TESTING.md)


## Future Updates

The project could be updated by including more questionnaires, for example or by having different "themes" that could be assessed. 
Another improvement could be to have a login system, which could involve the creation of a username and password. 

If I had more time, I could have also optimized the program by removing recursive code.


## Validation

PEP8 validation was done using the Code Insitute validator - [here - CI PEP8 Validator](https://pep8ci.herokuapp.com/)

Initial validation failed mainly due to lines showing as too long. After segmentin the affected lines, the validation results showed no errors or warnings.

![pep8 validation](/assets/images/pep8ci-validation.jpg)


## Deployment

### Heroku

The Application has been deployed from GitHub to Heroku by following the steps:

1. Create or log in to your account at heroku.com
2. Create a new app, add a unique app name ( for example psychology-test) and then choose your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars add the private API key information using key 'CRED' and into the value area copy the API key information added to the .json file.  Also add a key 'PORT' and value '8000'.
6. Add required buildpacks (further dependencies). For this project, set it up so Python will be on top and Node.js on bottom
7. Go to "Deploy" and select "GitHub" in "Deployment method"
8. To connect Heroku app to your Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below.
9. Choose the branch you want to build your app from
10. If preferred, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
11. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

### Branching the GitHub Repository using GitHub Desktop and Visual Studio Code
1. Go to the GitHub repository.
2. Click on the branch button in the left hand side under the repository name.
3. Give your branch a name.
4. Go to the CODE area on the right and select "Open with GitHub Desktop".
5. You will be asked if you want to clone the repository - say yes.
6. GitHub desktop will suggest what to do next - select Open code using Visual Studio Code.

## Bugs

I am not aware of any bugs in the code


## Credits

The main technique on how to ustilize Google Sheets was taken from the Code Insitute "Love Sandwiches" project. [here](https://github.com/davidelan/love-sandwiches)


No tutorials or videos were used to developed this program, only often googled how to implement certain python functionalities, such as how to import and use the "colorama" library.

The structure of this README.md was taken from Diane Corriette [here](https://github.com/todiane/corri-construction-p3/blob/main/README.md)


## Acknowledgements

I would like to thank Kay Welfare and my fellow students for the inspiration and the support I always receie in our weekly meetings.

A big thank you to my mentor Jubril Akolade for his support and valuable advices.

I am very grateful to my girlfriend who puts up with me when I am under stress becuase of a coding project :-D
