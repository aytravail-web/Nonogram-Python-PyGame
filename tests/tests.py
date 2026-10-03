import unittest
import sys

sys.path.insert(0, "..")

# Inclusion des tests à effectuer

from TestPosition import TestPosition
from TestCellule import TestCellule
from TestImage import TestImage
from TestBloc import TestBloc
from TestNonogram import TestNonogram
from TestSuggestion import TestSuggestion

if __name__ == '__main__':
    unittest.main()

