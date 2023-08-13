import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'root', db = 'dex')
mycursor = mydb.cursor()

mycursor.execute('create table items(name varchar(300), type varchar(20), price int, img varchar(300))')
mycursor.execute('create table cart(name varchar(100), price int)')
mycursor.execute('create table lastpurch(name varchar(100) primary key, price int, time varchar(50), date date)')
mydb.commit()

#---------------------------WOMEN------------------
f = open('data\WomenBottomwear.txt', 'r',)
lines = f.readlines()
for i in lines:
    j = i.split()
    print(j)
    mycursor.execute('insert into items values("' + j[2] + '","women_bottom",' + j[0] + ',"' + j[1]+'");')
mydb.commit()
f.close()

f = open('data\WomenTopwear.txt', 'r',)
lines = f.readlines()
for i in lines:
    j = i.split()
    print(j)
    mycursor.execute('insert into items values("' + j[2] + '","women_top",' + j[0] + ',"' + j[1]+'");')
mydb.commit()
f.close()

f = open('data\WomenFootwear.txt', 'r',)
lines = f.readlines()
for i in lines:
    j = i.split()
    print(j)
    mycursor.execute('insert into items values("' + j[2] + '","women_foot",' + j[0] + ',"' + j[1]+'");')
mydb.commit()
f.close()

#---------------------------MEN------------------
f = open('data\MenBottomwear.txt', 'r',)
lines = f.readlines()
for i in lines:
    j = i.split()
    print(j)
    mycursor.execute('insert into items values("' + j[2] + '","men_bottom",' + j[0] + ',"' + j[1]+'");')
mydb.commit()
f.close()

f = open('data\MenTopwear.txt', 'r',)
lines = f.readlines()
for i in lines:
    j = i.split()
    print(j)
    mycursor.execute('insert into items values("' + j[2] + '","men_top",' + j[0] + ',"' + j[1]+'");')
mydb.commit()
f.close()

f = open('data\MenFootwear.txt', 'r',)
lines = f.readlines()
for i in lines:
    j = i.split()
    print(j)
    mycursor.execute('insert into items values("' + j[2] + '","men_foot",' + j[0] + ',"' + j[1]+'");')
mydb.commit()
f.close()
#--------------------------------KIDS-----------------------

f = open('data\KidsBottomwear.txt', 'r',)
lines = f.readlines()
for i in lines:
    j = i.split()
    print(j)
    mycursor.execute('insert into items values("' + j[2] + '","kids_bottom",' + j[0] + ',"' + j[1]+'");')
mydb.commit()
f.close()

f = open('data\KidsTopwear.txt', 'r',)
lines = f.readlines()
for i in lines:
    j = i.split()
    print(j)
    mycursor.execute('insert into items values("' + j[2] + '","kids_top",' + j[0] + ',"' + j[1]+'");')
mydb.commit()
f.close()

f = open('data\KidsFootwear.txt', 'r',)
lines = f.readlines()
for i in lines:
    j = i.split()
    print(j)
    mycursor.execute('insert into items values("' + j[2] + '","kids_foot",' + j[0] + ',"' + j[1]+'");')
mydb.commit()
f.close()


