# get character from ASCII Value
def get_char(c):
    return chr(c)

# Find numbers which are divisible by given number
def divisible_by(numbers, divisor):
    result = []
    
    for i in numbers:
        if i % divisor == 0:
            result.append(i)
    return result

# Alternate capitalization
def capitalize(s):
    even = ""
    odd = ""
    
    for i in range(len(s)):
        if i % 2 == 0:
            even += s[i].upper()
            odd += s[i]
        else:
            odd += s[i].upper()
            even += s[i]
    return [even,odd]

#Minimize Sum Of Array (Array Series #1)
def min_sum(arr):
    arr.sort()
    x = len(arr)
    minimum_sum = 0
    
    for i in range(x // 2):
        minimum_sum += arr[i] * arr[x - 1 - i]
        
    return minimum_sum

# Sum consecutives
def sum_consecutives(lst):
    result = []
    new_sum = lst[0]
    
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            new_sum += lst[i]
        else:
            result.append(new_sum)
            new_sum = lst[i]
            
    result.append(new_sum)
    
    return result

#Sum of parts
def parts_sums(ls):
    old_sum = sum(ls)
    result = []
    new_sum = 0
    
    for i in ls:
        result.append(old_sum - new_sum)
        new_sum += i
    result.append(0)
    
    return result

#Word a10n (abbreviation)


