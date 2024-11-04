// 82ms / 10.87MB

import java.io.*;
import java.util.*;

public class Lv2_나무공격 {

	static int suspect = 0;
	static int N, M;
	static int[][] maps;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		maps = new int[N][M];
		for(int n=0; n<N; n++){
			st = new StringTokenizer(br.readLine());
			for(int m=0; m<M; m++){
				maps[n][m] = Integer.parseInt(st.nextToken());
				if(maps[n][m] == 1) suspect++;
			}
		}

		st = new StringTokenizer(br.readLine());
		int L1 = Integer.parseInt(st.nextToken()) - 1;
		int R1 = Integer.parseInt(st.nextToken()) - 1;
		st = new StringTokenizer(br.readLine());
		int L2 = Integer.parseInt(st.nextToken()) - 1;
		int R2 = Integer.parseInt(st.nextToken()) - 1;

		attackSuspects(L1, R1);
		attackSuspects(L2, R2);

		System.out.println(suspect);
	}

	static void attackSuspects(int L, int R){
		for(int l=L; l<R+1; l++){
			for(int m=0; m<M; m++){
				if(maps[l][m] == 1){
					maps[l][m] = 0;
					suspect--;
					break;
				}
			}
		}
	}
}
