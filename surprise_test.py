string = input()
list1 =['{', '(', '[']
list2 =['}', ')', ']']


lst =[]
Dict ={ ')':'(', '}':'{', ']':'['}
a = b = c = 0
if string[0]  in list2:
    print(1)

else:

    for i in range(0, len(string)):
        if string[i] in list1:
            lst.append(string[i])
            k = i + 2
        else:
            if len(lst)== 0 and (string[i] in list2):
                print(i + 1)
                c = 1
                break
            else:

                if Dict[string[i]]== lst[len(lst)-1]:
                    lst.pop()
                else:
                    print(i + 1)
                    a = 1
                    break
    if len(lst)== 0 and c == 0:
        print("success")
        b = 1

    if a == 0 and b == 0 and c == 0:
        print(k)
