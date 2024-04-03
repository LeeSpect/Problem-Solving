import java.io.*;
import java.util.*;

public class G4_2458_키순서{
	static int N;
	static List<Integer>[][] upDown;
	static boolean[] visited;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st=new StringTokenizer(br.readLine(), " ");
		
		N=Integer.parseInt(st.nextToken());
		int M=Integer.parseInt(st.nextToken());
		upDown=new List[N][2];
		for(int i=0; i<N; i++) for(int j=0; j<2; j++) upDown[i][j]=new ArrayList<>();
		
		int temp1, temp2;
		for(int i=0; i<M; i++){
			st=new StringTokenizer(br.readLine(), " ");
			temp1=Integer.parseInt(st.nextToken())-1;
			temp2=Integer.parseInt(st.nextToken())-1;
			upDown[temp1][1].add(temp2);
			upDown[temp2][0].add(temp1);
		}
		
		int ans = 0;
		for(int i=0; i<N; i++) if(isKnown(i)) ans += 1;
		
		System.out.println(ans);
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
