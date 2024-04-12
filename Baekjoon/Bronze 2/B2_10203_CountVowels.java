import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int minX = 100;
        int maxX = 1;
        int minY = 100;
        int maxY = 1;

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int X = Integer.parseInt(st.nextToken());
            int Y = Integer.parseInt(st.nextToken());

            if (X < minX)
                minX = X;
            if (X > maxX)
                maxX = X;
            if (Y < minY)
                minY = Y;
            if (Y > maxY)
                maxY = Y;
        }

        int sideLength = Math.max(maxX - minX, maxY - minY);
        int area = sideLength * sideLength;

        System.out.println(area);
    }
}