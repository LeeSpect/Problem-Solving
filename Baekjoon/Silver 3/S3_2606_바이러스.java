import java.io.*;
import java.util.*;

public class S3_2606_바이러스{
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N=Integer.parseInt(br.readLine());
		int M=Integer.parseInt(br.readLine());
		
		int[][] map = new int[N][N];
		ArrayList<ArrayList<Integer>> list = new ArrayList<>();
		for(int i=0; i<N; i++) list.add(new ArrayList<>());
		
		int start, end;
		for(int m=0; m<M; m++){
			st= new StringTokenizer(br.readLine(), " ");
			start = Integer.parseInt(st.nextToken())-1;
			end = Integer.parseInt(st.nextToken())-1;
			list.get(start).add(end); list.get(end).add(start);
		}
		
		ArrayDeque<Integer> deq = new ArrayDeque<>();
		boolean[] visited = new boolean[N];
		deq.offer(0);
		visited[0] = true;
		int cnt = 0;
		while(!deq.isEmpty()){
			int temp = deq.poll();
			for(int node:list.get(temp)){
				if(!visited[node]) {
					visited[node] = true;
					deq.offer(node);
					cnt += 1;
				}
			}
		}
		System.out.println(cnt);
		br.close();
	}
}
