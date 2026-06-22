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
input1=StringVar()


#blueprint for grid/list view toggles and orderings
is_on = False

def toggle():
     global is_on
     is_on = not is_on
     if is_on:
          listView.config(bg='red')
          #conn = sqlite3.connect('manga.db')
          #c=conn.cursor()
          #c.execute("SELECT status FROM Status")
          #rows= c.fetchall()
          #for row in rows :
          #     print(row)
          #conn.close()
     else:
          listView.config(bg='green')

listView = Button(root,bg = 'green' ,command=toggle)
listView.pack()

class My_widget(Frame):

     def __init__(self, parent, label_text, button_text):
          super().__init__(master = parent)

          #grid
          self.rowconfigure(0,weight=1)
          self.columnconfigure((0,1),weight=1, uniform='z')

          #buttons
          self.label = Label(self, text=label_text)
          self.label.grid(row=0, column=0)
          Button(self, text=button_text,command=self.input,fg="white",bg="red").grid(row=0, column=1)
          #inputbox example
          Entry(self,textvariable=input1).grid(row=0, column=2)
          self.pack()

     def input(self) :
          entryInput = input1.get()
          self.label.config(text=entryInput)
          #print(entryInput)

My_widget(root,"Label 1","Button 1")

root.mainloop()