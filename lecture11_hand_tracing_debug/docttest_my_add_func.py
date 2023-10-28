import os

os.chdir('lecture8\my_add_func.py')

import doctest
doctest.testfile('my_add_func.py')

# import doctest
# doctest.testfile('/path/to/my_add_func.py')