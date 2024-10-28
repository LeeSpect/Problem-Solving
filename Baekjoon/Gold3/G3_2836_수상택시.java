import java.io.*;
import java.util.*;

public class Main {
    static class Point extends Comparable<Point>{
        int start, end, no;
        public Point(int start, int end, int no) {
            this.start = start;
            this.end = end;
            this.no = no;
        }

        @Override
        public int compareTo(Point o) {
            return Integer.compare(this.end, o.end);
        }
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N, M;
        int[][] points;

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        points = new int[N][2];
        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            points[i][0] = Integer.parseInt(st.nextToken());
            points[i][1] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(points, (p1, p2) ->
                p1[0]==p2[0] ? Integer.compare(p1[1], p2[1]) : Integer.compare(p1[0], p2[0]));

        int now = 0;
        int ans = 0;
        PriorityQueue<Point> boat = new PriorityQueue<>();
        boat.offer(new Point(0, M, 0));
        for(int i=1; i<N+1; i++){
            Point point = new Point(points[i-1][0], points[i-1][1], i);
            if(boat.peek().end <= point.start){
                while(boat.peek().end <= point.start){

                }
            }

            if(point.start < boat.peek().end){
                ans += boat.peek().start - now;
                now = point.start;
                boat.offer(point);
            }else{
                while(point.start < )
            }
        }
    }

}
