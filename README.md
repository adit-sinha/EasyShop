# EasyShop
Welcome to the Tkinter Shopping Simplifier! This program fetches images from urls as per choices of clothes made by you and displays them in a Tk() window!

Made by [@Adit Sinha](https://github.com/adit-sinha), [@Ekhnoor Grover](https://github.com/Noor-G), [@Dhruv Rawal](https://github.com/M3-MZ) and Ahaan Bohra.

## Accolades
- Silico Battles (2022-23): 2nd Prize (Hackathon)
Note: This project, which previously only used data file handling, was merged with a separate project made at the hackathon which used database management.

## Project Overview
EasyShop is a shopping interface we created for people who want to buy specific cloth wear and to provide shopkeepers with a shopping model that requires minimal labour. Such models are now in use in some enterprises such as Decathlon. 

They start by logging into the interface, if it is their first time using it then they must register. When a user registers, an SQL table based on their unique username is created to store their cart. Returning users can directly access their cart and add more cloth articles to their cart. However, if the cart is empty, the user is requested to shop first. If the user has any queries there is a
contact support page in which they can ask their query via Whatsapp or Mail. We provide certain choices through which they can get to what they want faster.

Using the ‘Tkinter’ module and ‘PIL’ module we managed to display images of the clothing options for the user. They can choose the clothes they would like to add to the cart. At the checkout page they can view the final summary and then checkout. We also allow the shopkeeper or administrator to view the last purchase made by a user using a MySQL table. It also details them on the date and time it was issued.

NOTE: All image links in the .txt files and the 'fashion carnival' image belong to https://www.myntra.com/. They are being used in our program for educational purposes only. Images used for buttons belong to http://shutterstock.com/. Other relevant images belong to their creators and have not been created by any party who programmed this project. 


## Python Concepts Used
1. Lists:
2. User Defined Functions:
3. Dictionaries: 
4. File Handling:
5. Importing a function from a file:
6. In built functions:
7. ‘Tkinter’ module:
8. ‘PIL’ module:
9. ‘urllib’ module:
10. ‘webbrowser’ module
11. ‘datetime’ module
12. MySQL
13. MySQL-Python connectivity

We have utilized several python concepts and modules to make this project. 

- The project utilizes basic python data structures such as lists and dictionaries to store organized data. It also uses these to organize the data we receive from the MySQL table.
- The code is also well organized with appropriate documentation. All the user created functions and variables featured also have appropriate names for the viewer/programmer's sake.
- We also made use of file handling, using it here so that we can combine the different aspects of the project into one as well as for the login interface to run smoothly.
- The ‘Tkinter’ module is a concept which we weren’t taught in school. It is a module to make a relatively simple general user interface, and we applied it to every part of our project to enhance the customer experience.
- We also experimented with the PIL and urllib module in python in order to get the image from the link and portray it in the Tk window.
- We’ve also used MySQL to create ‘cart’ and‘items’ tables that are used to store the user’s temporary cart and the web store’s current stock. The temporary cart maintains the user’s previous session and only gets updated/truncated when the user proceeds to pay.
- We’ve also added a ‘lastpurch’ table using MySQL which is used to store details about the user’s last purchase. It includes the name (primary key), price, date and time as its parameters. To record the date and time, we’ve used the ‘datetime’ module. 

## Requirements 

All the following steps must be completed to run the project:

1. You must have pip installed.
2. The program must be downloaded from the link provided as a zipped folder (.zip) and extracted.
3. You must have Tkinter, pillow, urllib3 and mysql connector modules installed using the following commands:

```python 
$pip install tk
$pip install pillow
$pip install urllib3
$pip install pip install mysql-connector-python
```

4. **Create a Database 'dex' and run 'sqlLoader.py' to fill the data table for clothes.**
5. **Run 'Login Interface.py' in the folder of the same name to start the program.**
6. All files (python and data) and images must be in the same directories as in the link to the project.
7. The password and username for your MySQL client must be ‘root’. If this is not the case, this must be edited in the python programs. 

## Output Screens
Screen 1: First Screen, allows user to register a new user or go to Login page

![Screen 1 Image](/mdscreens/screen1.png)

Screen 2: Screen if user enters a username already present

![Screen 2 Image](/mdscreens/screen2.png)

Screen 3: Login Page; user logs into their EasyShop account

![Screen 3 Image](/mdscreens/screen3.png)

Screen 4: Screen if user’s login credentials are incorrect

![Screen 4 Image](/mdscreens/screen4.png)

Screen 5:  If the login credentials are correct, the user is taken to the Home Page which allows user to contact support, continue shopping or proceed to cart.

![Screen 5 Image](/mdscreens/screen5.png)

Screen 6: Screen if user tries to proceed to cart without purchasing anything or having anything in the cart:

![Screen 6 Image](/mdscreens/screen6.png)

If the cart isn't empty, it displays the content put in the cart previously:
![Screen 6.1 Image](/mdscreens/screen6.1.png)

Screen 7: Contact Page (accessed if ‘Contact Support’ button pressed

![Screen 7 Image](/mdscreens/screen7.png) 

Pressing ‘Back’ button takes them to screen 5

Screen 8 and 9: Screen to make choices for shopping

![Screen 8 Image](/mdscreens/screen8.png)

![Screen 9 Image](/mdscreens/screen9.png)

Screen 10: Screen if 'Continue' pressed without making all 3 choices

![Screen 10 Image](/mdscreens/screen10.png)

Screen 11: When the “Continue” button is pressed, it takes the user to the Shopping Page:  

![Screen 11 Image](/mdscreens/screen11.png)

Screen 12 and 13: Shopping Page screen if list of clothes available finished

![Screen 12 Image](/mdscreens/screen12.png) 

![Screen 13 Image](/mdscreens/screen13.png)

Screen 14: Shopping Page if item added to cart (thrice)

![Screen 14 Image](/mdscreens/screen14.png)

> After the “Add to Cart” button is pressed, the clothing piece is added to the Cart SQL table. This table would contain information regarding the name, price, etc. of the clothing 
> 
> When ‘Return to home’ button is pressed, goes back to Screen 5
> When ‘Proceed to Cart’ button is pressed, goes to Screen 15

Screen 15: Checkout Page 

![Screen 15 Image](/mdscreens/screen15.png)

> Pressing ‘Shop More’ goes to screen 5
> Pressing ‘Proceed to pay’ goes to screen 17

Moreover, the ‘lastpurch’ table does the following: 
If the user has never made a purchase before, the latest record is inserted into it:

![Screen 15.1](/mdscreens/screen15.1.png)

However, if the user has made a purchase before, the latest record is
updated accordingly (The user 'Adit' is updated): 

![Screen 15.2](/mdscreens/screen15.2.png)

Screen 16: Checkout Page after a user buys another item after making choice

![Screen 16 Image](/mdscreens/screen16.png)

Screen 17: Final Screen; Thank you Page

![Screen 17 Image](/mdscreens/screen17.png)

## Limitations and Future Scope
The future scope of this project is immense. There are many features that we have not yet added, due to reasons such as lack of time, inexperience in programming or lack of resources. Below we have listed down the limitations faced by us while doing this project along with its potential in the future: -

1. We could add a delete button to the cart for users to delete items that they do not want to purchase. This could be easily done with SQL using a “delete’ query.
2. Web Scraping and parsing could potentially be a very efficient and automated way to update our shop with newer clothes. We were unable to do this as we did not how to utilise modules like ‘BeautifulSoup’ and the ‘requests’ module properly.
3. Another idea that we are planning to implement is a price estimate. Currently in our project we have rigid price ranges which do not have a lot of variability; however we are planning to implement an input to take the price and offer clothes around that price range to the user.
4. Storing the user’s information on a web server would also be a beneficial alteration since it would allow the stock of the store to be updated in real time. This would also make it easier for our project to be set up in offline and online stores.
5. We would like to add an update feature, which gives the user an option to change their username or password as it is currently not feasible due to our use of data file handling. 

## Bibliography 
1. https://www.geeksforgeeks.org/python-gui-tkinter/
2. https://www.w3schools.in/python-tutorial/guiprogramming/
3. https://smallbusiness.chron.com/
4. https://linuxhint.com/
5. https://docs.python.org/3/library/urllib.html
6. https://www.geeksforgeeks.org/python-urllib-module/
7. https://www.geeksforgeeks.org/python-launch-a-webbrowser-using-webbrowser-module/
8. https://www.shutterstock.com/
9. https://www.myntra.com/
10. https://www.geeksforgeeks.org/python-datetimemodule/ 



Thank you for checking out our project! We really appreciate your time.
