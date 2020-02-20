#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:40:52 2020

@author: acfm
"""
import re
from Lib import Lib
from Book import Book
import numpy
from utils import read

a_path = 'inputs/a_example.txt'
b_path = 'inputs/b_read_on.txt'
c_path = 'inputs/c_incunabula.txt'
d_path = 'inputs/d_tough_choices.txt'
e_path = 'inputs/e_so_many_books.txt'
f_path = 'inputs/f_libraries_of_the_world.txt'
#num_books, num_libs, num_days, book_scores, libraries, booksets_for_libs = read(a_path)
num_books, num_libs, num_days, book_scores, libraries, booksets_for_libs = read(b_path)

output_list_of_libs = []

books = []
for i, book in enumerate(book_scores):
    books.append(Book(i, book))

libs = []
for i, lib in enumerate(libraries):
    libs.append(Lib(i, booksets_for_libs[i], lib[1], lib[2], books))

current_day = 0
while num_days > current_day:
    highest_score_yet = 0;
    highest_i = 0
    value_is_updated = 0
    for i, lib in enumerate(libs):
        print("This is lib nb " + str(i) +" with books: ")
        print(lib.bookSet)
        if lib.is_used == 0:
            print("This lib is un used i="+str(i))
            temp_score = lib.get_score_from_lib(num_days-current_day)
            if temp_score >= highest_score_yet:
                highest_i = i
                highest_score_yet= temp_score
                value_is_updated=1

    if value_is_updated:
        output_list_of_libs.append(highest_i)

        libs[highest_i].is_used=1
        current_day += libs[highest_i].signUp
    else:
        print("breaking")
        break
    
print("Time to print some books")

#print(f"Time to output results\nNumber of libs: {output_list_of_libs}")
#print(f"First lib: {}")
#print(f"First lib: {}")
#'\nfirst lib, number of books\nfirst libs books\n....\nlast lib, number of books\nlast libs books\n")
print("Number of books" +str(len(output_list_of_libs)))
for i in output_list_of_libs:
    print("This lib is used: " + str(i))
    print("These books" + str(libs[i].UsedBooks))

#derp



