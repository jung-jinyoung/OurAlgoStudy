/*
 최소 단위로 완탐
 문자열 자르고 합칠때 StringBuilder sb = new StringBuilder();
 문자열 자르기 string.subString();  
 */

import java.util.*;
class Solution {
    static int lenS;
    static int nowLen; 
    static int minLen;
    static String prev;
    static String now;
        
    // s를 i씩 잘라서 확인 
    public static int check(String s, int i){
        StringBuilder sb = new StringBuilder(); 
        
        prev = "";
        int cnt = 0;
        
        for (int j=0; j<lenS; j+=i){
    
            if (j+i<lenS){ // 인덱스 안넘을때
                now = s.substring(j,j+i);
            } else{
                now = s.substring(j,lenS);//인덱스 넘을때 start, end 면 end+1까지 
            }
            
            if (now.equals(prev)){
                cnt++; 
            } else{ // 다를떄: 이전꺼sb에 넣고 cnt 초기화
                if(cnt>1){
                    sb.append(cnt);
                }
                sb.append(prev);
                cnt = 1; 
                prev = now; 
            }
        }
        if (cnt>1){
            sb.append(cnt);
        }
        sb.append(now); 
        return sb.length();
    }
    
    
    public int solution(String s) {
        lenS = s.length();
        minLen = lenS * lenS; 
            
        for (int i=1; i<=lenS; i++){
            nowLen = check(s, i);
            minLen = Math.min(minLen, nowLen);
        }

        return minLen;
    }
}