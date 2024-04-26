import sys
input = sys.stdin.readline

def encode_message(N, message):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
    index_map = {char: i for i, char in enumerate(characters)}

    reversed_message = message[::-1]

    encoded_message = []

    for char in reversed_message:
        old_index = index_map[char]
        new_index = (old_index + N) % 28
        encoded_message.append(characters[new_index])

    return ''.join(encoded_message)

def main():
    while True:
        input_line = input().rstrip()
        if input_line == "0": break
        
        parts = input_line.split()
        N = int(parts[0])
        message = parts[1]

        print(encode_message(N, message))

if __name__ == "__main__":
    main()
