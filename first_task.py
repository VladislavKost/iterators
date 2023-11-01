class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.index = 0
        self.sublist_iterator = iter([])

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.sublist_iterator)
            return item
        except StopIteration:
            if self.index < len(self.list_of_list):
                self.sublist_iterator = iter(self.list_of_list[self.index])
                self.index += 1
                return next(self.sublist_iterator)
            else:
                raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
