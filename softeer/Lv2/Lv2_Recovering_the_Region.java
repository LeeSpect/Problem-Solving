import java.io.*;
import java.util.*;

public class Lv2_Recovering_the_Region {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		for(int i=1; i<N+1; i++){
			for(int j=0; j<N-1; j++){
				System.out.print(i+" ");
			}
			System.out.println(i);
		}
	}
}
