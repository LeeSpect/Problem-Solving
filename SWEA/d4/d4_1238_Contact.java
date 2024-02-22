import java.io.*;
import java.util.*;

public class d4_1238_Contact{
	public static void main(String[] args) throws Exception{
//		System.setIn(new FileInputStream("res/input_d4_1238.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int T=10;
		Node[] nodes;
		boolean[] visited;
		
		for(int tc=1; tc<T+1; tc++){
			st=new StringTokenizer(br.readLine(), " ");
			int L=Integer.parseInt(st.nextToken());
			int start=Integer.parseInt(st.nextToken());
			nodes=new Node[101];
			visited=new boolean[101];
			
			st=new StringTokenizer(br.readLine(), " ");
			for(int l=0; l<L/2; l++){
				int from=Integer.parseInt(st.nextToken());
				int to=Integer.parseInt(st.nextToken());
				nodes[from]=new Node(to, nodes[from]);
			}
			ArrayDeque<Integer> deq = new ArrayDeque<>();
			visited[start] = true;
			deq.offer(start);
			Integer[] arr = new Integer[0];
			while(!deq.isEmpty()){
				arr = deq.toArray(new Integer[0]);
				int size=deq.size();
				for(int s=0; s<size; s++){
					int temp=deq.poll();
					for(Node node=nodes[temp]; node!=null; node=node.link){
						if(!visited[node.vertex]){
							visited[node.vertex]=true;
							deq.offer(node.vertex);
						}
					}
				}
			}
			int max=0;
			for(int i:arr) if(i>max) max = i;
			
			sb.append("#").append(tc).append(" ").append(max).append("\n");
		}
		System.out.println(sb.toString());
		br.close();
	}
	
	static class Node{
		int vertex;
		Node link;
		Node(int vertex, Node link){
			this.vertex=vertex;this.link=link;
		}
	}
}
