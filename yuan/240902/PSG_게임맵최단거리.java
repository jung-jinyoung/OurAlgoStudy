/*
 * 배열 길이는 .length; 로 확인 
 */
import java.util.*;
import java.math.*; 

class Solution {
    static int n,m;
    static int mincnt;     
    static int[][] visited;
    static int[] dx = new int[]{-1,0,1,0};
    static int[] dy = new int[]{0,1,0,-1};
    
    ///dfs
    public static void dfs(int x, int y, int[][] visited, int[][] maps){
        if ( x == n-1 && y == m-1 ){
            mincnt = Math.min(visited[n-1][m-1],mincnt);
            return;
        }
        //현재 이동거리기준 백트래킹
        if (visited[x][y] > mincnt){
            return;
        }
        // 이동
        for (int k=0; k<4; k++){
            int nx = x + dx[k];
            int ny = y + dy[k]; 
            
            // 범위안, 방문한적 없음, 이동 가능  
            if ( 0<= nx && nx< n && 0<= ny && ny<m && visited[nx][ny] ==0 && maps[nx][ny] == 1){
                visited[nx][ny] = visited[x][y] + 1;
                dfs(nx,ny,visited,maps); // dfs
                visited[nx][ny] = 0; // 다시 바꾸기 
            }
        }
    }
    
    public int solution(int[][] maps) {
        
        n = maps.length;
        m = maps[0].length; 
        mincnt = n*m+1;
        
        visited = new int[n][m];
        visited[0][0] = 1; 
        dfs(0,0,visited,maps);
        
        if (mincnt != m*n+1){
            return mincnt;
        } else {
            return -1; 
        }
    }
}