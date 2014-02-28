import vim


# TODO add more options here TODO make customizable
possible_marks = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def drr():
    marks = get_mark_locations()
    old_buf = list(vim.current.buffer)
    print(marks)
    a_mark = marks['a']
    cur_line = vim.current.buffer[a_mark['row'] - 1]
    cur_line_list = list(cur_line)
    cur_line_list[a_mark['col']] = '?'
    print(cur_line_list)
    vim.current.buffer[a_mark['row'] - 1] = ''.join(cur_line_list)
    #print(old_buf)
    #print(vim.vars)
    highlight_marks()
    restore_buffer(old_buf)


def insert_mark_labels():
    buf = vim.current.buffer
    return buf


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


def restore_buffer(buf):
    pass
