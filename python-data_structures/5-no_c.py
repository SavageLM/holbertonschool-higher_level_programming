#!usr/bin/python3
def no_c(my_string):

    new_string = ""
    if my_string is not None:
        for i in my_string:
            if my_string[i] != "c" and my_string[i] != "C":
                new_string.append(my_list[i])
        return new_string
