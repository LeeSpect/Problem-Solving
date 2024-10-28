// 324,940 KB, 1,768 ms
import java.io.*;
import java.util.*;

public class Main {
    static int[] parents;

    static class Node implements Comparable<Node> {
        int start, end, cost;

        public Node(int start, int end, int cost) {
            this.start = start; this.end = end; this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return Integer.compare(this.cost, o.cost);
        }
    }

    static int find_parents(int node){
        while (parents[node] != node){
            parents[node] = parents[parents[node]];
            node = parents[node];
        }
        return parents[node];
    }

    static boolean Union(int node1, int node2){
        int a, b;
        a = find_parents(node1);
        b = find_parents(node2);
        if(a == b) return false;
        if(a < b) parents[b] = a;
        else parents[a] = b;
        return true;
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        parents = new int[N+1];
        for(int i=0; i<N+1; i++) parents[i] = i;
        PriorityQueue<Node> que = new PriorityQueue<>();
        int A, B, C;
        for(int i=0; i<M; i++){
            st = new StringTokenizer(br.readLine());
            A = Integer.parseInt(st.nextToken());
            B = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());
            que.offer(new Node(A, B, C));
        }

        int weigh = 0;
        int max_cost = 0;
        while(!que.isEmpty()){
            Node node = que.poll();
            if(Union(node.start, node.end)){
                weigh += node.cost;
                max_cost = Math.max(max_cost, node.cost);
            }
        }
        System.out.println(weigh - max_cost);
    }
}