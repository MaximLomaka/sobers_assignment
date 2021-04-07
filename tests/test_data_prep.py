from unittest.mock import patch
import pandas as pd
import src.data_prep as dp


@patch('src.data_prep.pd.read_csv')
def test_bank3_prep(mock_read_csv):
    mock_read_csv.return_value = pd.DataFrame({'date_readable': [2015, 2016],
                                               'type': ['add', 'remove'],
                                               'euro': [100, 343],
                                               'cents': [5, 7],
                                               'from': [124, 432],
                                               'to': [123, 321]
                                               })

    expected_df = pd.DataFrame({'date': [2015, 2016],
                                'transaction': ['add', 'remove'],
                                'euro': [100, 343],
                                'cents': [5, 7],
                                'from': [124, 432],
                                'to': [123, 321],
                                'amounts': [100.5, 343.7]
                                })
    bank3 = dp.Bank3('')
    result = bank3.get_df()
    assert expected_df.equals(result.astype({'amounts': 'float64'}))
