package a0213;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class G4_17144_미세먼지안녕 {
    static int[] rpos = {1, -1, 0, 0};
    static int[] cpos = {0, 0, 1, -1};

    private static void spreadDust(int R, int C, int[][] G) {
        int[][] temp = new int[R][C];
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (G[i][j] > 0) {
                    int amount = G[i][j] / 5;
                    int count = 0;
                    for (int d = 0; d < 4; d++) {
                        int nr = i + rpos[d];
                        int nc = j + cpos[d];
                        if (nr >= 0 && nr < R && nc >= 0 && nc < C && G[nr][nc] != -1) {
                            temp[nr][nc] += amount;
                            count++;
                        }
                    }
                    G[i][j] -= amount * count;
                }
            }
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                G[i][j] += temp[i][j];
            }
        }
    }

    private static void cleaning(int R, int C, int[][] G, int[] cleaner) {
        upperClean(R, C, G, cleaner[0]);
        lowerClean(R, C, G, cleaner[1]);
    }

    private static void upperClean(int R, int C, int[][] G, int row) {
        for (int i = row - 1; i > 0; i--) G[i][0] = G[i-1][0];
        for (int i = 0; i < C - 1; i++) G[0][i] = G[0][i+1];
        for (int i = 0; i < row; i++) G[i][C-1] = G[i+1][C-1];
        for (int i = C - 1; i > 1; i--) G[row][i] = G[row][i-1];
        G[row][1] = 0;
    }

    private static void lowerClean(int R, int C, int[][] G, int row) {
        for (int i = row + 1; i < R - 1; i++) G[i][0] = G[i+1][0];
        for (int i = 0; i < C - 1; i++) G[R-1][i] = G[R-1][i+1];
        for (int i = R - 1; i > row; i--) G[i][C-1] = G[i-1][C-1];
        for (int i = C - 1; i > 1; i--) G[row][i] = G[row][i-1];
        G[row][1] = 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());

        int[][] G = new int[R][C];
        int[] cleaner = new int[2];
        boolean foundCleaner = false;

        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < C; j++) {
                G[i][j] = Integer.parseInt(st.nextToken());
                if (G[i][j] == -1 && !foundCleaner) {
                    cleaner[0] = i;
                    cleaner[1] = i + 1;
                    foundCleaner = true;
                }
            }
        }

        for (int t = 0; t < T; t++) {
            spreadDust(R, C, G);
            cleaning(R, C, G, cleaner);
        }

        int dustSum = 0;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (G[i][j] > 0) dustSum += G[i][j];
            }
        }

        System.out.println(dustSum);
    }
}
