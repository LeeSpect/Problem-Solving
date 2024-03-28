import java.util.*;
import java.io.*;
import java.awt.Point;

public class G4_3055_탈출{
	static int R,C,cnt;
	static boolean okToGo;
	static int[] dx={1,-1,0,0},dy={0,0,1,-1};
	static int[][] maps;
	static Point endPoint;
	static Queue<Point> waterQue,dochiQue;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine(), " ");
		R=Integer.parseInt(st.nextToken());
		C=Integer.parseInt(st.nextToken());
		
		maps=new int[R][C];
		dochiQue=new ArrayDeque<>(); 
		waterQue=new ArrayDeque<>(); 
		
		for(int i=0; i<R; i++){
			String string=br.readLine();
			for(int j=0; j<C; j++){
				switch(string.charAt(j)){
				case '.': maps[i][j]=0; break;
				case 'X': maps[i][j]=-1; break;
				case '*': maps[i][j]=1; waterQue.offer(new Point(i,j)); break;
				case 'S': maps[i][j]=2; dochiQue.offer(new Point(i,j)); break;
				case 'D': maps[i][j]=3; endPoint=new Point(i,j); break;
				}
			}
		}
		
		cnt=1;okToGo=false;
		loop: while(!dochiQue.isEmpty()){
			int lenWaterPoints = waterQue.size();
			for(int ld=0; ld<lenWaterPoints; ld++){
				Point waterPoint = waterQue.poll();
				for(int d=0; d<4; d++){
					int nx=waterPoint.x+dx[d];
					int ny=waterPoint.y+dy[d];
					if(0>nx || nx>R-1 || 0>ny || ny>C-1) continue;
					if(maps[nx][ny]==0||maps[nx][ny]==2){
						maps[nx][ny]=1;
						waterQue.offer(new Point(nx, ny));
					}
				}
			}
			
			// 'X'=-1 / '.'=0 / '*'=1 / 'S'=2 / 'D'=3
			int lenDochiPoints = dochiQue.size();
			for(int ls=0; ls<lenDochiPoints; ls++){
				Point dochiPoint = dochiQue.poll();
				for(int d=0; d<4; d++){
					int nx=dochiPoint.x+dx[d];
					int ny=dochiPoint.y+dy[d];
					if(0>nx||nx>R-1|| 0>ny || ny>C-1 || maps[nx][ny]=='*') continue;
					if(maps[nx][ny]==3) {
						okToGo=true;
						break loop;
					}
					if(maps[nx][ny]==0){
						maps[nx][ny]=2;
						dochiQue.offer(new Point(nx, ny));
					}
				}
			}
			cnt++;
		}
		if(okToGo) System.out.println(cnt);
		else System.out.println("KAKTUS");
		br.close();
	}
}



















