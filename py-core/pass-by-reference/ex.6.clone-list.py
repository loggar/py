initial_list = [1, 2, 3]


def duplicate_last(a_list):
    last_element = a_list[-1]
    a_list.append(last_element)
    return a_list


new_list = duplicate_last(a_list=initial_list.copy()
                          )  # making a copy of the list
print(new_list)
print(initial_list)
