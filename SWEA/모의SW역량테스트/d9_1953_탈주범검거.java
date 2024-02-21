package a0220;

import java.io.*;
import java.util.*;

public class d9_1953_탈주범검거 {
	static int[] dx={-1,0,1,0}, dy= {0,1,0,-1};
	// 0:상, 1:우, 2:하, 3:좌
	static int[][] condition={{0},{0,1,2,3},{0,2},{1,3},{0,1},{2,1},{2,3},{0,3}};
	
	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/input_d9_1953.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<T+1; tc++){
			st = new StringTokenizer(br.readLine(), " ");
			int N=Integer.parseInt(st.nextToken());
			int M=Integer.parseInt(st.nextToken());
			int R=Integer.parseInt(st.nextToken());
			int C=Integer.parseInt(st.nextToken());
			int L=Integer.parseInt(st.nextToken());
			
			int[][] map = new int[N][M];
			for(int i=0; i<N; i++){
				st = new StringTokenizer(br.readLine(), " ");
				for(int j=0; j<M; j++) map[i][j] = Integer.parseInt(st.nextToken());	
			}
			
			ArrayDeque<Point> deq = new ArrayDeque<>();
			boolean[][] visited = new boolean[N][M];
			deq.offer(new Point(R, C));
			visited[R][C] = true;
			int ans = 1;
			for(int i=0; i<L-1; i++){
				int size = deq.size();
				for(int s=0; s<size; s++){
					Point tempPoint = deq.pollFirst();
					for(int d=0; d<4; d++){
						boolean flag = true;
						for(int num:condition[map[tempPoint.x][tempPoint.y]]) {
							if(num == d) {
								flag=false; break;
							}
						}
						if(flag) continue;
						
						int nx = tempPoint.x + dx[d];
						int ny = tempPoint.y + dy[d];
						if(0>nx||nx>N-1 || 0>ny||ny>M-1 || visited[nx][ny] || map[nx][ny]==0) continue;
						// 0이면 visited 해보는 방법도 시도해볼 만함.
						for(int nextType:condition[map[nx][ny]]){
							if((d+2)%4 == nextType) {
								deq.offer(new Point(nx, ny));
								visited[nx][ny] = true;
								ans++;
								break;
							}
						}
					}
				}
			}
			sb.append("#").append(tc).append(" ").append(ans).append("\n");
		}
		System.out.println(sb.toString());
		br.close();
	}
	
	static class Point{
		int x, y;
		public Point(int x, int y) {
			this.x=x;this.y=y;
		}
	}
}
