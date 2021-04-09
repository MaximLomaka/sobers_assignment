import abc
import csv
import datetime


class DfPrep:
    """
this class using for the basic interface. 
If you need to process a new file you should inherit from this class and realize abstract methods 
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.date_format = '%d-%m-%Y'

    @abc.abstractmethod
    def get_prep_df(self):
        pass

    @staticmethod
    def dict_rename_key(iterable, old_key, new_key):
        """
        dict_rename_key method
        Args:
            iterable (dict)
            old_key (string)
            new_key (string)
        Returns:
            dict
        """
        if isinstance(iterable, dict):
            for key in list(iterable.keys()):
                if key == old_key:
                    iterable[new_key] = iterable.pop(key)
        return iterable


class Bank1(DfPrep):

    def get_prep_df(self):
        row_list = []
        renamed_columns = {'timestamp': 'date', 'type': 'transaction', 'amount': 'amounts'}
        with open(self.file_path, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                for old_name, new_name in renamed_columns.items():
                    self.dict_rename_key(row, old_name, new_name)
                row['date'] = datetime.datetime.strptime(row['date'], '%b %d %Y').strftime(self.date_format)

                row_list.append(row)
        return row_list


class Bank2(DfPrep):

    def get_prep_df(self):
        row_list = []
        with open(self.file_path, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                row_list.append(row)
        return row_list


class Bank3(DfPrep):
    def get_prep_df(self):
        renamed_columns = {'date_readable': 'date', 'type': 'transaction'}
        row_list = []
        with open(self.file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['amounts'] = f"{row['euro']}.{row['cents']}"
                for old_name, new_name in renamed_columns.items():
                    self.dict_rename_key(row, old_name, new_name)
                row['date'] = datetime.datetime.strptime(row['date'], '%d %b %Y').strftime('%d.%m.%Y')
                row_list.append(row)
        return row_list
