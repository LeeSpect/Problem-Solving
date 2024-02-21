import java.util.Scanner;

public class Main
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = Integer.parseInt(sc.nextLine());
        for (int i = 0; i < N; i++) {
            String str = sc.nextLine();

            System.out.println(str.toLowerCase());
        }
    }
}

// 파이썬
// import sys; input=sys.stdin.readline

// def main():
//     T = int(input())
//     for i in range(T):
//         string = input().rstrip()
//         print(string.lower())

// if __name__=='__main__':
//     main()
