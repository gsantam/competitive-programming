def rotate( array, k) -> None:
    left_list = []
    for i in range(k):
        left_list.append(array.pop())

    left_list = list(reversed(left_list))

    array = list(reversed(array))
    while len(array)>0:
        left_list.append(array.pop())
    return left_list
