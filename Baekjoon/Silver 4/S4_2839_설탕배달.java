package a0213;

import java.io.*;
import java.util.*;

public class S4_2839_설탕배달 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		System.out.println(sugar(N));
	}
	
	static int sugar(int N) {
		int k = N/5;
		for(int i=k; -1<i; i--) {
			if((N-5*i) % 3 == 0) return i+(N-5*i)/3;
		}
		return -1;
	}
}
