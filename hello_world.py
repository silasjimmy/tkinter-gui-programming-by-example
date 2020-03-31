#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 07:00:53 2020

@author: silasjimmy
"""

import tkinter as tk

class HelloWorld(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Hello TKinter!')
        
        label = tk.Label(self, text='Hello World!')
        label.pack(fill=tk.BOTH, expand=1, padx=100, pady=50)
     
if __name__=='__main__':
    window = HelloWorld()
    window.mainloop()