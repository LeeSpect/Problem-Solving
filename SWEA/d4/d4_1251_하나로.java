package a0212;

import java.io.*;
import java.util.*;

public class d4_1251_하나로 {
	static int N;
	static double E;
	static double[][] islands;

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		int T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<T+1; tc++) {
			N = Integer.parseInt(br.readLine());
			islands = new double[N][2];

			st = new StringTokenizer(br.readLine(), " ");
			for(int i=0; i<N; i++) islands[i][0] = Double.parseDouble(st.nextToken());
			st = new StringTokenizer(br.readLine(), " ");
			for(int i=0; i<N; i++) islands[i][1] = Double.parseDouble(st.nextToken());
			E = Double.parseDouble(br.readLine());

			sb.append("#").append(tc).append(" ").append(prim()).append("\n");
		}
		br.close();
		System.out.println(sb.toString());
	}

	static long prim() {
		boolean[] visited = new boolean[N];
		double[] minEdge = new double[N];
		for(int i=0; i<N; i++) minEdge[i] = Double.MAX_VALUE;
		minEdge[0] = 0;
		
		double total = 0;
		// minEdge 배열 정리 (0번 정점에서 각 정점으로 가는 가중치를 저장)
		for(int t=0; t<N; t++) {
			double min = Double.MAX_VALUE; // 최소값 초기화
			int current = -1;              // 최소값을 가진 정점 초기화
			for(int i=0; i<N; i++) {
				if(!visited[i] && minEdge[i] < min) {  // 방문하지 않은 정점 중 최소값 찾기
					min = minEdge[i];      // 최소값 갱신
					current = i;           // 최소값을 가진 정점 갱신
				}
			}
			visited[current] = true; // 방문처리
			total += min;			 // 최소값 누적

			for(int i=0; i<N; i++) {
				if(!visited[i]) {    // 방문하지 않은 정점 중
					double dist = cal(islands[current], islands[i]); // 현재 정점에서 다른 정점까지의 거리 계산
					if(dist < minEdge[i]) { // 현재 정점에서 다른 정점까지의 거리가 minEdge 배열에 저장된 값보다 작으면
						minEdge[i] = dist;  // 최소값 갱신
					}
				}
			}
		}
		return Math.round(total);
	}

	static double cal(double[] a, double[] b) {
		return E * (Math.pow(a[0] - b[0], 2) + Math.pow(a[1] - b[1], 2));
	}
}
