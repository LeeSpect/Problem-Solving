import java.io.*;
import java.util.*;

public class G4_15961_회전초밥{
	public static void main(String[] args) throws Exception{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st=new StringTokenizer(br.readLine(), " ");
		int N=Integer.parseInt(st.nextToken());
		int d=Integer.parseInt(st.nextToken());
		int k=Integer.parseInt(st.nextToken());
		int c=Integer.parseInt(st.nextToken());
		
		// 접시 배열
		int[] dishesArr = new int[N];
		for(int i=0; i<N; i++) dishesArr[i] = Integer.parseInt(br.readLine());
		
		int[] sushiArr = new int[d+1];              // 초밥 종류의 개수를 저장할 배열(d:초밥의 가짓수, 초밥의 종류는 1부터 시작)
		int ans = 0;                                // 최대 종류의 초밥 개수
		int count = 0;                              // 현재 선택된 초밥의 종류 개수
		
		// 0번부터 k-1번 까지, K개의 초밥에 대해 종류의 개수를 구한다.
		for(int i=0; i<k; i++) {          
			if(sushiArr[dishesArr[i]] == 0) count++; // 해당 초밥의 개수가 0이라면, 새로운 종류가 추가되는 것이기 때문에, 종류의 개수 증가
			sushiArr[dishesArr[i]]++;                // 해당 초밥의 개수 증가
		}

		// 처음 k개의 초밥에 대한 경우의 수를 ans에 저장
		if(sushiArr[c] == 0) ans = count+1; // 쿠폰 초밥이 없다면, count+1
		else ans = count;                   // 쿠폰 초밥이 있다면, count

		// k개의 초밥을 선택했을 때, 가장 많은 종류의 초밥을 먹을 수 있는 경우의 수를 구한다.
		for(int i=1; i<N; i++) {
			// 맨 앞에 있는 초밥을 제거
			sushiArr[dishesArr[i-1]]--;
			if(sushiArr[dishesArr[i-1]] == 0) count--; // 해당 초밥의 개수가 0이라면, 종류의 개수 감소
			
			// 맨 뒤에 있는 초밥을 추가
			if(sushiArr[dishesArr[(i+k-1)%N]] == 0) count++; // 해당 초밥의 개수가 0이라면, 종류의 개수 증가
			sushiArr[dishesArr[(i+k-1)%N]]++;                // 해당 초밥의 개수 증가
			
			// 현재 선택된 초밥의 종류 개수가 ans보다 크다면, ans에 저장
			if(sushiArr[c] == 0) ans = Math.max(ans, count+1); // 쿠폰 초밥이 없다면, count+1
			else ans = Math.max(ans, count);                   // 쿠폰 초밥이 있다면, count
		}

		System.out.println(ans);
		
		br.close();
	}
}
