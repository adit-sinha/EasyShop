#Login Page Function
from tkinter import *
from mainpg import mainf
def logf():
    file = open('logpw.txt','r')
    logpwdic = {}
    for line in file:
        elemlist = line.split()
        if len(elemlist)>1:
            logpwdic.update({elemlist[0]:elemlist[1]})
    file.close()
    #Login Page
    logpg = Tk()
    logpg.geometry('500x250')
    logpg.resizable(True, True)
    logpg.title('Login to EasyShop!')
    logpg['background'] = '#33f5eb'
    
    def mainent():
        if Login.get() in logpwdic:
            if PW.get() == list(logpwdic.values())[list(logpwdic.keys()).index(Login.get())]:
                logpg.destroy()
                mainf()
            else:
                Result['text'] = 'Try Again!'
                
        else:
            Result['text'] = 'Try Again!'
    #Buttons        
    welc = Label(logpg, text = "Please login to your EasyShop Account:", font = ('Century Gothic',15), background = '#33f5eb')
    img = PhotoImage(file = "logo.png")
    canvas2 = Label(logpg, image = img)

    Login = Entry(logpg, width = 50)
    Login.insert(0, 'Username')
    PW = Entry(logpg, width = 50)
    PW.insert(0, 'Password')

    logb = Button(logpg, text ="Login", command = mainent, width = 10)

    quitb = Button(logpg, text ="Exit", command = exit, width = 10)
    Result = Label(logpg, background = '#33f5eb')

    #Geometry Managers          
    welc.pack(anchor = 'center')
    canvas2.pack(pady = 20, anchor = 'center')
    
    Login.pack(anchor = 'center')
    PW.pack(anchor = 'center')

    logb.pack(pady = 10, anchor = 'center')
    Result.pack(anchor = 'center')

    quitb.place(relx = 0.99, rely = 0.99, anchor = 'se')
    mainloop()
