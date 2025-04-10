# 4.
total_length = 0
word_count = 0
with open('input.txt', 'r') as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            total_length += len(word)
            word_count += 1

print(total_length / word_count)
