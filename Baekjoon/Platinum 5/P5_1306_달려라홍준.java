// 182544KB, 792ms

import java.io.*;
import java.util.*;

public class P5_1306_달려라홍준{
	static int[] numbers, tree;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb=new StringBuilder();
		StringTokenizer st=new StringTokenizer(br.readLine(), " ");
		
		int N=Integer.parseInt(st.nextToken());
		int M=Integer.parseInt(st.nextToken());
		
		int tmp = (int)Math.ceil(Math.log(N)/Math.log(2)) +1;
		int h = (int)Math.pow(2,  tmp);
		
		numbers = new int[h];
		tree = new int[h];
		st=new StringTokenizer(br.readLine(), " ");
		for(int i=1; i<N+1; i++) {
			numbers[i]=Integer.parseInt(st.nextToken());
		}
		init(1, 1, N);
		
		int arr;
		for(int m=M; m<N-M+2; m++){
			arr=query(1, 1, N, m-M+1, m+M-1);
//			System.out.println(arr);
			sb.append(arr).append(" ");
		}
		System.out.println(sb.toString());
	}
	
	static void init(int node, int start, int end){
		if(start==end) {
			tree[node] = numbers[start];
		}
		else{
			init(node*2, start, (start+end)/2);
			init(node*2+1, (start+end)/2+1, end);
			tree[node] = Math.max(tree[node*2], tree[node*2+1]);
		}
	}
	
	static int query(int node, int start, int end, int left, int right){
		if(start > right || left > end) return -1;
		if(left <= start && end <= right) return tree[node];
		
		int leftRe = query(node*2, start, (start+end)/2, left, right);
		int rightRe = query(node*2+1, (start+end)/2+1, end, left, right);
		
		int re = Math.max(leftRe, rightRe);
		return re;
	}
}