import java.io.*;
import java.util.*;

public class S1_1149_RGB거리{
	public static void main(String[] args) throws Exception{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N=Integer.parseInt(br.readLine());
		int[] dp = new int[3];
		st=new StringTokenizer(br.readLine(), " ");
		for(int i=0; i<3; i++){
			dp[i] = Integer.parseInt(st.nextToken());
		}
		
		int a, b, c;
		int[] newDP = new int[3];
		for(int n=0; n<N-1; n++){
			st=new StringTokenizer(br.readLine(), " ");
			a=Integer.parseInt(st.nextToken());
			b=Integer.parseInt(st.nextToken());
			c=Integer.parseInt(st.nextToken());
			
			newDP[0] = dp[1]>dp[2] ? a+dp[2] : a+dp[1];
			newDP[1] = dp[0]>dp[2] ? b+dp[2] : b+dp[0];
			newDP[2] = dp[0]>dp[1] ? c+dp[1] : c+dp[0];
			for(int i=0; i<3; i++) dp[i] = newDP[i];
		}
		
		System.out.println(Math.min(Math.min(dp[0], dp[1]), dp[2]));
		br.close();
	}
}
