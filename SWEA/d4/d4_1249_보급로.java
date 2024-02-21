package a0212;

import java.io.*;
import java.util.*;

public class d4_1249_보급로 {
	static int N;
	static int[] dx = new int[] {-1,0,1,0}, dy = new int[] {0,1,0,-1};
	static int[][] dp;
	
	public static void main(String[] args) throws Exception{
	    System.setIn(new FileInputStream("res/input_d4_1249.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<T+1; tc++) {
			N = Integer.parseInt(br.readLine());
			int[][] map = new int[N][N];
			for(int i=0; i<N; i++) {
				String string = br.readLine();
				for(int j=0; j<N; j++) {
					map[i][j] = string.charAt(j) - '0';
				}
			}
			sb.append("#").append(tc).append(" ").append(solve(map)).append("\n");
		}
		System.out.println(sb);
		br.close();
	}
	
	static int solve(int[][] map) {
		PriorityQueue<int[]> pq = new PriorityQueue<>((l1, l2) -> Integer.compare(l1[0], l2[0])); // l[0]:비용,l[1]:x좌표,l[2]:y좌표
		
		dp = new int[N][N];
		dp[0][0] = 0;
		for(int i=0; i<N; i++) for(int j=0; j<N; j++) dp[i][j] = Integer.MAX_VALUE;
		
		pq.add(new int[] {map[0][0], 0, 0});
		
		while(!pq.isEmpty()) {
			int[] temp = pq.poll();
			for(int d=0; d<4; d++) {
				int nx = temp[1] + dx[d];
				int ny = temp[2] + dy[d];
				if (isValid(nx, ny) && temp[0]+map[nx][ny] < dp[nx][ny]) {
					if(nx==N-1 && ny==N-1) return temp[0]+map[nx][ny];
					dp[nx][ny] = temp[0]+map[nx][ny];
					pq.add(new int[] {dp[nx][ny], nx, ny});
				}
			}
		}
		return dp[N-1][N-1];
	}
	
	static boolean isValid(int x, int y) {
		return 0<=x&&x<N && 0<=y&&y<N;
	}
	
}
