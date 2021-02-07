"""

"""


def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    file_txt = open(path, "r", encoding = "UTF-8")
    file_here = ''.join(list(file_txt)).split('\n')
    return file_here
# print(read_input("skyscrapers_state.txt"))


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    lst = list(input_line)
    if lst[-1] == "*":
        del lst[-1]
    if pivot == int(lst[0]):
        del lst[0]
        int_lst = []
        for i in lst:
            int_lst.append(int(i))
        res = []
        res.append(int_lst[0])
        for j in range(len(int_lst)-1):
            if int_lst[j+1] > int_lst[j]:
                res.append(int_lst[j+1])
        if len(res) == pivot:
            return True
    else:
        return False
# print(left_to_right_check("412453*", 4))
# print(left_to_right_check("452453*", 5))


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    all_signs = ''.join(board)
    if '?' in list(all_signs):
        return False
    else:
        return True
# print(check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***']))
# print(check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215', '*35214*', '*41532*', '*2*1***']))
# print(check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))

def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    del board[0]
    del board[-1]
    res = []
    for _ in board:
        if _[0] == '*':
            del list(_)[0]
            if len(set(_)) == len(_):
                res.append(_)
        if _[-1] == '*':
            del list(_)[-1]
            if len(set(_)) == len(_):
                res.append(_)
    return res
# print(check_uniqueness_in_rows(['000', '*124*', '123*']))


def check_1(lst):
    """
    >>> check_1(['4', '1', '2', '3', '5', '4', '*'])
    True
    """
    pivot = int(lst[0])
    del lst[-1]
    board = []
    for j in lst:
        board.append(int(j))
    res = [0]
    res.append(board[1])
    
    for i in range(1, len(board)-1):
        if board[i] < board[i+1]:
            if board[i+1] > max(res):
                res.append(board[i+1])

    del res[0]
    if len(res) == pivot:
        return True

    else:
        return False
# print(check_1([4, 2, 3, 1, 4, 5]))
# print(check_1(['4', '1', '2', '3', '4', '0', '*']))

def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    result = []
    res = []
    for i in board:
        res.append(list(i))
    
    prom = []
    for j in res:
        if j[0] != '*' or j[-1] != '*':
            prom.append(j)

    for _ in prom:
        if _[0] == '*':
            rev = _[::-1]
            if check_1(rev) is True:
                result.append(_)
        else:
            if check_1(_) is True:
                result.append(_)
    
    if len(result) == len(prom):
        return True
    else:
        return False
# print(check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))
# print(check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))


def rebuilding(lst):
    res = []
    prom_res = []
    for i in lst:
        prom_res.append(list(i))

    result = []
    for _ in range(len(prom_res[0])):
        prom_here =[]
        for j in range(len(prom_res)):
            var = prom_res[j][_]
            prom_here.append(var)
        result.append(prom_here)

    return result


# print(rebuilding(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))

def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    if check_horizontal_visibility(rebuilding(board)) is True:
        return True
    else:
        return False
# print(check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))
# print(check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    lst = read_input(input_path)
    check_1 = check_columns(lst)
    check_2 = check_horizontal_visibility(lst)
    check_3 = check_not_finished_board(lst)
    check_4 = check_uniqueness_in_rows(lst)
    # if check_1 is True and check_2 is True and check_3 is True and check_4 is True:
    #     return True
    # else:
    #     return False
    # return check_4

print(check_skyscrapers('skyscrapers_state.txt'))

# if __name__ == "__main__":
#     print(check_skyscrapers("check.txt"))
