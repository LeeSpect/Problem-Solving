// 11668KB, 72ms

package Baekjoon.Gold5;

import java.util.*;
import java.io.*;

public class G5_1461_도서관 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken()); // 책의 개수
		int m = Integer.parseInt(st.nextToken()); // 한 번에 옮길 수 있는 최대 책 개수

		// 책 위치 정보를 저장할 리스트
		ArrayList<Integer> positive = new ArrayList<>();
		ArrayList<Integer> negative = new ArrayList<>();

		// 입력된 책 위치를 나누어 저장
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<n; i++) {
			int book = Integer.parseInt(st.nextToken());
			if (book > 0) positive.add(book);
			else negative.add(-book); // 음수 좌표를 양수로 저장하여 처리
		}

		// 절대값이 큰 순으로 정렬
		Collections.sort(positive, Collections.reverseOrder());
		Collections.sort(negative, Collections.reverseOrder());

		int totalDistance = 0;

		// 양수 방향에서 가장 멀리 떨어진 책 위치 처리
		for (int i=0; i<positive.size(); i+=m) {
			totalDistance += positive.get(i) * 2; // 왕복 거리
		}

		// 음수 방향에서 가장 멀리 떨어진 책 위치 처리
		for (int i=0; i<negative.size(); i+=m) {
			totalDistance += negative.get(i) * 2; // 왕복 거리
		}

		// 마지막 이동에서 가장 먼 책 위치를 뺌(마지막으로 왕복하지 않음)
		int maxDistance = 0;
		if (!positive.isEmpty() && !negative.isEmpty()) {
			maxDistance = Math.max(positive.get(0), negative.get(0));
		} else if (!positive.isEmpty()) {
			maxDistance = positive.get(0);
		} else if (!negative.isEmpty()) {
			maxDistance = negative.get(0);
		}

		// 총 이동 거리에서 가장 먼 거리를 빼서 최종 결과 출력
		System.out.println(totalDistance - maxDistance);


	}

}