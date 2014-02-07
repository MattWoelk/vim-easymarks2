import vim


def drr():
    marks = vim.eval("marks").split()
    print(marks[0])
    print(":;)")
