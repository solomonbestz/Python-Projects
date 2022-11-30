def reverse_str(string):
    rev_string = ""
    str_index = len(string)

    while str_index > 0:
        print(str_index)
        rev_string = rev_string + string[str_index - 1]
        str_index = str_index - 1

    return rev_string

if __name__=='__main__':
    print(reverse_str("david"))