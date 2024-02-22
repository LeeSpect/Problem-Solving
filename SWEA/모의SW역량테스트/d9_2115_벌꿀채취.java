package a0222;

import java.io.*;
import java.util.*;

public class d9_2115_벌꿀채취 {
	static int x2cri, y2cri, honey1, honey2, ans, max, N, M, C, temp;
	static boolean[] v;
	static int[] arr, al;
	static int[][] map;
	
	static void subs(int cnt, String str, int startX, int startY){
		if(cnt==M){
			arr = new int[str.length()];
			for(int i=0; i<str.length(); i++) arr[i]=str.charAt(i)-'0';
			int temp = getHoney(startX, startY);
			if(max<temp) max=temp;
			return;
		}
		if(v[cnt]) return;
		v[cnt] = true;
		subs(cnt+1, str+al[cnt], startX, startY);
		v[cnt] = false;
		subs(cnt+1, str, startX, startY);
	}

	static int getHoney(int startX, int startY){
		int cnt = 0;
		int honeyValue = 0;
		for(int a:arr) {
			cnt += map[startX][startY+a];
			honeyValue += map[startX][startY+a]*map[startX][startY+a];
		}
		if(cnt > C) return 0;
		return honeyValue;
	}

	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("res/input_d9_2115.txt"));
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb=new StringBuilder();
		StringTokenizer st;

		int T=Integer.parseInt(br.readLine());
		for(int tc=1; tc<T+1; tc++){
			st=new StringTokenizer(br.readLine(), " ");
			N=Integer.parseInt(st.nextToken());
			M=Integer.parseInt(st.nextToken());
			C=Integer.parseInt(st.nextToken());
			
			map=new int[N][N];
			for(int i=0; i<N; i++){
				st=new StringTokenizer(br.readLine(), " ");
				for(int j=0; j<N; j++) map[i][j]=Integer.parseInt(st.nextToken());
			}

			al = new int[M];
			for(int i=0; i<M; i++) al[i]=i;
			v= new boolean[M];
			ans=0;
			Loop1:
			for(int x1=0; x1<N; x1++){
				for(int y1=0; y1<N-M+1; y1++){
					//농부2의 시작점 잡기
					x2cri=x1; y2cri=y1+M+1;
					//만약 다음 농부가 같은 행에서 채취할 수 없는 경우
					if(y2cri > N-1) {
						x2cri++; // 농부2는 다음 행으로
						y2cri=0;
					}
					// 다음 행이 범위를 벗어난다면
					if(x2cri > N-1) continue Loop1; // 농부1의 다음 위치로
					
					//농부1의 꿀 채취
					max=0;
					temp = 0;
					for(int y=y1; y<y1+M; y++) temp+= map[x1][y];
					if(temp <= C) for(int y=y1; y<y1+M; y++) max += map[x1][y]*map[x1][y];
					else subs(0, "", x1, y1);
					honey1=max;
					
					//농부2의 위치 선정
					for(int x2=x2cri; x2<N; x2++){
						int tempY=0;
						if(x1==x2) tempY=y2cri;

						for(int y2=tempY; y2<N-M+1; y2++){
							//농부2의 꿀 채취
							max=0;
							temp=0;
							for(int y=y2; y<y2+M; y++) temp+=map[x2][y];
							if(temp <= C) for(int y=y2; y<y2+M; y++) max+= map[x2][y]*map[x2][y];
							else subs(0, "", x2, y2);
							honey2=max;
							if(honey1+honey2 > ans) ans = honey1+honey2;
						}
					}
				}
			}
			sb.append("#").append(tc).append(" ").append(ans).append("\n");
		}
		System.out.println(sb.toString());
		br.close();
	}
}
