OK_FORMAT = True
test = {   'name': 'q2_5',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> # Check your column labels and spelling;\n>>> largest.labels == ('name', 'poverty_total')\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> # India is the country with the largest number of people living;\n>>> # in extreme poverty.;\n>>> largest.column(0).item(0) == 'India'\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> # The table should contain exactly 10 rows.;\n>>> largest.num_rows == 10\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
