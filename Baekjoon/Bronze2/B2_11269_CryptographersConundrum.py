import sys
input = sys.stdin.readline

def main():
    cipher_text = input().strip()
    target = "PER"
    changes_needed = 0

    for i, char in enumerate(cipher_text):
        if char != target[i % 3]:
            changes_needed += 1

    print(changes_needed)

if __name__ == "__main__":
    main()
