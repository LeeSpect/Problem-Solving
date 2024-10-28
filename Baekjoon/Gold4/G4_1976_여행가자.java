// 16804 KB, 156 ms
import java.io.*;
import java.util.*;

public class Main {
    static int[][] graph;
    static boolean[] visited;

    static void bfs(int startNode){
        ArrayDeque<Integer> deq = new ArrayDeque<>();
        deq.offer(startNode);
        visited[startNode] = true;

        while(!deq.isEmpty()){
            int currentNode = deq.poll();
            int neighbor=0;
            // 현재 노드에 연결된 모든 이웃 노드를 탐색
            for(int isConnected:graph[currentNode]){
                // 이웃 노드가 연결되어 있고 방문하지 않았다면
                if(isConnected==1 && !visited[neighbor]){
                    visited[neighbor] = true; // 이웃 노드를 방문한 것으로 표시
                    deq.offer(neighbor); // 이웃 노드를 큐에 추가
                }
                neighbor++;
            }
        }
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        graph = new int[N][N];
        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<N; j++){
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        visited = new boolean[N];
        int[] travelPlan = new int[M];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<M; i++) travelPlan[i] = Integer.parseInt(st.nextToken());

        // 시작 도시 설정 (입력된 도시는 1부터 시작하므로 0부터 시작하도록 조정)
        int startCity = travelPlan[0] - 1;
        bfs(startCity);

        // 모든 여행 경로에 대해 방문 가능 여부 확인
        boolean canTravel = true;
        for(int city:travelPlan){
            if(!visited[city - 1]){
                canTravel = false;
                break;
            }
        }
        if(canTravel) System.out.println("YES");
        else System.out.println("NO");
    }
}
