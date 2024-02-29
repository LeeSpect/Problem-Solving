import java.io.*;
import java.util.*;

public class S2_10971_외판원순회2{
    static int N;
    static int[][] W;
    static boolean[] visited;
    static int minCost = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception{
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st;
    	
        N = Integer.parseInt(br.readLine());
        W = new int[N][N];          // 도시 간 이동 비용(도시i -> 도시j 비용)
        visited = new boolean[N];

        for(int i=0; i<N; i++){
        	st=new StringTokenizer(br.readLine(), " ");
            for(int j=0; j<N; j++) W[i][j] = Integer.parseInt(st.nextToken());
        }

        // 최소 비용으로 순회하기 때문에 어느 지점에서 출발해도 경로가 동일 => 시작도시 0으로 설정
        // 1->2->3->1
        // 2->3->1->2
        // 3->1->2->3
        
        visited[0] = true;          // 시작 도시 방문 표시
        solve(0, 0, 0, 1);          // 시작 도시에서 시작, 비용 0, 시작 도시, 1개의 도시 방문
        System.out.println(minCost);
        br.close();
    }

    // current: 현재 도시, cost: 현재까지 비용, startCity: 시작 도시, depth: 방문한 도시 수
    static void solve(int current, int cost, int startCity, int depth){
        if(cost > minCost) return;                                        // 현재까지 비용이 최소 비용보다 크면 return(가지치기): 백트래킹
        if(depth == N){
            if(W[current][startCity] != 0){                               // 마지막 도시에서 시작 도시로 돌아갈 수 있는 경우
                minCost = Math.min(minCost, cost + W[current][startCity]);// 최소 비용 갱신
            }
            return;
        }

        for(int i=0; i<N; i++){                                           // 모든 도시에 대해
            if(!visited[i] && W[current][i] != 0){                        // 아직 방문하지 않았고, 갈 수 있는 도시인 경우
                visited[i] = true;
                solve(i, cost + W[current][i], startCity, depth + 1);     // 다음 도시로 이동: DFS
                visited[i] = false;                                       // false: 다른 경로로 방문할 수 있도록
            }
        }
    }
}
