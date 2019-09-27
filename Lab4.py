def reverse_list(lst):
    for i in range(-1, -len(lst)-1, -1):
        temp = lst[i]
        del lst[i]
        lst.append(temp)

def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-(i+1)]:
            return False
    
    return True

def move_zeroses(nums):
    counter = 0
    ind = 0
    while ind < len(nums):
        if nums[ind] == 0:
            counter += 1
            del nums[ind]
        else:
            ind += 1
    
    for i in range(counter):
        nums.append(0)

def find_missing(lst):
    for i in range(len(lst)):
        if i != lst[i]:
            return i

def find_missing_c(lst):
    complete = sum([i for i in range(len(lst) + 1)])
    num = sum(lst)
    
    return complete - num