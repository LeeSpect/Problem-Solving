import java.io.IOException;
import java.util.Scanner;

public class javaPractice {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        while (true) {
            double n = sc.nextDouble();
            if (n == 0) {
                break;
            }
            double answer = 1 + n + Math.pow(n, 2) + Math.pow(n, 3) + Math.pow(n, 4);
            System.out.println(String.format("%.2f", answer));
        }
    }

}
