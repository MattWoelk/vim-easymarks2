import vim


possible_marks = ['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'] # TODO add more options here TODO make customizable


def drr():
    marks = {}
    marks['a'] = vim.current.buffer.mark('a')
    #marks = vim.command("marks").split()
    print(marks['a'])
    print(";)")
