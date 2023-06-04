"""
module depicting dictionary and their operations.
"""


class DictMapping():
    """
    Mapping and transforming list of dictionaries.
    """
    def __init__(self, _input):
        """
        Initialize a list of dictionaries input.
        """
        self.input = _input

    def transform_mapping(self) -> list[dict]:
        """
        Transforms a list of dictionaries by interchanging list of values with keys.

        Returns:
        --------
        list[dict]: Transformed list of dictionaries.
        """
        result = []
        dict_map = {}
        length = len(self.input)
        for i in range(length):
            key:int = self.input[i]["id"]
            val:str = self.input[i]["keys"]
            items:list[str] = val.split(", ")
            for item in items:
                if item in dict_map:
                    dict_map[item].append(key)
                else:
                    dict_map.update({item: [key]})
        result = [{"key": key, "ids": values} for key, values in dict_map.items()]
        return result


if __name__ == "__main__":
    _input = [
        {"id": 1001, "keys": "abc, def, ijk"},
        {"id": 1002, "keys": "abc, ghk, ijk"},
        {"id": 1003, "keys": "abc, def, ijk"},
        {"id": 1004, "keys": "def, ghk, ijk"},
    ]
    mapping = DictMapping(_input)
    print(mapping.transform_mapping())
