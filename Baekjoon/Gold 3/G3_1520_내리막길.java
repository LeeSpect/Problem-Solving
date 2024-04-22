import java.io.*;
import java.util.*;

public class G3_1520_내리막길{
	static int M, N;
	static int[] dx={0,1,0,-1}, dy={1,0,-1,0};
	static int[][] map, dp;
	
    public static void main(String[] args) throws Exception{
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st=new StringTokenizer(br.readLine(), " ");
    	
    	N=Integer.parseInt(st.nextToken());
    	M=Integer.parseInt(st.nextToken());
    	map=new int[N][M];
    	dp=new int[N][M];
    	for(int i=0; i<N; i++){
    		st=new StringTokenizer(br.readLine(), " ");
    		for(int j=0; j<M; j++){
    			map[i][j]=Integer.parseInt(st.nextToken());
    			dp[i][j]=-1;
    		}
    	}
    	dp[N-1][M-1] = 1;
    	dfs(0,0);
    	System.out.println(dp[0][0]);
    	br.close();
    }
    
    static void dfs(int x, int y){
    	if(x==N-1 && y==M-1) return; // 끝 지점 도착
    	if(dp[x][y] != -1) return;
    	
    	dp[x][y] = 0;
    	
    	int nx, ny;
    	for(int d=0; d<4; d++){
    		nx=x+dx[d];
    		ny=y+dy[d];
    		if(0>nx || nx>N-1 || 0>ny || ny>M-1) continue;
    		if(map[x][y] > map[nx][ny]){
    			if(dp[nx][ny] != -1) dp[x][y] += dp[nx][ny];
    			else{
    				dfs(nx, ny);
    				dp[x][y] += dp[nx][ny];
    			}
    		}
    	}
    }
}
