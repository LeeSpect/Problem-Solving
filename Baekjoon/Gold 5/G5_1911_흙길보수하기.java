package a0221;

import java.io.*;
import java.util.*;

public class G5_1911_흙길보수하기 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int answer = 0;
		int N = Integer.parseInt(st.nextToken());
		int L = Integer.parseInt(st.nextToken());

		// 물웅덩이 위치 저장
		int[] waters = new int[2*N];

		for(int i=0; i<N; i++){
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			waters[i] = start; // 시작점
			waters[i+1] = end; // 끝점
		}

		// 정렬해도 상관 없다. 입력에서 물웅덩이 위치가 겹치는 범위는 없으므로
		Arrays.sort(waters); // 오름차순 정렬

		// 널빤지의 가장 마지막 위치를 기억한다.
		int lastIdx = 0; // 널빤지의 가장 마지막 위치

		for(int i=0; i<2*N; i+=2){ // 물웅덩이의 시작점과 끝점을 순서대로 탐색
			int start = waters[i]; // 시작점

			// 이미 물웅덩이에 널빤지가 존재한다면,
			// 시작점을 널빤지의 가장 마지막 위치 + 1로 잡는다.
			if (lastIdx >= start) {
				start = lastIdx + 1; // 널빤지의 가장 마지막 위치 + 1
			}
			int end = waters[i+1];    // 끝점
			int length = end - start; // 널빤지 길이

			// 이미 널빤지가 대져있을 수도 있기 때문에, 이런 경우는 continue
			if (length <= 0) continue;

			// 널빤지 개수
			int cnt = length / L;

			//널빤지 대고 남는 부분
			int res = length % L;

			// 남는 부분이 있으면, 널빤지 개수를 1 증가시키고 마지막 널빤지 위치를 구한다.
			if(res != 0) {
				cnt++; // 널빤지 개수 증가
				lastIdx = waters[i+1]-1 + (L - res); // 마지막 널빤지 위치
			}

			// 답에 카운트 더하기
			answer += cnt;
		}
		System.out.println(answer);
	}
}
