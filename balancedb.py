def isBalanced(s):
    if len(s) % 2 == 0:
        opens = ['(', '[', '{']
        closes = [')', ']', '}']
        list1 = []
        for i in s:
            if i in opens:
                list1.append(i)
            else:
                if len(list1) > 0 and (i == ']' and list1[-1] == '[' or i == ')' and list1[-1] == '(' or i == '}' and list1[-1] == '{'):
                    list1.pop()
                else:
                    return 'NO'
        if list1 == []:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'