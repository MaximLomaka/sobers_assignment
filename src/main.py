from data_prep import Bank1, Bank2, Bank3
from process import Process

if __name__ == '__main__':
    columns_to_drop = ['euro', 'cents']
    dfs = (
        Bank1('data/bank1.csv'),
        Bank2('data/bank2.csv'),
        Bank3('data/bank3.csv')
    )
    process = Process(dfs, columns_to_drop)
    process.write_to_file('result')

