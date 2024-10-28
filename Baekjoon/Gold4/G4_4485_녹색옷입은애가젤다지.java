import java.util.*;
import java.io.*;

public class G4_4485_녹색옷입은애가젤다지 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		int tc=1;
		int[] dx={1,-1,0,0}, dy= {0,0,-1,1};
		int[][] map;
		boolean[][] visited;
		Queue<int[]> pq;
		
		while(true){
			int N=Integer.parseInt(br.readLine());
			if(N==0) break;
			map = new int[N][N];
			for(int i=0; i<N; i++){
				st = new StringTokenizer(br.readLine(), " ");
				for(int j=0; j<N; j++){
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			pq = new PriorityQueue<>((o1, o2) -> Integer.compare(o1[0], o2[0]));
			visited = new boolean[N][N];
			pq.offer(new int[] {map[0][0], 0, 0});
			while(!pq.isEmpty()){
				int[] tempArr = pq.poll();
				if(tempArr[1] == N-1 && tempArr[2] == N-1){
					sb.append("Problem ").append(tc++).append(": ").append(tempArr[0]).append("\n");
					break;
				}
				visited[tempArr[1]][tempArr[2]] = true;
				for(int d=0; d<4; d++){
					int nx = tempArr[1] + dx[d];
					int ny = tempArr[2] + dy[d];
					if(0>nx || N-1<nx || 0>ny || N-1<ny || visited[nx][ny]) continue;
					pq.offer(new int[]{tempArr[0]+map[nx][ny], nx, ny});
				}
			}
		}
		System.out.println(sb.toString());
	}
}
