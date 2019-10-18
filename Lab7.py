def str_to_int(int_str):
    return sum([int(int_str[i]) * 10**(len(int_str) - i - 1) for i in range(len(int_str))])

def max_two_product(lst):
    maximum = [max(lst), min(lst)]
    for i in lst:
        if i > maximum[1] and i != maximum[0]:
            maximum[1] = i
    return maximum[0] * maximum[1]

def non_vowels(input_str, low, high):
    vowels = 'aeiouAEIOU'
    if low == high:
        if input_str[low] in vowels:
            return []
        else:
            return [input_str[low]]
    else:
        rest = non_vowels(input_str, low, high - 1)
        if input_str[high] not in vowels:
            rest.append(input_str[high])
        return rest

def find_max_even(lst, low, high):
    if low == high:
        if lst[low] % 2 == 0:
            return lst[low]
        else:
            return None
    else:
        rest = find_max_even(lst, low + 1, high)
        if rest == None:
            if lst[low] % 2 == 0:
                return lst[low]
            else:
                return None
        else:
            if lst[low] % 2 == 0:
                return max(rest, lst[low])
            else:
                return rest

def reverse_vowels(input_str):
    left = 0
    right = len(input_str) - 1
    vowels = 'aeiouAEIOU'
    inputStr = list(input_str)
    
    while left < right:
        while left < right and inputStr[left] not in vowels:
            left += 1

        while left < right and inputStr[right] not in vowels:
            right -= 1
        
        inputStr[left], inputStr[right] = inputStr[right], inputStr[left]
        left += 1
        right -= 1
    
    return ''.join(inputStr)

def square_root(num):
    base = 0
    while base**2 < num:
        base += 1
    while base**2 > num:
        base -= 0.1
    while base**2 < num:
        base += 0.01
    return round(base, 2)