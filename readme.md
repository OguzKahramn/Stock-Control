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


![alt text](https://github.com/OguzKahramn/Stock-Control/blob/main/program.png)

The menu looks like the image above. The features are can be seen on the image that:
* The user can add product with its amount by clicking **Save** button.
* The user can decrease the product with its amount by clicking **Decrease** button.
* If the unwanted product has been inserted, the user can delete the product by referring its id by clicking **Delete** button. In order to do it, the user will list the product to see product id. **Each product even the same name has different id.** 
* In order to see inventroy, the user should click **List** button.
* Threshold is a given number that if the user clicks **Show Below**, the all products which are less than the threshold value, will be listed in the screen.
* **Clear** button clears the screen.  

