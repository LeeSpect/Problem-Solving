// 209896KB 700ms

import java.io.*;
import java.util.*;

public class G1_2357_최솟값과최댓값{
	static long[] numbers;
	static long[][] tree;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb=new StringBuilder();
		StringTokenizer st=new StringTokenizer(br.readLine(), " ");
		
		
		int N=Integer.parseInt(st.nextToken());
		int M=Integer.parseInt(st.nextToken());
		
		int tmp = (int)Math.ceil(Math.log(N)/Math.log(2)) +1;
		int h = (int)Math.pow(2,  tmp);
		
		numbers = new long[h];
		tree = new long[h][2];  // idx0:최소, idx1:최대
		for(int i=1; i<N+1; i++) {
			numbers[i]=Long.parseLong(br.readLine());
		}
		init(1, 1, N);
		
		int a, b;
		long[] arr;
		for(int m=0; m<M; m++){
			st=new StringTokenizer(br.readLine(), " ");
			a=Integer.parseInt(st.nextToken());
			b=Integer.parseInt(st.nextToken());
			arr=query(1, 1, N, a, b);
			sb.append(arr[0]).append(" ").append(arr[1]).append("\n");
		}
		System.out.println(sb.toString());
	}
	
	static void init(int node, int start, int end){
		if(start==end) {
			tree[node][0] = numbers[start];
			tree[node][1] = numbers[start];
		}
		else{
			init(node*2, start, (start+end)/2);
			init(node*2+1, (start+end)/2+1, end);
			tree[node][0] = Math.min(tree[node*2][0], tree[node*2+1][0]);
			tree[node][1] = Math.max(tree[node*2][1], tree[node*2+1][1]);
		}
	}
	
	static long[] query(int node, int start, int end, int left, int right){
		if(start > right || left > end) return new long[] {1000000001, -1};
		if(left <= start && end <= right) return tree[node];

		long[] re = new long[2];
		
		long[] leftRe = query(node*2, start, (start+end)/2, left, right);
		long[] rightRe = query(node*2+1, (start+end)/2+1, end, left, right);
		
		re[0] = Math.min(leftRe[0], rightRe[0]);
		re[1] = Math.max(leftRe[1], rightRe[1]);
		return re;
	}
	
}