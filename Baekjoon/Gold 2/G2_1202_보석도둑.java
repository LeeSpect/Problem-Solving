import java.io.*;
import java.util.*;

/*
1. 보석을 arraylist로 입력받은 후 무게 순서대로 오름차순 정렬
2. 가방에 담을 수 있는 최대 무게를 입력 받은 후 오름차순 정렬
3. 가격 순서대로 내림차순 정렬을 하는 우선순위 큐를 생성
4. 현재 가방이 담을 수 있는 최대 무게보다 작거나 같은 무게를 가진 보석을 우선순위 큐에 추가
5. 우선순위 큐의 제일 첫 번째 값(가장 가격이 비싼 보석)을 총 가격에 추가
6. 4 ~ 5를 반복 
*/
 
public class 보석{
    public static void main(String[] args) throws Exception{
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st=new StringTokenizer(br.readLine(), " ");
 
        int N=Integer.parseInt(st.nextToken());
        int K=Integer.parseInt(st.nextToken());
        
        List<Gem> list = new ArrayList<>();  // 보석 리스트
        for(int i=0; i < N; i++){
        	st=new StringTokenizer(br.readLine(), " ");
            list.add(new Gem(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }
        Collections.sort(list, (o1, o2) -> Integer.compare(o1.m, o2.m)); //무게순 정렬
        
        int[] weight = new int[K];  // 가방 리스트
        for(int i=0; i<K; i++) weight[i] = Integer.parseInt(br.readLine());
        Arrays.sort(weight); // 무게순 정렬
        
        long total = 0;  // 총 가격
        int listIdx = 0; // 보석 리스트 인덱스
        Queue<Gem> pq = new PriorityQueue<>((o1, o2) -> Integer.compare(o2.v, o1.v)); //가격순 정렬
        for(int i=0; i<K; i++){ // 가방 무게 순으로
            while(listIdx<N && list.get(listIdx).m <= weight[i]){  // 현재 가방에 담을 수 있는 보석들을 pq에 추가
                Gem cur = list.get(listIdx++);  // 현재 보석
                pq.add(new Gem(cur.m, cur.v));  // pq에 추가
            }
            if(!pq.isEmpty()) total += pq.poll().v;  // pq에서 가장 비싼 보석을 빼서 총 가격에 추가
        }
        System.out.println(total);
    }
    
    public static class Gem{
        int m, v;
        public Gem(int m, int v){
            this.m = m; this.v = v;
        }
    }
}