OK_FORMAT = True
test = {   'name': 'q1_1',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> # Check your column labels and spelling;\n>>> b_pop.labels == ('time', 'population_total')\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Times should range from 1970 through 2015;\n>>> all(b_pop.sort("time").column("time") == np.arange(1970, 2016))\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
