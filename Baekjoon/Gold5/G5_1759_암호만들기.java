package Baekjoon.Gold5;

import java.io.*;
import java.util.*;

public class G5_1759_암호만들기{
	static int L, C, cntVowel, cntCons, minVowel=1, minCons=2;
	static char[] alphaArray, ansArray, vowels={'a','e','i','o','u'};
	static boolean[] visited;
	static StringBuilder sb;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		sb = new StringBuilder();
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine(), " ");
		L=Integer.parseInt(st.nextToken());
		C=Integer.parseInt(st.nextToken());
		alphaArray = new char[C];
		st=new StringTokenizer(br.readLine(), " ");
		for(int i=0; i<C; i++) alphaArray[i]=st.nextToken().charAt(0);
		Arrays.sort(alphaArray);
		ansArray = new char[L];
		visited = new boolean[C];
		solve(0, 0);
		
		System.out.println(sb.toString());
		br.close();
	}
	
	static void solve(int cnt, int start){
		if(cnt == L){
			if(minVowel <= cntVowel && minCons <= cntCons){
				for(char c:ansArray) sb.append(c);
				sb.append("\n");
			}
			return;
		}
		for(int i=start; i<C; i++){
			if(visited[i]) continue;
			visited[i]=true;
			ansArray[cnt] = alphaArray[i];
			
			boolean isVowel = false;
			for(char vowel:vowels){
				if(vowel==ansArray[cnt]){
					isVowel = true;
					break;
				}
			}

			if(isVowel) cntVowel++;
			else cntCons++;
			solve(cnt+1, i+1);
			if(isVowel) cntVowel--;
			else cntCons--;
			visited[i]=false;
		}
	}
}
