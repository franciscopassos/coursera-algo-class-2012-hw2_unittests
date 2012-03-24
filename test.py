import unittest
import qsort


expectations = [ ('array0.txt', 64, 60, 55),
                 ('array1.txt', 253, 253, 66),
                 ('array2.txt', 1596, 1596, 228),
                 ('array3.txt', 576, 669, 636),
                 ('array4.txt', 237, 235, 172),
                 ('array5.txt', 252, 185, 186),
                 ('array6.txt', 236, 258, 177),
                 ('array7.txt', 213, 199, 180),
                 ('array8.txt', 231, 206, 192),
                 ('array9.txt', 282, 310, 214),
                 ('array10.txt', 191, 232, 206) ]


class TestFiles(unittest.TestCase):

  def _testFile(self, filename, expected_low, expected_high, expected_median):
  
    choosePivotFunctions = (qsort.choosePivotLow,
                            qsort.choosePivotHigh,
                            qsort.choosePivotMedian)
    expected_values = expected_low, expected_high, expected_median
    
    with open(filename) as file:
      strings = file.read().split("\n")
      l_base = [int(x) for x in strings if len(x)]
    
    for function, expected_value in zip(choosePivotFunctions, expected_values):
      l = l_base[:]
      actual_value = qsort.quicksort(l, 0, len(l)-1, function)
      self.assertEqual(expected_value, actual_value,
                       "Wrong value, expected %d, got %d (%s)" % (
                           expected_value, actual_value, function.__name__))


for filename, low, high, median in expectations:
  def test(filename, low, high, median):
    return lambda self: self._testFile(filename, low, high, median)
  setattr(TestFiles, 'test_file_%s' % filename, test(filename, low, high, median))


if __name__ == "__main__":
    unittest.main()