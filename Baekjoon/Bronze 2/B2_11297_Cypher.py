import sys
input = sys.stdin.readline
def decrypt_message(date, message):
    day, month, year = map(int, date.split())
    S = (day + month + year) % 25 + 1
    
    decrypted = []
    for char in message:
        if 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') - S) % 26 + ord('a'))
            decrypted.append(new_char)
        else:
            decrypted.append(char)
    
    return ''.join(decrypted)

while True:
    date_input = input().rstrip()
    if date_input == "0 0 0":
        break
    
    encrypted_message = input().rstrip()
    
    decrypted_output = decrypt_message(date_input, encrypted_message)
    print(decrypted_output)
