package a0215;

import java.io.*;
import java.util.*;

public class d3_1873_상호의배틀필드 {
	static int H, W;
	static int[] dx = {-1,1,0,0}, dy= {0,0,-1,1};
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<T+1; tc++) {
			st = new StringTokenizer(br.readLine(), " ");
			H = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());
			
			char[][] map = new char[H][W];
			Player player = new Player();
			for(int i=0; i<H; i++) {
				String string = br.readLine();
				for(int j=0; j<W; j++) {
					map[i][j] = string.charAt(j);
					if(map[i][j] != '.' && map[i][j] != '*' && map[i][j] !='#' && map[i][j] != '-') {
						player.x=i; player.y=j;
						if(map[i][j] == '^') player.dir =0;
						else if(map[i][j] == 'v') player.dir=1;
						else if(map[i][j] == '<') player.dir=2;
						else player.dir=3;
					}
				}
			}
			int N = Integer.parseInt(br.readLine());
			String commands = br.readLine();
			for(int n=0; n<N; n++) {
				char command = commands.charAt(n);
				if(command == 'S') {
					int nx = player.x + dx[player.dir], ny = player.y + dy[player.dir];
					while(isValid(nx, ny)) {
						if(map[nx][ny] == '*') {
							map[nx][ny] = '.';
							break;
						} else if(map[nx][ny] == '#') break;
						nx += dx[player.dir];
						ny += dy[player.dir];
					}
				} else {
					if(command == 'U') player.dir = 0;
					else if(command == 'D') player.dir=1;
					else if(command == 'L') player.dir=2;
					else player.dir=3;
					if(player.dir == 0)	map[player.x][player.y] = '^';  
					else if(player.dir == 1) map[player.x][player.y] = 'v';  
					else if(player.dir == 2) map[player.x][player.y] = '<';  
					else map[player.x][player.y] = '>';
					if(isValid(player.x+dx[player.dir], player.y+dy[player.dir]) && map[player.x+dx[player.dir]][player.y+dy[player.dir]] == '.') {
						map[player.x][player.y]='.'; 
						player.x += dx[player.dir];
						player.y += dy[player.dir];
						if(player.dir == 0)	map[player.x][player.y] = '^';  
						else if(player.dir == 1) map[player.x][player.y] = 'v';  
						else if(player.dir == 2) map[player.x][player.y] = '<';  
						else map[player.x][player.y] = '>';  
					}
				}
			}
			sb.append("#").append(tc).append(" ");
			for(int i=0; i<H; i++) {
				for(int j=0; j<W; j++) sb.append(map[i][j]);
				sb.append("\n");
			}
		}
		System.out.println(sb.toString());
		br.close();
	}
	
	static boolean isValid(int x, int y) {
		return 0<=x&&x<H && 0<=y&&y<W;
	}
	
	static class Player{
		int x,y,dir;
	}
}
