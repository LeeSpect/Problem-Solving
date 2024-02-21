package a0220;

import java.io.*;
import java.util.*;

public class G4_2636_치즈{
	static int N, M, time=0, lastSize=0;
	static int[] dx={-1,1,0,0}, dy={0,0,-1,1};
	static int[][] map;
	static boolean[][] visited;
	static ArrayDeque<Point> airDeq = new ArrayDeque<>();
	static ArrayDeque<Point> cheeseDeq = new ArrayDeque<>();
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		visited = new boolean[N][M];
		map=new int[N][M];
		for(int i=0; i<N; i++){
			st = new StringTokenizer(br.readLine(), " ");
			for(int j=0; j<M; j++)map[i][j] = Integer.parseInt(st.nextToken());
		}
		
		for(int i=0; i<N; i++){
			if(map[i][0]==0 && !visited[i][0]){
				visited[i][0] = true;
				airDeq.offer(new Point(i,0));
			}
			if(map[i][M-1]==0 && !visited[i][M-1]){
				visited[i][M-1] = true;
				airDeq.offer(new Point(i,M-1));
			}
		}
		for(int i=0; i<M; i++){
			if(map[0][i]==0 && !visited[0][i]){
				visited[0][i] = true;
				airDeq.offer(new Point(0,i));
			}
			if(map[N-1][i]==0 && !visited[N-1][i]){
				visited[N-1][i] = true;
				airDeq.offer(new Point(N-1,i));
			}
		}

		// 공기와 접촉한 치즈 찾기
		airing();
		while(!cheeseDeq.isEmpty()){
			// 치즈 녹이기
			melt();
			// 공기와 접촉한 치즈 찾기
			airing();
			time++;
		}
		sb.append(time).append("\n").append(lastSize);
		
		System.out.println(sb.toString());
		br.close();
	}

	// 공기와 접촉한 치즈 찾기
	static void airing(){
		while(!airDeq.isEmpty()){
			Point temp = airDeq.poll();
			for(int d=0; d<4; d++){
				int nx = temp.x+dx[d];
				int ny = temp.y+dy[d];
				if(0<=nx&&nx<N && 0<=ny&&ny<M && !visited[nx][ny]){
					visited[nx][ny] = true;
					if(map[nx][ny]==0) airDeq.offer(new Point(nx,ny));
					else cheeseDeq.offer(new Point(nx,ny));
				}
			}
		}
	}

	// 치즈 녹이기
	static void melt(){
		lastSize = cheeseDeq.size();
		while(!cheeseDeq.isEmpty()){
			Point temp = cheeseDeq.poll();
			airDeq.offer(temp);
		}
	}

	static class Point{
		int x, y;
		public Point(int x, int y){
			this.x = x; this.y = y;
		}
	}
}
