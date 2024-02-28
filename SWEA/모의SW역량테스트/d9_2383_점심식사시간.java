import java.io.*;
import java.util.*;
import java.awt.Point;

public class d9_2383_점심식사시간{
	static int N, ans, size;
	static int[][] stairs;
	static List<Point> people;

	public static void main(String[] args) throws Exception{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb=new StringBuilder();
		StringTokenizer st;
		
		int T=Integer.parseInt(br.readLine());
		for(int tc=1; tc<T+1; tc++){
			N=Integer.parseInt(br.readLine());
			
			people=new ArrayList<>();
			stairs=new int[2][3]; // 0: x, 1: y, 2: 시간
			int stair=0;
			for(int i=0; i<N; i++){
				st=new StringTokenizer(br.readLine(), " ");
				for(int j=0; j<N; j++){
					int temp = Integer.parseInt(st.nextToken());
					if(temp==1) people.add(new Point(i,j));
					else if(temp>1){
						stairs[stair++] = new int[] {i,j,temp};
					}
				}
			}
			
			ans = Integer.MAX_VALUE;
			size = people.size();
			subs(0, new boolean[size], 0, 0);
			
			sb.append("#").append(tc).append(" ").append(ans).append("\n");
		}
		System.out.println(sb.toString());
		br.close();
	}

	static void subs(int idx, boolean[] stairChoice, int group1, int group2){
		if(idx == size){
			int[] time1 = new int[group1]; // 이 계단을 선택한 사람들이 계단에 도착하는 데까지 걸리는 시간
			int[] time2 = new int[group2];
			int t1=0, t2=0;
			for(int i=0; i< size; i++){ // stairChoice 배열을 통해 각 사람이 어떤 계단을 선택했는지 확인하고
				if(!stairChoice[i])     // 선택한 계단에 도착하는 시간을 calc 메서드로 계산
					time1[t1++] = calc(people.get(i), stairs[0]);
				else
					time2[t2++] = calc(people.get(i), stairs[1]);
			}
			Arrays.sort(time1); // 계단에 도착하는 시간을 오름차순으로 정렬
			Arrays.sort(time2);

			adjustTime(time1, stairs[0][2]); // 각 계단별로 대기 시간 조정 -> 동시에 최대 3명가지만 내려갈 수 있음
			adjustTime(time2, stairs[1][2]);
			
			// 각 계단에서 마지막으로 내려가는 사람이 계단을 완전히 내려가는 시간
			int temp = Math.max(t1==0 ? 0 : time1[t1-1], t2==0 ? 0 : time2[t2-1]);
			ans = Math.min(ans, temp);
			return;
		}

		stairChoice[idx] = false;
		subs(idx+1, stairChoice, group1+1, group2);
		stairChoice[idx] = true;
		subs(idx+1, stairChoice, group1, group2+1);
	}

	// 사람들의 대기 시간 조정 -> 동시에 최대 3명가지만 내려갈 수 있음
	static void adjustTime(int[] times, int stairLength){
		// int[] times: 각 사람이 계단에 도착하여 내려가기 시작하는 시간을 담고 있는 배열
		// int stairLength: 계단을 내려가는 데 걸리는 시간

		if(times.length > 3){
			for(int i=3; i<times.length; i++){
				times[i] = Math.max(times[i], times[i-3]+stairLength);
				// times[i]: 원래 이 사람이 계단에 도착하여 내려가기 시작할 예정이었던 시간
				// times[i-3] + stairLength: 세 명 중 가장 빨리 계단을 내려갈 사람이 계단을 완전히 내려가는 시간
				//                         : 현재 사람이 계단을 내려가기 시작할 수 있는 가장 빠른 시간
			}
		}
	}

	static int calc(Point p, int[] stairs){
		return Math.abs(p.x-stairs[0]) + Math.abs(p.y - stairs[1]) + stairs[2] + 1; // 계단에 도착하는 시간
		// Math.abs(p.x-stairs[0]) + Math.abs(p.y - stairs[1]) => 사람과 게단 사이의 거리
		// stairs[2] => 계단을 내려가는 데 필요한 시간: 사람이 계단에 도착한 후 계단을 완전히 내려가는 데까지 필요한 시간
		// 1 => 사람이 계단에 도착하고 실제로 계단을 내려가기 시작하는 시간 == 1분
	}
}
