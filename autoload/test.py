import vim


def drr():
    marks = vim.command("marks").split()
    print(marks[0])
    print(":;)")
