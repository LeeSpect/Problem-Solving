import sys
input = sys.stdin.readline

T = int(input())
def decode_word(word):
    value = sum((ord(char) - ord('a')) for char in word) % 27
    if value == 26:
        return ' '
    else:
        return chr(ord('a') + value)

for _ in range(T):
    secret_message = input().strip()
    words = secret_message.split()
    decoded_message = ''.join(decode_word(word) for word in words)
    print(decoded_message)
