# Stock Control Program

It is a simple stock control program which has been written in Python language. It will be improved.


## Requirements

The program uses MySql query. The user must create database table. In order to create a table, I can recommend MySql Workbench. This GUI is very suitable for beginners.
The table format will be given in following parts.

**connection.py** file is used for the connection the MySql database. The user must write host,user name, password and the database(table) name. 

**mainwindow.py** is a file to create a GUI for the users. It has been obtained to use QtDesigner. The user can change the labels what it wants in language.

**program.py** is the main file that must be runned.

### Needed Modules

For the user only **mysqly.connector** module has been required. 


![alt text](https://github.com/OguzKahrmn/Stock-Control/blob/main/program.png?raw=true)