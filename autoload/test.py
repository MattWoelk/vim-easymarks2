import vim


# TODO add more options here TODO make customizable
possible_marks = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def drr():
    marks = get_mark_locations()
    #marks = vim.command("marks").split()
    print(marks['a'])
    print(";)")


def get_mark_locations():
    result = {}
    for mark in possible_marks:
        mark_location = vim.current.buffer.mark(mark)
        if mark_location:
            mark_location = {'row': mark_location[0], 'col': mark_location[1]}
        result[mark] = mark_location
    return result
