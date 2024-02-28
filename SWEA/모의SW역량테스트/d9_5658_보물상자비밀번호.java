import java.io.*;
import java.util.*;

public class d9_5658_보물상자비밀번호{
	static int N, K;
	public static void main(String[] args) throws Exception{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb=new StringBuilder();
		StringTokenizer st;
		
		int T=Integer.parseInt(br.readLine());
		for(int tc=1; tc<T+1; tc++){
			st=new StringTokenizer(br.readLine(), " ");
			N=Integer.parseInt(st.nextToken());
			K=Integer.parseInt(st.nextToken());
			
			String string = br.readLine();
			int size = string.length();
			string += string;
			HashSet<Integer> set = new HashSet<>();
			for(int i=0; i<size+(size/4); i++){
				String target = string.substring(i, i+size/4);
				set.add(-Integer.parseInt(target, 16));
			}
			PriorityQueue<Integer> pq = new PriorityQueue<>(set);
			for(int i=0; i<K-1; i++){
				pq.poll();
			}
			sb.append("#").append(tc).append(" ").append(-pq.poll()).append("\n");
		}
		System.out.println(sb.toString());
		br.close();
	}
}
