import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        String input;
        while (!(input = br.readLine()).equals("0+0=0")) {
            st = new StringTokenizer(input, "+=");
            int a = Integer.parseInt(new StringBuilder(st.nextToken()).reverse().toString());
            int b = Integer.parseInt(new StringBuilder(st.nextToken()).reverse().toString());
            int c = Integer.parseInt(new StringBuilder(st.nextToken()).reverse().toString());

            if (a + b == c)
                sb.append("True\n");
            else
                sb.append("False\n");
        }
        sb.append("True");

        System.out.println(sb.toString());
    }
}
