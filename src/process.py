import pandas as pd


class Process:
    # columns to drop in final df
    def __init__(self, dfs, columns_to_drop):
        self.dfs = dfs
        self.columns_to_drop = columns_to_drop

    @property
    def merged_df(self):

        df = pd.concat([df.get_df() for df in self.dfs]).drop(self.columns_to_drop, 1)
        df['date'] = pd.to_datetime(df['date'])
        return df

    def write_to_file(self, file_name, file_type='csv'):
        """ Writing final df to the file. If we need additional file types
            we can remove error and add required type
        """
        df = self.merged_df
        if file_type == 'csv':
            df.to_csv(file_name, index=False)
        else:
            raise AttributeError('File type can be only csv ')
