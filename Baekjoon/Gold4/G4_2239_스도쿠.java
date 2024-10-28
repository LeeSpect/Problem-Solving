package a0327;

import java.util.*;
import java.io.*;

public class G4_2239_스도쿠 {
	static int[][] map = new int[9][9];
	static boolean[][] sudo_r = new boolean[10][10];
	static boolean[][] sudo_c = new boolean[10][10];
	static boolean[][][] sudo_3x3 = new boolean[3][3][10];
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for(int i=0; i<9; i++){
			String string = br.readLine();
			for(int j=0; j<9; j++) map[i][j] = string.charAt(j) - '0';
		}
		
		for(int i=0; i<9; i++){
			for(int j=0; j<9; j++){
				if(map[i][j] != 0){
					sudo_r[i][map[i][j]] = true;
					sudo_c[j][map[i][j]] = true;
					sudo_3x3[i/3][j/3][map[i][j]] = true;
				}
			}
		}
		DFS(0, 0);
		System.out.println(sb.toString());
	}
	
	static void DFS(int r, int c) {
		if(c==9) {
			c = 0;
			r++;
		}
		if(r==9){
			for(int i=0; i<9; i++){
				for(int j=0; j<9; j++) {
					sb.append(map[i][j]);
					System.out.print(map[i][j]);
				}
				System.out.println();
				sb.append("\n");
			}
			System.exit(0);
		}
		if(map[r][c]==0){
			for(int k=1; k<10; k++){
				if(!sudo_r[r][k] && !sudo_c[c][k] && !sudo_3x3[r/3][c/3][k]){
					sudo_r[r][k] = true;
					sudo_c[c][k] = true;
					sudo_3x3[r/3][c/3][k] = true;
					map[r][c] = k;
					map[r][c] = k;
					DFS(r, c+1);
					sudo_r[r][k] = false;
					sudo_c[c][k] = false;
					sudo_3x3[r/3][c/3][k] = false;
					map[r][c] = 0;
				}
			}
		}else{
			DFS(r, c+1);
		}
	}
}




















