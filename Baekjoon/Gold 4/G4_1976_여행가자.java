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
            for(int isConnected:graph[currentNode]){
                if(isConnected==1 && !visited[neighbor]){
                    visited[neighbor] = true;
                    deq.offer(neighbor);
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

        int startCity = travelPlan[0] - 1;
        bfs(startCity);

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
