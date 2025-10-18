def unique_elements_count(lst, threshold):
    unique_count = len(set(lst))
    return unique_count > threshold

def test_task5():
    print(unique_elements_count([1, 2, 3, 2, 1], 5))

    print(unique_elements_count(['a', 'b', 'a', 'c'], 3))

    print(unique_elements_count([], 0))

if __name__ == "__main__":
    test_task5()
