from collections import OrderedDict
import src.data_prep as dp


def test_bank3_prep():

    input_data = dp.Bank3('data/bank3.csv')

    result = input_data.get_prep_df()
    expected_result = [OrderedDict([('euro', '5'), ('cents', '7'), ('to', '182'),
                                    ('from', '198'), ('amounts', '5.7'), ('date', '05.10.2019'),
                                    ('transaction', 'remove')]),
                       OrderedDict([('euro', '1060'), ('cents', '8'), ('to', '198'), ('from', '188'),
                                    ('amounts', '1060.8'), ('date', '06.10.2019'), ('transaction', 'add')])]

    assert expected_result == result
