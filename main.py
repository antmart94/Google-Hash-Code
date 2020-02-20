#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:40:52 2020

@author: acfm
"""
import pandas as pd
import re
import Lib
import Book
import numpy
from utils import read

a_path = 'inputs/a_example.txt'
b_path = 'inputs/b_read_on.txt'
c_path = 'inputs/c_incunabula.txt'
d_path = 'inputs/d_tough_choices.txt'
e_path = 'inputs/e_so_many_books.txt'
f_path = 'inputs/f_libraries_of_the_world.txt'
num_books, num_libs, num_days, book_scores, libraries, booksets_for_libs = read(a_path)

current_days = 0
while num_days > current_day:
    #loop each lib in lib list
        #call function to calculate how much score this lib can generate on given days (days-current_day)
        #if highest score yet, store the index of lib
    #the index of the lib with highest score is added to order list
    #purge books from other libs 
    #set lib to used
    current_day += 1 #todo lib.days_toscan


