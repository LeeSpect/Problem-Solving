import java.io.*;
import java.util.*;

public class B3_20361_일우는야바위꾼{
	public static void main(String[] args) throws Exception{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine(), " ");
		int N=Integer.parseInt(st.nextToken());
		int X=Integer.parseInt(st.nextToken());
		int K=Integer.parseInt(st.nextToken());
		
		for(int i=0; i<K; i++){
			st=new StringTokenizer(br.readLine(), " ");
			int A=Integer.parseInt(st.nextToken());
			int B=Integer.parseInt(st.nextToken());
			if(A==X) X=B;
			else if(B==X) X=A;
		
			
		}
		System.out.println(X);
		br.close();
	}
}
