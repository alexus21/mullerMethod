import pandas as pd

class ShowInfo:
    def __init__(self, df):
        self._df = df

    def showIterationsInfo(self):
        print(self._df)