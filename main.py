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

output_list_of_libs[]

current_days = 0
while num_days > current_day:
    highest_score_yet = 0;
    highest_i = 0
    for i, lib in enumerte(libs):
        temp_scores = get_score_from_lib(lib, num_days-current_day)
        if temp_score >= highest_score_yet:
            highest_i = i
            highest_score_yet= temp_score

    output_list_of_libs.append(i)
    #purge books from other libs 
    #set lib to used
    current_day += 1 #todo lib.days_toscan


