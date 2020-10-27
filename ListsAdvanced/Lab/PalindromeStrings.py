words = [word for word in input().split() if word == word[::-1]]
searched = input()

print(words)
print(f'Found palindrome {words.count(searched)} times')
