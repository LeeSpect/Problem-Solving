import java.io.*;
import java.util.*;

public class G4_21939_문제추천시스템Version1{
	static TreeSet<Problem> problems = new TreeSet<>();
	static Problem[] problemArr;
	public static void main(String[] args) throws Exception{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb=new StringBuilder();
		StringTokenizer st;
		
		int N=Integer.parseInt(br.readLine());
		problemArr = new Problem[100001];
		for(int i=0; i<N; i++){
			st=new StringTokenizer(br.readLine(), " ");
			Problem problem = new Problem(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
			problems.add(problem);
			problemArr[problem.idx]= problem; 
		}
		
		int M=Integer.parseInt(br.readLine());
		String command;
		for(int i=0; i<M; i++){
			st=new StringTokenizer(br.readLine(), " ");
			command = st.nextToken();
			switch(command){
				case "recommend": sb.append(recommend(Integer.parseInt(st.nextToken()))).append("\n"); break;
				case "add": add(new Problem(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()))); break;
				case "solved": solved(Integer.parseInt(st.nextToken())); break;
			}
		}
		System.out.println(sb.toString());
		br.close();
	}
	
	static int recommend(int x){
		if(x==1) return problems.last().idx;
		else return problems.first().idx; 
	}
	
	static void add(Problem problem){
		problems.add(problem);
		problemArr[problem.idx]=problem;
	}
	
	static void solved(int i){
		problems.remove(problemArr[i]);
		problemArr[i]=null;
	}
	
	static class Problem implements Comparable<Problem>{
		int idx; int diff;
		Problem(int idx, int diff){
			this.idx=idx;this.diff=diff;
		}
		@Override
		public int compareTo(Problem o) {
			return this.diff!=o.diff ? Integer.compare(this.diff, o.diff):Integer.compare(this.idx, o.idx);
		}
		@Override
		public int hashCode() {
			return 0;
		}
		@Override
		public boolean equals(Object obj) {
			if (this == obj)
				return true;
			if (obj == null)
				return false;
			if (getClass() != obj.getClass())
				return false;
			Problem other = (Problem) obj;
			return diff == other.diff && idx == other.idx;
		}
	}
}
