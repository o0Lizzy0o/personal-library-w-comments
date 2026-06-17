from tkinter import *
import sqlite3

#connect sqlite
conn = sqlite3.connect('manga.db')
c=conn.cursor()
#print data
c.execute("SELECT * FROM manga")
rows= c.fetchall()
for row in rows :
     print(row)

conn.close()

# base widget

root = Tk()
root.title('test name')
root.geometry('700x450')

class My_widget(Frame):
     def __init__(self, parent, label_text, button_text):
          super().__init__(master = parent)

          #grid
          self.rowconfigure(0,weight=1)
          self.columnconfigure((0,1),weight=1, uniform='z')

          #buttons
          Label(self,text=label_text).grid(row=0,column=0)
          Button(self, text=button_text).grid(row=0, column=1)
          self.pack()

My_widget(root,"Label 1","Button 1")

root.mainloop()