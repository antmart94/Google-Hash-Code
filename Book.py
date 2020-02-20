

import pandas as pd
import re


class Book:
    int id
    int score

    def _init_(self, id, score):
        self.id = id
        self.score = score