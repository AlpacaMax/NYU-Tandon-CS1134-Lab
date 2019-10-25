from ArrayStack import *
import random

def stack_sum(s):
    if len(s) == 1:
        return s.top()
    else:
        val = s.pop()
        rest = val + stack_sum(s)
        s.push(val)
        return rest

def eval_prefix(exp_str):
    exp_lst = exp_str.split()
    numStack = ArrayStack()
    for i in range(len(exp_lst) - 1, -1, -1):
        token = exp_lst[i]
        if token.isdigit():
            numStack.push(token)
        else:
            arg1 = numStack.pop()
            arg2 = numStack.pop()
            result = eval(arg1 + token + arg2)
            numStack.push(str(result))
    return numStack.pop()

def is_balanced(input_str):
    lefts = "({["
    rights = ")}]"
    bCheck = ArrayStack()
    for i in input_str:
        if i in lefts:
            bCheck.push(i)
        else:
            if len(bCheck) != 0 and lefts.index(bCheck.top()) == rights.index(i):
                bCheck.pop()
            else:
                return False
    if len(bCheck) == 0:
        return True
    else:
        return False

def is_balanced2(input_str):
    leftP = ArrayStack()
    for i in input_str:
        if i == '(':
            leftP.push(i)
        elif len(leftP) != 0:
            leftP.pop()
        else:
            return False
    if len(leftP):
        return False
    else:
        return True

def flatten_list(lst):
    store = ArrayStack()
    isFlattened = False
    while not isFlattened:
        isFlattened = True
        for i in range(len(lst)):
            store.push(lst.pop())
        for i in range(len(store)):
            top = store.pop()
            if isinstance(top, list):
                isFlattened = False
                for i in top:
                    lst.append(i)
            else:
                lst.append(top)

def stack_sort(s):
    store = ArrayStack()
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(s)):
            store.push(s.pop())
        
        while len(store) > 0:
            if len(store) == 1:
                s.push(store.pop())
            else:
                arg1 = store.pop()
                arg2 = store.pop()
                if arg1 > arg2:
                    s.push(arg1)
                    store.push(arg2)
                else:
                    s.push(arg2)
                    store.push(arg1)
                    isSorted = False

'''
s = ArrayStack()
a = [i for i in range(100)]
random.shuffle(a)
for i in a:
    s.push(i)
stack_sort(s)
print(s.data)
'''

lst =  [ 1, [2, 3, 4], [5, [6, [7] ] , [8, [ [ 9 ] ] ] ]]
flatten_list(lst)
print(lst)