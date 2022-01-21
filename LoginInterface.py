#Login Interface using Tkinter
from tkinter import *
from logpg import logf



#-------------------------Pages--------------------------
'''
choicepg: offers choices to register or login
logpg: the final login page
mainpg: the main home page which allows user to shop,
        contact support and go to cart
contactpg: page where user can go to for getting support
shoppg: page where user makes their choices
clothespg: page which shows the user the clothes available
checkoutpg: page which shows user the final billings
typage: final screen where user exits program
'''
#---------------------------------------------------------


#Tk window started
choicepg = Tk()
choicepg.geometry('500x300')
choicepg.resizable(True, True)
choicepg.title('EasyShop')
choicepg['background'] = '#5ee682'


#Functions for choicepg
def exit():
    #exits program
    choicepg.destroy()

    
def regist():
    #To take string with login ids and passwords
    readfile = open('logpw.txt','r')
    read = ''.join(readfile.readlines())
    readfile.close()
    
    file = open('logpw.txt','a+')
    if Login.get() not in read:
        #To check if username in file
        file.write(Login.get()+ ' ' + PW.get() + '\n')
        file.close()
        choicepg.destroy()
        logf()
    else:
        result['text'] = 'That Username is already present.'

def logfunc():
    choicepg.destroy()
    logf()


welc = Label(choicepg, text = "Welcome to EasyShop's Shopping Interface!", font = ('Century Gothic',15), background = '#5ee682') 
img = PhotoImage(file = "logo.png")
canvas = Label(choicepg, image = img)

#Entry boxes for credentials
Login = Entry(choicepg, width = 50)
Login.insert(0, 'Username')
PW = Entry(choicepg, width = 50)
PW.insert(0, 'Password')


regb = Button(choicepg, text ="Register", command = regist, width = 10)
result = Label(choicepg, background = '#5ee682') #Label used to tell user username already exists
ortext = Label(choicepg, text = "OR", font = ('Century Gothic',15), background = '#5ee682')
logb = Button(choicepg, text ="Login", command = logfunc, width = 10)
quitb = Button(choicepg, text ="Exit", command = exit, width = 10)

#Geometry Managers used to place all the Tk Widgets
welc.pack(anchor = 'center')
canvas.pack(pady = 20, anchor = 'center')

Login.pack(anchor = 'center')
PW.pack(anchor = 'center')

result.pack(pady = 5, anchor = 'center')
regb.pack(anchor = 'center')
ortext.pack(pady = 5, anchor = 'center')
logb.pack(anchor = 'center')
quitb.place(relx = 0.99, rely = 0.99, anchor = 'se')

mainloop()

