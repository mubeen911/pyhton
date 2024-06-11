

def print_ele(lst, index):
    if index < len(lst):
        print(lst[index], end=" ")  # Adding a space for better readability
        print_ele(lst, index + 1)
    else:
        return


item=[23,45,667,89,34]
print_ele(item,0)