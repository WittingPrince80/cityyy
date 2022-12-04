# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 12:07:18 2022

@author: Aryan
"""



from tkinter import *
import random

root=Tk()
root.title("unlucky ways to die in minecraft")
root.geometry("500x500")

enter_city = Entry(root)
enter_city.place(relx= 0.5,rely = 0.2, anchor = CENTER)

city_list = Label(root)
random_number_label = Label(root)
unlucky_death = Label(root)

list1 = []

def addcity():
    city = enter_city.get()
    list1.append(city)
    city_list["text"] = "Your citys : " + str(list1)

def random_number():
    length = len(list1)
    random_no = random.randint(0, length-1)
    random_number_label["text"] = str(random_no)
    generated_random_number = list1[random_no]
    unlucky_death["text"] = "Random City: " + str(generated_random_number)
    btn1 = Button(root, text="Add City", command= addcity)  
btn1.place(relx= 0.5,rely = 0.3, anchor = CENTER )
 
city_list.place(relx= 0.5,rely = 0.4, anchor = CENTER )

btn1 = Button(root, text="Randomize ", command = random_number)
btn1.place(relx= 0.5,rely = 0.5, anchor = CENTER )

random_number_label.place(relx= 0.5,rely = 0.6, anchor = CENTER )
unlucky_death.place(relx= 0.5,rely = 0.7, anchor = CENTER )

root.mainloop()