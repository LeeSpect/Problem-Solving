import java.util.Scanner;

public class Main
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = Integer.parseInt(sc.nextLine());
        for (int i = 0; i < N; i++) {
            String str = sc.nextLine();

            System.out.println(str.substring(0, 1).toUpperCase() + str.substring(1));
        }
    }
}

// python
// import sys
// input = sys.stdin.readline

// def main():
//     T = int(input())
//     for _ in range(T):
//         string = input().rstrip()
//         print(string[0].upper() + string[1:])

// if __name__ == "__main__":
//     main()
