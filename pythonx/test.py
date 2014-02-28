import vim


# TODO add more options here TODO make customizable
possible_marks = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def drr():
    #marks = get_mark_locations()
    #print(marks)
    print(vim.vars)
    highlight_marks()


def get_mark_locations():
    """ Output format: {'a': {'col': 0, 'row': 4}, etc.}"""
    result = {}
    for mark in possible_marks:
        mark_location = vim.current.buffer.mark(mark)
        if mark_location:
            mark_location = {'row': mark_location[0], 'col': mark_location[1]}
            result[mark] = mark_location
    return result


def highlight_marks():
    print("highlighting")
