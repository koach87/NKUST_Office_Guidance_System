# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:21:09 2020

@author: user
"""


from tkinter import *

def title(title):
    window.title(title)
    
def entry():
    pass

window = Tk()
window.geometry("300x300")

key_in_frame = Frame(window)
student_ID = Entry(key_in_frame)
student_ID.pack(side = LEFT)
test = Button(window)
test.pack()

key_in_frame.pack()



selection_frame = Frame(window)    




window.mainloop()