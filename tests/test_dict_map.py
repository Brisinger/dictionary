"""
Module to test dictionary mappings in a list of dictionaries.
"""
import unittest
from unittest import TestCase
from src.dict_map import DictMapping


class TestDictMapping(TestCase):
    """
    Test class testing mapping and operations with dictionaries.
    """
    def setUp(self) -> None:
        """
        Initialize test input and expected result.
        """
        self.input =  [
            {"id": 1001, "keys": "abc, def, ijk"},
            {"id": 1002, "keys": "abc, ghk, ijk"},
            {"id": 1003, "keys": "abc, def, ijk"},
            {"id": 1004, "keys": "def, ghk, ijk"},
        ]
        self.expected = [
            {"key": "abc", "ids": [1001, 1002, 1003]},
            {"key": "def", "ids": [1001, 1003, 1004]},
            {"key": "ijk", "ids": [1001, 1002, 1003, 1004]},
            {"key": "ghk", "ids": [1002, 1004]},
        ]
        return super().setUp()

    def test_transform_mapping(self):
        """
        Testing transformation operations on list of dictionaries.
        """
        # Arrange
        expected = self.expected
        mapping = DictMapping(self.input)
        # Act
        result = mapping.transform_mapping()
        # Assert
        self.assertEqual(len(result), len(expected))
        for i, val in enumerate(result):
            self.assertEqual(val["key"], expected[i]["key"])
            for j, item in enumerate(val["ids"]):
                self.assertEqual(item, expected[i]["ids"][j])

    if __name__ == "__main__":
        unittest.main()
