import java.io.*;
import java.util.*;

public class d3_4615_재미있는오셀로게임 {
	static int[] dx = { -1, -1, -1, 0, 0, 1, 1, 1 }, dy = { -1, 0, 1, -1, 1, -1, 0, 1 };

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		int T = Integer.parseInt(br.readLine());
		int N, M, n, x, y, color, black, white;
		int[][] map;
		boolean flag;

		for (int tc = 1; tc < T + 1; tc++) {
			st = new StringTokenizer(br.readLine(), " ");
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());

			// b=1, w=2
			map = new int[N][N];
			n = (N - 1) / 2; // 중간값
			map[n][n] = 2;
			map[n][n + 1] = 1; // 초기 돌 위치
			map[n + 1][n] = 1;
			map[n + 1][n + 1] = 2;
			black = 2;
			white = 2; // 초기 돌 개수

			for (int m = 0; m < M; m++) {
				st = new StringTokenizer(br.readLine(), " ");
				y = Integer.parseInt(st.nextToken()) - 1; // 0부터 시작
				x = Integer.parseInt(st.nextToken()) - 1;
				color = Integer.parseInt(st.nextToken());
				map[x][y] = color; // 돌 놓기
				if (color == 1)
					black++; // 돌 개수 증가
				else
					white++;

				for (int d = 0; d < 8; d++) { // 8방향 탐색
					int nx = x, ny = y;
					flag = false; // 해당 방향에서 상대방 돌이 뒤집혔는지
					for (int i = 0; i < 8; i++) { // 거리는 최대 8칸까지 탐색
						nx += dx[d];
						ny += dy[d];
						// 범위를 벗어나거나 빈칸이면 break
						if (0 > nx || nx > N - 1 || 0 > ny || ny > N - 1 || map[nx][ny] == 0)
							break;
						if (map[nx][ny] == color) { // 같은 색 돌이 나오면 뒤집기 가능
							flag = true;
							break; // 해당 방향에서 뒤집기가 가능하면 flag를 true로 하고 break
						}
					}
					if (flag) { // flag가 true이면 뒤집기
						nx = x;
						ny = y;
						for (int i = 0; i < 8; i++) {
							nx += dx[d];
							ny += dy[d]; // 같은 색 돌이 나올 때까지 뒤집어야 하므로
							if (map[nx][ny] == color)
								break; // 같은 색 돌이 나오면 뒤집기 종료
							map[nx][ny] = color;
							if (color == 1) { // 뒤집은 만큼 돌 개수 연산
								black++;
								white--;
							} else {
								white++;
								black--;
							}
						}
					}
				}
			}
			sb.append("#").append(tc).append(" ").append(black).append(" ").append(white).append("\n");
		}

		br.close();
		System.out.println(sb.toString());
	}
}
