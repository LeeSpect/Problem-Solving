import java.util.*;

public class Main {
    public static double median(int n, int[] numbers) {
        if (n % 2 == 0) {
            int middle = n / 2;
            double medianValue = (numbers[middle - 1] + numbers[middle]) / 2.0;
            return medianValue;
        } else {
            int middle = n / 2;
            double medianValue = numbers[middle];
            return medianValue;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int i = 1;
        while (true) {
            int n = scanner.nextInt();
            if (n == 0) {
                break;
            }
            int[] numbers = new int[n];
            for (int j = 0; j < n; j++) {
                numbers[j] = scanner.nextInt();
            }
            double medianValue = median(n, numbers);
            System.out.printf("Case %d: %.1f\n", i, medianValue);
            i++;
        }
    }
}

//python
// import sys
// input = sys.stdin.readline

// def median(n, numbers):
//     if n % 2 == 0:
//         middle = n // 2
//         median_value = (numbers[middle - 1] + numbers[middle]) / 2
//     else:
//         middle = n // 2
//         median_value = numbers[middle]
//     return median_value

// i = 1
// while 1:
//     numbers = list(map(int, input().split()))
//     if not numbers[0]:
//         break
//     print(f'Case {i}: {median(numbers[0], numbers[1:]):.1f}')
//     i += 1
