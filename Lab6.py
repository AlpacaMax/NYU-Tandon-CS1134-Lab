import os

def sum_to(n):
    if n == 0:
        return 0
    else:
        return n + sum_to(n-1)

def product_evens(n):
    if n % 2 == 1:
        n -= 1

    if n <= 2:
        return 2
    else:
        return n * product_evens(n - 2)

def find_max(lst, low, high):
    if low == high:
        return lst[low]
    else:
        return max([lst[low], find_max(lst, low + 1, high)])

def is_palindrome(input_str, low, high):
    if low >= high:
        return True
    else:
        rest_isPa = is_palindrome(input_str, low + 1, high - 1)
        curr_isPa = input_str[low] == input_str[high]
        if rest_isPa:
            return curr_isPa
        else:
            return rest_isPa

def binary_search(lst, low, high, val):
    if low > high:
        return None
    else:
        mid = (low + high) // 2
        if lst[mid] == val:
            return mid
        elif lst[mid] < val:
            return binary_search(lst, mid + 1, high, val)
        else:
            return binary_search(lst, low, mid - 1, val)

def split_parity(lst, low, high):
    if low >= high:
        return

    while lst[low] % 2 == 0:
        low += 1
    while abs(lst[high] % 2) == 1:
        high -= 1
    
    if low < high:
        temp = lst[low]
        lst[low] = lst[high]
        lst[high] = temp
        split_parity(lst, low, high)

def vc_count(word, low, high):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I','O','U']
    if low > high:
        return (0,0)
    else:
        rest_count = vc_count(word, low + 1, high)
        if word[low] in vowels:
            return (rest_count[0] + 1, rest_count[1])
        else:
            return (rest_count[0], rest_count[1] + 1)

def nested_sum(lst):
    result = 0
    for i in lst:
        if isinstance(i, list):
            result += nested_sum(i)
        else:
            result += i
    return result

def disk_usage(path):
    totalUsage = os.path.getsize(path)
    if os.path.isdir(path):
        allFiles = os.listdir(path)
        for i in range(len(allFiles)):
            absolutePath = os.path.join(path, allFiles[i])
            totalUsage += disk_usage(absolutePath)
    
    return totalUsage

#print(disk_usage('/Users/yangxin7001/Documents/Notes'))
#print(os.path.getsize('/Users/yangxin7001/Documents/Notes'))