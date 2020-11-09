#zadanie 1
def mieszanka(a_list, b_list):
    length = len(a_list)
    i = 0
    zwrot_list = []
    while i < length:
        if i+1/2 == 1:
            zwrot_list.append(a_list[i])
        else:
            zwrot_list.append(b_list[i])

#zadanie 2
