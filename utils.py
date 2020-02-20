#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 19:09:38 2020

@author: acfm
"""

#a_path = 'inputs/a_example.txt'
#b_path = 'inputs/b_read_on.txt'
#c_path = 'inputs/c_incunabula.txt'
#d_path = 'inputs/d_tough_choices.txt'
#e_path = 'inputs/e_so_many_books.txt'
#f_path = 'inputs/f_libraries_of_the_world.txt'

def convert_to_int(line):
    return [int(i) for i in line.rstrip().split(' ')]

def read(path):
    with open(path, 'r') as f:
        num_books, num_libs, num_days = convert_to_int(f.readline()) # num_books, num_libs, num_days 
        # B section
        scores = convert_to_int(f.readline()) # Individual book scores
        # L section
        libs = []
        booksets_in_lib = []
        while True:
            line1 = f.readline()
            line2 = f.readline()
            if not line1 or not line2: break
            
            libs.append(convert_to_int(line1)) # num_books in library, signup time, num book shipped 
            booksets_in_lib.append(convert_to_int(line2))
            
    return num_books, num_libs, num_days, scores, libs, booksets_in_lib