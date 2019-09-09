import random

def add_binary(bin_num1, bin_num2):
    '''
    bin_num1 - type: str
    bin_num2 - type: str
    return value - type: str
    '''

    a = list(bin_num1)
    b = list(bin_num2)

    a.reverse()
    b.reverse()

    prompt = 0

    result = []

    while len(a) > len(b) or len(a) < len(b):
        if len(a) > len(b):
            b.append('0')
        elif len(a) < len(b):
            a.append('0')
    
    for i in range(len(a)):
        numA = int(a[i])
        numB = int(b[i])

        res = numA + numB + prompt

        if res > 1:
            res -= 2
            prompt = 1
        else:
            prompt = 0
        
        result.append(str(res))
    
    if prompt == 1:
        result.append(str(prompt))
    
    result.reverse()
    strResult = "".join(result)

    return strResult

def can_construct(word, letters):
    '''
    word - type: str
    letters - type: str
    return value - type: bool
    '''

    letters = list(letters)

    for i in word:
        if i in letters:
            letters.remove(i)
        else:
            return False

    return True

def create_permutation(n):
    numbers = list(range(n))
    result = []
    
    while len(numbers) > 0:
        index = random.randint(0, len(numbers) - 1)
        num = numbers[index]
        result.append(num)
        numbers.remove(num)

    return result

def scramble_word(word):
    letters = list(word)
    result = list(word)
    newOrder = create_permutation(len(letters))

    for i in range(len(letters)):
        result[i] = letters[newOrder[i]]
    
    return ''.join(result)

def GuessGame(word):
    original = word
    scrambled = scramble_word(word)

    print("Unscramble the word: ", ''.join(scrambled))

    counter = 1
    while True:
        prompt = "Try #" + str(counter) + ": "
        guess = input(prompt)

        if guess == original:
            print("Yay, you got it!")
            break
        else:
            print("Wrong!")
        
        counter += 1

GuessGame('pokemon')