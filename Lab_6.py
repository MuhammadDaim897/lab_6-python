
# QUestion 1 lab 6
ounput=[2, 3, 2, 5, 3, 2, 5, 8]

result={}

for num in ounput:
    if num in result:
        result[num]=+1
    else:
        result[num]=1
        print(result)


# QUestion 2 lab 6

marks = {
    'Ali': 85,
    'Sara': 95,
    'Ahmed': 95,
    'Noor': 78
}

highest = max(marks.values())

for name, score in marks.items():
    if score == highest:
        print(name, score)
    else:
        print(name, score)

# Question 3 lab 6

data = {'a': 1, 'b': 2, 'c': 3}

result = {}

for key, value in data.items():
    result[value] = key

print(result)

# Question 4 lab 6

words = ['apple', 'ant', 'banana', 'ball', 'cat']

result = {}

for word in words:
    first = word[0]

    if first in result:
        result[first].append(word)
    else:
        result[first] = [word]

print(result)