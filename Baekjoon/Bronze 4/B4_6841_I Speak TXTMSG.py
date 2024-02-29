import sys
input = sys.stdin.readline

def main():
    a_list = ['CU', ':-)', ':-(', ';-)', ':-P', '(~.~)',
              'TA', 'CCC', 'CUZ', 'TY', 'YW', 'TTYL']
    b_list = ['see you', "I’m happy", "I’m unhappy", 'wink', 'stick out my tongue', 'sleepy', 'totally awesome',
              'Canadian Computing Competition', 'because', 'thank-you', "you’re welcome", 'talk to you later']
    while 1:
        string = input().rstrip()
        if string in a_list:
            print(b_list[a_list.index(string)])
        else:
            print(string)
        if string == 'TTYL':
            break

if __name__ == '__main__':
    main()
