package a0214;

import java.io.*;
import java.util.*;

public class S1_1992_쿼드트리 {
	static String[] map;
	static StringBuilder sb;

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		sb = new StringBuilder();
		
		int N = Integer.parseInt(br.readLine());
		map = new String[N];
		for(int i=0; i<N; i++) map[i] = br.readLine();
		
		check(0, 0, N);
		
		System.out.println(sb.toString());
		br.close();
	}
	
	static void check(int x, int y, int range) {
		for(int i=x; i<x+range; i++) {
			for(int j=y; j<y+range; j++) {
				if(map[i].charAt(j) != map[x].charAt(y)) {
					
					sb.append("(");
					check(x, y, range/2);
					check(x, y+range/2, range/2);
					check(x+range/2, y, range/2);
					check(x+range/2, y+range/2, range/2);
					sb.append(")");
					return;
				}
			}
		}
		sb.append(map[x].charAt(y));
	}
	
	
}
