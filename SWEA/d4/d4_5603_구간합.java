import java.io.*;
import java.util.*;

public class d4_5603_구간합{
	static HashMap<Long, Long> f=new HashMap<>();
	
	public static void main(String[] args) throws Exception{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb=new StringBuilder();
		StringTokenizer st;
		
		long sum = 0;
		for(long i=0; i<10; i++) {
			sum += i;
			f.put(i, sum);
		}
		
		int T=Integer.parseInt(br.readLine());
		long A, B, ans;
		for(int tc=1; tc<T+1; tc++){
			st=new StringTokenizer(br.readLine(), " ");
			A=Long.parseLong(st.nextToken());
			B=Long.parseLong(st.nextToken());
			
			if(A > 0) ans = getF(B) - getF(A-1);
			else ans = getF(B) - getF(A);

			sb.append("#").append(tc).append(" ").append(ans).append("\n");
		}
		br.close();
		System.out.println(sb.toString());
	}
	
	static long getV(long n){
		long v = 1;
		while(n>=10){
			v *= 10;
			n /= 10;
		}
		return v;
	}
	
	static long getF(long n){
		if(f.containsKey(n)) return f.get(n);
		if(n<10) return f.get(n);
		
		long v = getV(n);
		long ff = getF(n-1-n%v);
		long g = (n/v)*(n%v+1) + getF(n%v);
		long ans = ff + g;
		
		f.put(n, ans);
		return ans;
	}
}
