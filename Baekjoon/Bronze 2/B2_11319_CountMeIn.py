import sys
input = sys.stdin.readline

def count_vowels_consonants(sentence):
    vowels = set("aeiouAEIOU")
    consonant_count = 0
    vowel_count = 0

    for char in sentence:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return consonant_count, vowel_count

S = int(input().strip())

for _ in range(S):
    sentence = input().strip()
    consonant_count, vowel_count = count_vowels_consonants(sentence)
    print(consonant_count, vowel_count)
