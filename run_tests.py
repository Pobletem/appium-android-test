import unittest

loader = unittest.TestLoader()
# looks for test_*.py files in the tests directory
suite = loader.discover('tests')

# run the test scripts shows the output in the terminal
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)

