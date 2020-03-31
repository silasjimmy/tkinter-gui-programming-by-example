#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 07:00:53 2020

@author: silasjimmy
"""

import tkinter as tk
import tkinter.messagebox as msgbox

class HelloWorld(tk.Tk): # Subclassing Tkinter's main window widget— Tk
    def __init__(self):
        super().__init__()
        self.title('Hello TKinter!')
        
        label = tk.Label(self, text='Hello World!') # Widget
        label.pack(fill=tk.BOTH, expand=1, padx=100, pady=50)
        
class ChooseOne(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Choose One')
        
        self.label = tk.Label(self, text='Choose One')
        self.label.pack(fill=tk.BOTH, expand=True, padx=100, pady=50)
        
        hello_button = tk.Button(self, text="Say Hello", command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))
        goodbye_button = tk.Button(self, text="Say Goodbye", command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))
        
    def say_hello(self):
        self.label.configure(text="Hello World!")
    
    def say_goodbye(self):
        self.label.configure(text="Goodbye! \n (Closing in 2 seconds)")
        self.after(2000, self.destroy)
        
class Variables(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Choose One')
        
        self.text_lbl = tk.StringVar()
        self.text_lbl.set('Choose One')
        
        self.label = tk.Label(self, textvar=self.text_lbl)
        self.label.pack(fill=tk.BOTH, expand=True, padx=100, pady=50)
        
        hello_button = tk.Button(self, text="Say Hello", command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))
        goodbye_button = tk.Button(self, text="Say Goodbye", command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))
        
    def say_hello(self):
        self.text_lbl.set('Hello World!')
    
    def say_goodbye(self):
        self.text_lbl.set("Goodbye! \n (Closing in 2 seconds)")
        self.after(2000, self.destroy)
        
class MessageBox(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Choose One')
        
        self.text_lbl = tk.StringVar()
        self.text_lbl.set('Choose One')
        
        self.label = tk.Label(self, textvar=self.text_lbl)
        self.label.pack(fill=tk.BOTH, expand=True, padx=100, pady=50)
        
        hello_button = tk.Button(self, text="Say Hello", command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))
        goodbye_button = tk.Button(self, text="Say Goodbye", command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))
        
    def say_hello(self):
        msgbox.showinfo(title='Hello', message='Hello World!')
    
    def say_goodbye(self):
        self.text_lbl.set("Closing in 2 seconds")
        msgbox.showinfo('Goodbye', 'Goodbye! Its been fun!')
        self.after(2000, self.destroy)
     
if __name__=='__main__':
    hello_world = HelloWorld()
    hello_world.mainloop()
#    choose_one = ChooseOne()
#    choose_one.mainloop()
#    variables = Variables()
#    variables.mainloop()
#    messagebox = MessageBox()
#    messagebox.mainloop()