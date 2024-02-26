import java.io.*;
import java.util.*;

public class S3_17952_과제는끝나지않아{
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N=Integer.parseInt(br.readLine());
		
		ArrayDeque<Work> works = new ArrayDeque<>();
		int ans = 0;
		
		for(int time=0; time<N; time++){
			st = new StringTokenizer(br.readLine(), " ");
			int isWork=Integer.parseInt(st.nextToken());
			if(isWork==0) {
				if(!works.isEmpty()) {
					Work work = works.peekLast();
					if(--work.term == 0) ans+=works.pollLast().score;
				}
				continue;
			}
			int score = Integer.parseInt(st.nextToken());
			int term = Integer.parseInt(st.nextToken());
			
			if(term == 1){
				ans += score;
			}else{
				works.offer(new Work(score, term-1, time));
			}
		}
		System.out.println(ans);
		br.close();
	}
	
	static class Work{
		int score, term, minute;
		public Work(int score, int term, int minute) {
			this.score = score;
			this.term = term;
			this.minute = minute;
		}
	}
}
