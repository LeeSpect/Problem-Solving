import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());

        for (int i = 0; i < n; i++) {
            int answer = 0;
            String k = sc.nextLine();
            for (int j = 0; j < k.length(); j++) {
                if (k.charAt(j) == 'U'){
                    answer += 1;
                }
                else {
                    break;
                }
            }
            System.out.println(answer);
        }
        sc.close();
    }

}
