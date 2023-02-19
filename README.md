# Dockerizing a Python Application

![Project Image](project-image-url)

---

### Table of Contents

- [Description](#description)
- [Python Application](#python-application)
- [Dockerizing](#dockerizing)
- [Deployment](#deployment)
- [Author Info](#author-info)

---

## Description

Docker is an incredibly powerful software container platform that has enabled developers to develop and run applications much more efficiently. In this repository, I want to share my experience using Docker, specifically concerning how I dockerized a Python application. The process of dockerizing an application involves packaging the application and its dependencies together, inside a container, which can then be distributed and deployed anywhere. By doing this, it ensures that the application always runs the same, regardless of the environment it is deployed in. With Docker, I have been able to create a robust and secure environment for running my Python applications.

[Back To The Top](#dockerizing-a-python-application)

---

## Python Application

This Python application allows the user to input a team from the Premier League and returns that team's full squad list. It uses the Football-data.org API to retrieve the relevant data, and also implements fuzzy matching to help with any misinputs.

### Packages
-  **requests** 
    
    Used to interact and extract data from the API
- **pandas**

    Used to store the team's squad list in a dataframe

- **fuzzywuzzy**

    Used to deal with any user misinputs

### Example

In the example below the user has inputed **Arsenal**. 
```
Input your Premier League football team here: Arsenal

You have chosen the team Arsenal FC here is the squad list:

             Player Name    Position    Nationality
0        Aaron Ramsdale  Goalkeeper        England
1           Matt Turner  Goalkeeper  United States
2             Ben White     Defence        England
3           Rob Holding     Defence        England
4   Oleksandr Zinchenko     Defence        Ukraine
5     Takehiro Tomiyasu     Defence          Japan
6        Kieran Tierney     Defence       Scotland
7               Gabriel     Defence         Brazil
8        William Saliba     Defence         France
9          Jakub Kiwior     Defence         Poland
10        Thomas Partey    Midfield          Ghana
11             Jorginho    Midfield          Italy
12         Granit Xhaka    Midfield    Switzerland
13      Mohamed El Neny    Midfield          Egypt
14      Martin Ødegaard    Midfield         Norway
15     Leandro Trossard    Midfield        Belgium
16     Emile Smith Rowe    Midfield        England
17         Fabio Vieira    Midfield       Portugal
18        Gabriel Jesus     Offence         Brazil
```

[Back To The Top](#dockerizing-a-python-application)

---

## Dockerizing

### Creating the Dockerfile

In order to Dockerize an application you must create a Dockerfile to contain the application. Below you can see an image of the Dockerfile I created to contain the python application:

![Blank diagram (1)](https://user-images.githubusercontent.com/71076769/219946110-b76ca965-4e68-4730-9d32-9311488985b5.svg)

### Building the Docker Image

Now we muist build the image of the application with this Dockerfile. This acheived by running the following command in the same directory which stores our application and the Dockerfile.

`docker build -t docker-football`

The " -t " applies a tag to the Docker image which allows a reference to the Docker image we just created.

### Running the Docker Application

At first it is intuitive to use the following command to run the Docker application we have just made:

`docker run docker-football`

However this leads to the following error:
```
File "//./football-scraper.py", line 24, in <module>
    team_input = input('Input your Premier League football team here: ')
EOFError: EOF when reading a line
```
This is because in our application we are asking for a user's input and therefore we must specify an interactive instance of our application. This is achieved using the following command:

`docker run -i -t docker-football`

```
Input your Premier League football team here:
```
This now asks the user for their input!

[Back To The Top](#dockerizing-a-python-application)

---

## Deployment

In this section I will explain my experience of deploying my Docker application.

The first step was to log into Docker Hub using a valid username and password. This provided access to the Docker Hub account where the application will be deployed. 

Once logged in, the desired Docker application should be located and the tag of the application should be changed to the desired value. 

The next step is to push the application to Docker Hub. To do this, the command:

`docker push <name of application>` should be run in the terminal. 

This uploads the application to Docker Hub, which can then be tested and run by any user using Docker!

[Back To The Top](#dockerizing-a-python-application)

---

## Author Info

LinkedIn - [George Lopez](https://www.linkedin.com/in/george-benjamin-lopez/)

[Back To The Top](#dockerizing-a-python-application)
