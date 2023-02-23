'''
indices of pattern in genome string

Sample Input:
ATAT
GATATATGCATATACTT

Sample Output:
1 3 9

'''

pattern = input('Enter pattern: ')
with open('Vibrio_cholerae.txt', 'r') as file:
    text = file.read().replace('\n', '')

text_length = len(text)
pattern_length = len(pattern)
location = []
for i in range(text_length - pattern_length+1):
    if text[i:i+pattern_length] == pattern:
        location.append(i)
print(*location, sep = ' ') 