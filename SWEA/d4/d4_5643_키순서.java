package a0403;

import java.io.*;
import java.util.*;

public class d4_5643_키순서{
	static int N;
	static List<Integer>[][] upDown;
	static boolean[] visited;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int M, temp1, temp2;
		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<T+1; tc++){
			N=Integer.parseInt(br.readLine());
			M=Integer.parseInt(br.readLine());
			upDown=new List[N][2];
			for(int i=0; i<N; i++) for(int j=0; j<2; j++) upDown[i][j]=new ArrayList<>();
			
			for(int i=0; i<M; i++){
				st=new StringTokenizer(br.readLine(), " ");
				temp1=Integer.parseInt(st.nextToken())-1;
				temp2=Integer.parseInt(st.nextToken())-1;
				upDown[temp1][1].add(temp2);
				upDown[temp2][0].add(temp1);
			}
			
			int ans = 0;
			for(int i=0; i<N; i++) if(isKnown(i)) ans += 1;
			
			sb.append("#").append(tc).append(" ").append(ans).append("\n");
		}
		System.out.println(sb.toString());
		br.close();
	}
	
	static boolean isKnown(int i){
		visited=new boolean[N];
		visited[i]=true;
		int cnt=1;
		Queue<Integer> deq=null;
		cnt = check(deq, i, 0, cnt);
		cnt = check(deq, i, 1, cnt);
		return cnt==N ? true:false;
	}
	
	static int check(Queue<Integer> deq, int i, int flag, int cnt){
		deq=new ArrayDeque<>();
		deq.offer(i);
		while(!deq.isEmpty()){
			int node=deq.poll();
			for(int parent:upDown[node][flag]){
				if(!visited[parent]){
					visited[parent]=true;
					deq.offer(parent);
					cnt++;
				}
			}
		}
		return cnt;
	}
}
