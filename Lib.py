

import pandas as pd
import re

class Lib:

    def __init__(self,  libId, bookSet,  signUp,  scan):
            self.libId = libId
            self.bookSet = bookSet
            self.signUp = signUp
            self.scan = scan
            self.is_used = 0

    def remove_from_book_set(book_id_to_remove):
        if book_id_to_remove in bookSet:
            bookSet.remove(book_id_to_remove)

