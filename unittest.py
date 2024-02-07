import unittest
from main import bubble_sort
from gnome import gnome_sort
from merge import merge_sort
from selection import selection_sort

class TestSortingAlgorithms(unittest.TestCase):
    def test_bubble_sort(self):
        data = [5, 3, 8, 4, 2]
        expected = [2, 3, 4, 5, 8]
        bubble_sort(data)
        self.assertEqual(data, expected)

    def test_gnome_sort(self):
        data = [5, 3, 8, 4, 2]
        expected = [2, 3, 4, 5, 8]
        gnome_sort(data)
        self.assertEqual(data, expected)

    def test_merge_sort(self):
        data = [5, 3, 8, 4, 2]
        expected = [2, 3, 4, 5, 8]
        merge_sort(data)
        self.assertEqual(data, expected)

    def test_selection_sort(self):
        data = [5, 3, 8, 4, 2]
        expected = [2, 3, 4, 5, 8]
        selection_sort(data)
        self.assertEqual(data, expected)

if __name__ == '__main__':
    unittest.main()
