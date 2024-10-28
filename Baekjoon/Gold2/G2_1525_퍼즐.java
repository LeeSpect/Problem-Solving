package Baekjoon.Gold2;

import java.util.*;
import java.io.*;

public class G2_1525_퍼즐 {

	// 목표 상태인 퍼즐 완성 상태를 문자열로 표현
	static String target = "123456780";

	// 상하좌우 이동을 나타내는 방향 배열
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};

	// 방문한 퍼즐 상태를 저장하여 중복 계산 방지
	static Map<String, Integer> visited = new HashMap<>();

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		// 퍼즐의 시작 상태를 입력받아 문자열로 생성
		StringBuilder start = new StringBuilder();
		for (int i=0; i<3; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<3; j++) {
				start.append(st.nextToken());
			}
		}

		// BFS 탐색으로 결과 출력
		System.out.println(bfs(start.toString()));

	}

	// BFS를 통해 퍼즐을 목표 상태로 맞추는 최단 거리를 구하는 메서드
	public static int bfs(String start) {
		Deque<String> queue = new ArrayDeque<>();
		queue.offer(start);

		// 시작 상태를 방문 처리하고 이동 횟수를 0으로 설정
		visited.put(start, 0);

		while(!queue.isEmpty()) {
			// 현재 상태와 이동 횟수 가져옴
			String cur = queue.poll();
			int moveCount = visited.get(cur);

			// 현재 상태가 목표 상태와 일치하면 이동 횟수를 반환
			if (cur.equals(target)) return moveCount;

			// 빈 칸('0')의 위치를 찾아서 좌표로 반환
			int zeroIndex = cur.indexOf('0');
			int x = zeroIndex / 3;
			int y = zeroIndex % 3;

			// 상하좌우 네 방향으로 이동 시도
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				// 이동한 위치가 3x3 퍼즐 범위를 벗어나지 않는지 확인
				if (nx >= 0 && nx < 3 && ny >= 0 && ny < 3) {
					// 빈 칸과 새 위치의 값을 교환하여 새로운 퍼즐 상태 생성
					String next = swap(cur, zeroIndex, nx * 3 + ny);

					// 새로운 상태가 방문되지 않았으면 큐에 추가하고 방문 표시
					if (!visited.containsKey(next)) {
						visited.put(next, moveCount + 1);
						queue.offer(next);
					}
				}
			}
		}
		return -1;
	}

	// 두 위치의 문자를 교환하여 새로운 상태 문자열을 반환하는 메서드
	public static String swap(String s, int i, int j) {
		char[] arr = s.toCharArray();
		char temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
		return new String(arr);
	}
}