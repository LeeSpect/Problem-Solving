package a0208;

import java.io.*;
import java.util.*;

class d3_5215_햄버거다이어트 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<=T; tc++) {
			st = new StringTokenizer(br.readLine(), " ");

			int N = Integer.parseInt(st.nextToken());
			int L = Integer.parseInt(st.nextToken());
			int[] flavor = new int[N];
			int[] calorie = new int[N];

			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				flavor[i] = Integer.parseInt(st.nextToken());
				calorie[i] = Integer.parseInt(st.nextToken());
			}

			int[] dp = new int[L + 1];
			for (int i=0; i<N; i++) {
				for (int j = L; calorie[i] <= j; j--) {
					dp[j] = Math.max(dp[j], dp[j - calorie[i]] + flavor[i]);
				}
			}
			sb.append("#").append(tc).append(" ").append(dp[L]).append("\n");
		}
		System.out.println(sb);
		br.close();
	}
}