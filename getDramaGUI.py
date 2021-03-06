# -*- coding: utf-8 -*-
import tkinter.messagebox
from tkinter import *
import getMeiJuUrl
class GetDramaGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("get America TV GUI")
        
        frame = Frame(self.window)
        frame.pack()
        
        self.name = StringVar()
        self.season = StringVar()

        
        Label(frame, text = 'enter drama name like:纸牌屋').grid(row = 1, column = 1)
        Entry(frame, textvariable = self.name).grid(row = 1, column = 2)
        Label(frame, text = 'enter season like:第一季').grid(row = 2, column = 1)
        Entry(frame, textvariable = self.season).grid(row = 2, column = 2)
        
        Button(frame, text = 'submit', command = self.processSubmit).grid(row = 3, column = 2)

        self.window.mainloop()
    
    def processSubmit(self):
        if self.isNameOrSeasonNone():
            tkinter.messagebox.showwarning('Warning', 'drama name and season is default\n纸牌屋第一季')
            getMeiJuUrl.process_Info('纸牌屋', '第一季')
        else:
            tkinter.messagebox.showinfo("process", "submit success")
            getMeiJuUrl.process_Info(self.name.get(), self.season.get())
        tkinter.messagebox.showinfo('status', 'search done\nresult is in current dictionary')
        self.window.destroy()
    def isNameOrSeasonNone(self):
        return True if self.name.get() == '' or self.season.get() == '' else FALSE

def main():
    GetDramaGUI()
        
if __name__ == '__main__':
    main()
