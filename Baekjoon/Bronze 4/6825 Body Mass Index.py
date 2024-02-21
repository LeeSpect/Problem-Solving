import sys; input = sys.stdin.readline

def main():
    weight = float(input())
    height = float(input())
    BMI = weight / (height * height)
    if BMI > 25:
        print('Overweight')
    elif BMI >= 18.5:
        print('Normal weight')
    else:
        print('Underweight')

if __name__=='__main__':
    main()
