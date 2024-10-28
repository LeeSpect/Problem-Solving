package Baekjoon.Gold2;

import java.io.*;
import java.util.*;

public class G2_1938_통나무옮기기_이주형{
	public static void main(String[] args) throws Exception{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb=new StringBuilder();
		HashSet<Train> visited = new HashSet<>();
		int[] dx={-1,-1,-1,0,0,1,1,1}, dy={-1,0,1,-1,1,-1,0,1};
		
		int N=Integer.parseInt(br.readLine());
		char[][] map=new char[N][N];
		Train train = new Train();
		train.score = 0;
		int cnt=0;
		for(int i=0; i<N; i++){
			String line = br.readLine();
			for(int j=0; j<N; j++){
				map[i][j] = line.charAt(j);
				if(map[i][j]=='B'){
					switch(cnt){
						case 0: train.x1=i; train.y1=j; cnt++; break;
						case 1: train.x2=i; train.y2=j; cnt++; break;
						case 2: train.x3=i; train.y3=j; cnt++; break;
					}
				}
			}
		}
		
		// idx0:x idx1:y idx2:횟수
		Queue<Train> que = new PriorityQueue<>((o1, o2) -> Integer.compare(o1.score, o2.score));
		que.offer(train);
		visited.add(train);
		Loop: while(!que.isEmpty()){
			Train temp = que.poll();
			if(map[temp.x1][temp.y1]=='E' && map[temp.x2][temp.y2]=='E' && map[temp.x3][temp.y3]=='E'){
				System.out.println(temp.score);
				return;
			}
			//1 up
			if(temp.x1-1>=0 && map[temp.x1-1][temp.y1]!='1' &&
			   temp.x2-1>=0 && map[temp.x2-1][temp.y2]!='1' &&
			   temp.x3-1>=0 && map[temp.x3-1][temp.y3]!='1'){
				Train nextTrain = new Train(temp.x1-1, temp.x2-1, temp.x3-1, temp.y1, temp.y2, temp.y3, temp.score+1);
				if(!visited.contains(nextTrain)){
					que.offer(nextTrain);
					visited.add(nextTrain);
				}
			}
			//2down
			if(temp.x1+1<N && map[temp.x1+1][temp.y1]!='1' &&
			   temp.x2+1<N && map[temp.x2+1][temp.y2]!='1' &&
			   temp.x3+1<N && map[temp.x3+1][temp.y3]!='1'){
				Train nextTrain = new Train(temp.x1+1, temp.x2+1, temp.x3+1, temp.y1, temp.y2, temp.y3, temp.score+1);
				if(!visited.contains(nextTrain)){
					que.offer(nextTrain);
					visited.add(nextTrain);
				}
			}
			//3left
			if(temp.y1-1>=0 && map[temp.x1][temp.y1-1]!='1' &&
			   temp.y2-1>=0 && map[temp.x2][temp.y2-1]!='1' &&
			   temp.y3-1>=0 && map[temp.x3][temp.y3-1]!='1'){
				Train nextTrain = new Train(temp.x1, temp.x2, temp.x3, temp.y1-1, temp.y2-1, temp.y3-1, temp.score+1);
				if(!visited.contains(nextTrain)){
					que.offer(nextTrain);
					visited.add(nextTrain);
				}
			}
			//4right
			if(temp.y1+1<N && map[temp.x1][temp.y1+1]!='1' &&
			   temp.y2+1<N && map[temp.x2][temp.y2+1]!='1' &&
			   temp.y3+1<N && map[temp.x3][temp.y3+1]!='1'){
				Train nextTrain = new Train(temp.x1, temp.x2, temp.x3, temp.y1+1, temp.y2+1, temp.y3+1, temp.score+1);
				if(!visited.contains(nextTrain)){
					que.offer(nextTrain);
					visited.add(nextTrain);
				}
			}
			//5Turn
			//check
			for(int d=0; d<8; d++){
				int nx=temp.x2+dx[d];
				int ny=temp.y2+dy[d];
				if(0>nx || 0>ny || nx>N-1 || ny>N-1 || map[nx][ny]=='1') continue Loop;
			}
			Train nextTrain = new Train(temp.x2, temp.x2, temp.x2, temp.y2-1, temp.y2, temp.y2+1, temp.score+1);
			if(!visited.contains(nextTrain)){
				que.offer(nextTrain);
				visited.add(nextTrain);
			}
			Train nextTrain2 = new Train(temp.x2-1, temp.x2, temp.x2+1, temp.y2, temp.y2, temp.y2, temp.score+1);
			if(!visited.contains(nextTrain2)){
				que.offer(nextTrain2);
				visited.add(nextTrain2);
			}
		}
		System.out.println(0);
		br.close();
	}
	
	static class Train{
		int x1,x2,x3,y1,y2,y3,score;

		public Train() {}
		public Train(int x1, int x2, int x3, int y1, int y2, int y3, int score) {
			this.x1 = x1;
			this.x2 = x2;
			this.x3 = x3;
			this.y1 = y1;
			this.y2 = y2;
			this.y3 = y3;
			this.score = score;
		}

		@Override
		public int hashCode() {
			return Objects.hash(x1, x2, x3, y1, y2, y3);
		}
		
		@Override
		public boolean equals(Object obj) {
			if (this == obj)
				return true;
			if (obj == null)
				return false;
			if (getClass() != obj.getClass())
				return false;
			Train other = (Train) obj;
			return x1 == other.x1 && x2 == other.x2 && x3 == other.x3 && y1 == other.y1 && y2 == other.y2
					&& y3 == other.y3;
		}
	}
}
