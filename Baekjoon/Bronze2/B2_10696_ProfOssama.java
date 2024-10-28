import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int testCase = 1; testCase <= T; testCase++) {
            String[] input = br.readLine().split(" ");
            String N = input[0];
            int X = Integer.parseInt(input[1]);

            int remainder = 0;
            for (int i = 0; i < N.length(); i++) {
                int each = Character.getNumericValue(N.charAt(i));
                remainder = (remainder * 10 + each) % X;
            }

            sb.append("Case ").append(testCase).append(": ").append(remainder).append("\n");
        }

        System.out.print(sb.toString());
    }
}