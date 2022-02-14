# quicksort referencia
# https://www.delftstack.com/pt/howto/python/sort-list-alphabetically/


def sort_nums(lst):
    if not lst:
        return []
    return (
        sort_nums([x for x in lst[1:] if x < lst[0]])
        + [lst[0]]
        + sort_nums([x for x in lst[1:] if x >= lst[0]])
    )


def find_duplicate(nums):
    """ Faça o código aqui. """
    if nums is None:
        return False
    nums_sort = sort_nums(nums)
    for i in range(len(nums_sort) - 1):
        if nums_sort[i] < 0 or nums_sort[i + 1] < 0:
            return False
        if nums_sort[i] == nums_sort[i + 1]:
            return nums_sort[i]
    return False
