import abc
import pandas as pd


class DfPrep(abc.ABC):
    """
this class using for the basic interface. 
If you need to process a new file you should inherit from this class and realize abstract methods 
    """

    def __init__(self, df):
        self.df = pd.read_csv(df)

    @abc.abstractmethod
    def get_df(self):
        pass

    @abc.abstractmethod
    def _prep(self):
        pass


class Bank1(DfPrep):
    def _prep(self):
        self.df = self.df.rename({'timestamp': 'date', 'type': 'transaction', 'amount': 'amounts'}, axis=1)

    def get_df(self):
        self._prep()
        return self.df


class Bank2(DfPrep):

    def get_df(self):
        self._prep()
        return self.df

    def _prep(self):
        pass


class Bank3(DfPrep):
    def _prep(self):
        self.df = self.df.rename({'date_readable': 'date', 'type': 'transaction'}, axis=1)
        self.df = self.df.assign(amounts=self.df['euro'].astype(str) + '.' + self.df['cents'].astype(str))

    def get_df(self):
        self._prep()
        return self.df
