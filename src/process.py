import csv


class Process:
    def __init__(self, files, columns_to_drop):
        self.files = files
        self.columns_to_drop = columns_to_drop
        self.required_columns = ['from', 'to', 'date', 'transaction', 'amounts']

    @property
    def row_list(self):
        return [rows.get_prep_df() for rows in self.files]

    @staticmethod
    def _remove_columns(row_list):
        removed_columns = ['date_readable', 'euro', 'cents']

        for row in row_list:
            for removed_column in removed_columns:
                if removed_column in row:
                    row.pop(removed_column)
        return row_list

    def write_to_file(self, file_name, file_type='csv'):
        """ Writing final df to the file. If we need additional file types
            we can remove error and add required type
        """

        with open(f'{file_name}.{file_type}', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.required_columns)
            writer.writeheader()
            for df in self.row_list:
                self._remove_columns(df)
                for row in df:
                    writer.writerow(row)
