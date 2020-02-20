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

libs = []
for i, lib in enumerate(libraries):
    libs.append(Lib(i, lib[0], lib[1], lib[2]))
    
books = []
for i, book in enumerate(book_scores):
    books.append(Book(i, book_scores)
    
current_days = 0
while num_days > current_day:
    highest_score_yet = 0;
    highest_i = 0
    for i, lib in enumerte(libs):
        if lib.is_used == 0:
            temp_scores = get_score_from_lib(lib, num_days-current_day)
            if temp_score >= highest_score_yet:
                highest_i = i
                highest_score_yet= temp_score

    output_list_of_libs.append(highest_i)

    #TODO here purge books from other libs
    libs[highest_i].is_used=1
    current_day += libs[highest_i].signUp


