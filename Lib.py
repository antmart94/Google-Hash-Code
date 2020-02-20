

import pandas as pd
import re
import numpy as np

class Lib:

    def __init__(self,  libId, bookSet,  signUp,  scan, all_books):
        self.libId = libId
        self.bookSet = bookSet
        self.signUp = signUp
        self.scan = scan
        self.is_used = 0
        #self.books = [b for b in books if b.bid in bookSet]

    def remove_from_book_set(self, book_id_to_remove):
        if book_id_to_remove in self.bookSet:
            self.bookSet.remove(book_id_to_remove)

    def get_score_from_lib(self):
        return 5