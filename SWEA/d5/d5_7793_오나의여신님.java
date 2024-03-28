import java.util.*;
import java.io.*;
import java.awt.Point;

public class d5_7793_오나의여신님{
	static int N,M,cnt;
	static boolean okToGo;
	static int[] dx={1,-1,0,0},dy={0,0,1,-1};
	static int[][] maps;
	static Point godPoint;
	static Queue<Point> devilQue,sooQue;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb=new StringBuilder();
		StringTokenizer st;
		
		int T=Integer.parseInt(br.readLine());
		for(int tc=1; tc<T+1; tc++){
			st=new StringTokenizer(br.readLine(), " ");
			N=Integer.parseInt(st.nextToken());
			M=Integer.parseInt(st.nextToken());
			
			maps=new int[N][M];
			sooQue=new ArrayDeque<>(); 
			devilQue=new ArrayDeque<>(); 
			
			for(int i=0; i<N; i++){
				String string=br.readLine();
				for(int j=0; j<M; j++){
					switch(string.charAt(j)){
					case '.': maps[i][j]=0; break;
					case 'X': maps[i][j]=-1; break;
					case '*': maps[i][j]=1; devilQue.offer(new Point(i,j)); break;
					case 'S': maps[i][j]=2; sooQue.offer(new Point(i,j)); break;
					case 'D': maps[i][j]=3; godPoint=new Point(i,j); break;
					}
				}
			}
			
			cnt=1;okToGo=false;
			loop: while(!sooQue.isEmpty()){
				int lenDevilPoints = devilQue.size();
				for(int ld=0; ld<lenDevilPoints; ld++){
					Point devilPoint = devilQue.poll();
					for(int d=0; d<4; d++){
						int nx=devilPoint.x+dx[d];
						int ny=devilPoint.y+dy[d];
						if(0>nx || nx>N-1 || 0>ny || ny>M-1) continue;
						if(maps[nx][ny]==0||maps[nx][ny]==2){
							maps[nx][ny]=1;
							devilQue.offer(new Point(nx, ny));
						}
					}
				}
				
				int lenSooPoints = sooQue.size();
				for(int ls=0; ls<lenSooPoints; ls++){
					Point sooPoint = sooQue.poll();
					for(int d=0; d<4; d++){
						int nx=sooPoint.x+dx[d];
						int ny=sooPoint.y+dy[d];
						if(0>nx||nx>N-1|| 0>ny || ny>M-1 || maps[nx][ny]=='*') continue;
						if(maps[nx][ny]==3) {
							okToGo=true;
							break loop;
						}
						if(maps[nx][ny]==0){
							maps[nx][ny]=2;
							sooQue.offer(new Point(nx, ny));
						}
					}
				}
				cnt++;
			}
			sb.append("#").append(tc).append(" ");
			if(okToGo) sb.append(cnt);
			else sb.append("GAME OVER");
			sb.append("\n");
		}
		System.out.println(sb.toString());
		br.close();
	}
}
