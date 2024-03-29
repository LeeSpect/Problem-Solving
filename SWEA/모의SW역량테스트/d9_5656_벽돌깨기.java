import java.io.*;
import java.util.*;

public class d9_5656_벽돌깨기{
	static int[] dx={-1,0,1,0},dy={0,1,0,-1};
	static int N, W, H, ans, score, beforeScore, tempScore;
	static int[][] grid;
	static Queue<int[]> deq;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb=new StringBuilder();
		StringTokenizer st;
		
		int T=Integer.parseInt(br.readLine());
		for(int tc=1; tc<T+1; tc++){
			st=new StringTokenizer(br.readLine(), " ");
			N=Integer.parseInt(st.nextToken());
			W=Integer.parseInt(st.nextToken());
			H=Integer.parseInt(st.nextToken());
			ans=Integer.MAX_VALUE;
			grid=new int[H][W];
			score=0;
			
			for(int i=0;i<H;i++){
				st=new StringTokenizer(br.readLine(), " ");
				for(int j=0;j<W;j++) grid[i][j] = Integer.parseInt(st.nextToken());
			}
			comb(grid, 0);
			if(ans==Integer.MAX_VALUE) ans=0;
			sb.append("#").append(tc).append(" ").append(ans).append("\n");
		}
		System.out.println(sb.toString());
		br.close();
	}
	
	static void comb(int[][] grid, int cnt){
		if (cnt==N){
			int temp=0;
			for(int x=0;x<H;x++){
				for(int y=0;y<W;y++){
					if(grid[x][y] != 0) temp++;
				}
			}
			ans=Math.min(ans, temp);
			return;
		}
		for(int i=0; i<W; i++){
			int[][] newGrid = new int[H][W];
			for(int x=0; x<H; x++) {
				for(int y=0; y<W; y++) newGrid[x][y]=grid[x][y];
			}
			
			beforeScore = score;
			int[][] nextGrid = getGrid(newGrid, i);
			if(score == beforeScore) continue;
			
			tempScore = score-beforeScore; 
			comb(nextGrid, cnt+1);
			score -= tempScore;
		}
	}
	
	static int[][] getGrid(int[][] grid, int y){
		int x=0, power=0;
		for(int r=0; r<H; r++){
			if(grid[r][y]!=0){
				power = grid[r][y];
				x = r;
				break;
			}
		}
		if(power==0) return grid;
		deq = new ArrayDeque<>();
		score += grid[x][y];
		grid[x][y] = 0;
		deq.offer(new int[] {x, y, power});
		while(!deq.isEmpty()){
			int size = deq.size();
			for(int s=0; s<size; s++){
				int[] temp = deq.poll();
				for(int d=0; d<4; d++){
					int nx=temp[0], ny=temp[1];
					for(int t=0; t<temp[2]-1; t++){
						nx=nx+dx[d];
						ny=ny+dy[d];
						if(0>nx||nx>H-1||0>ny||ny>W-1) break;
						deq.offer(new int[] {nx, ny, grid[nx][ny]});
						score += grid[nx][ny];
						grid[nx][ny]=0;
					}
				}
			}
		}
		Loop: for(int c=0; c<W; c++){
			int downX=0;
			for(int i=H-1; i>-1; i--){
				if(grid[i][c]==0){
					downX = i;
					break;
				}
			}
			if(downX==0) continue;
			do{
				int upX=-1;
				for(int i=downX-1; i>-1; i--){
					if(grid[i][c]!=0){
						upX=i;
						break;
					}
				}
				if(upX==-1) continue Loop;
				grid[downX][c] = grid[upX][c];
				grid[upX][c] = 0;
				downX--;
			}while(true);
		}
		return grid;
	}
}
