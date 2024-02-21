package a0212;

import java.io.*;
import java.util.*;

public class d9_1767_프로세서연결하기 {
	static int N, isConnected, sizeOfLine, maxConnected, ans;
	static int[] dx= {-1,0,1,0}, dy= {0,1,0,-1};
	static int[][] map;
	static List<int[]> cores;

	public static void main(String[] args) throws Exception{
	    System.setIn(new FileInputStream("res/input_d9_1767.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<T+1; tc++) {
			N = Integer.parseInt(br.readLine());
			map = new int[N][N];
			cores = new ArrayList<>();
			for(int i=0; i<N; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				for(int j=0; j<N; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
					if(map[i][j] == 1) {
						if(i==0 || j==0 || i==N-1||j==N-1) continue;
						cores.add(new int[] {i, j});
					}
				}
			}
			
			isConnected = 0; sizeOfLine = 0; maxConnected = 0; ans = 0;
			solve(0);
			
			sb.append("#").append(tc).append(" ").append(ans).append("\n");
		}
		
		System.out.println(sb.toString());
		br.close();
	}
	
	static void solve(int start) {
		if(isConnected>maxConnected || (isConnected==maxConnected && sizeOfLine<ans)) { // 연결된 코어수가 더 많거나, 같은 경우 전선길이가 더 짧은 경우
			maxConnected = isConnected;
			ans = sizeOfLine;
		}
		
		for(int i=start; i<cores.size(); i++) {  // 코어의 개수만큼 반복
			if (cores.get(i)[0] == 0 || cores.get(i)[0] == N-1 || cores.get(i)[1] == 0 || cores.get(i)[1] == N-1) {  // 가장자리에 있는 코어는 연결될 수 있음
				isConnected++;
				solve(i+1);
				isConnected--;
				continue;
			}
			
			for(int d=0; d<4; d++) {  // 4방향으로 전선 연결
				int nx = cores.get(i)[0], ny = cores.get(i)[1];  // 현재 코어 위치
				boolean flag = true;                             // 전선 연결 가능한지 확인
				while(isValid(nx+dx[d], ny+dy[d])) {  // 전선 연결 가능한지 확인
					nx += dx[d];
					ny += dy[d];
					if(map[nx][ny] != 0) {  // 전선이나 코어가 있으면 전선 연결 불가  -> 전선 연결 해제
						int tempX = cores.get(i)[0] + dx[d], tempY = cores.get(i)[1] + dy[d];
						while(!(tempX==nx && tempY==ny)) {
							map[tempX][tempY] = 0;
							sizeOfLine--;
							tempX += dx[d];
							tempY += dy[d];
						}
						flag = false;  // 전선 연결 불가능
						break;         // 전선 연결 불가능하면 다음 방향으로
					}
					map[nx][ny] = 2; // 2: 전선
					sizeOfLine++;
				}
				if (flag == false) continue;  // 전선 연결 불가능하면 다음 코어로
				isConnected++;				// 전선 연결 가능하면 연결된 코어수 증가			
				solve(i+1);                   // 다음 코어로
				nx = cores.get(i)[0]; ny = cores.get(i)[1];  // 다시 현재 코어 위치로
				while(isValid(nx+dx[d], ny+dy[d])) {         // 전선 연결 해제
					nx += dx[(d)];
					ny += dy[(d)];
					map[nx][ny] = 0;
					sizeOfLine--;
				}
				isConnected--;
				
			}
		}
	}
	
	static boolean isValid(int x, int y) {
		return 0<=x&&x<N && 0<=y&&y<N;
	}
}
