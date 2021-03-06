

import re
import numpy as np

class Lib:

    def __init__(self,  libId, bookSet,  signUp,  scan, all_books):
        self.libId = libId
        self.bookSet = bookSet
        self.signUp = signUp
        self.scan = scan
        self.is_used = 0
        self.UsedBooks = []
        self.all_books = all_books
        #self.books = [b for b in books if b.bid in bookSet]

    def remove_from_book_set(self, book_id_to_remove):
        if book_id_to_remove in self.bookSet:
            self.bookSet.remove(book_id_to_remove)
    
    def get_highest_book(self):
        #Todo returns book with highest score
        current_score = 0
        current_hs_i = 0
        valid = 0
        for b in self.bookSet:
            if b not in self.UsedBooks:
                if self.all_books[b].score > current_score:
                    valid =1
                    current_score = self.all_books[b].score
                    current_hs_i = b
        return valid, self.all_books[current_hs_i]


    def get_score_from_lib(self, days_left):
        days_left -= self.signUp
        score = 0
        self.UsedBooks = []
        for day in range(days_left):
            for i in range(self.scan):
                valid, temp_book = self.get_highest_book()
                if valid == 0:
                    break
                self.UsedBooks.append(temp_book.bId)
                score += temp_book.score
        return score

                




