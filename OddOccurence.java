// @author : Arun Sharma
// Problem Link : https://app.codility.com/c/run/trainingNDVD33-XRW/

// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int[] A) {
        // write your code in Java SE 8
        Arrays.sort(A);
        int length = A.length;
        if (length == 1) {
            return A[0];
        }
        int i=0;
        for(i=0;i<length-1; i=i+2) {
            if(A[i] != A[i+1]) {
                return A[i];
            }
        }
        if(A[length-1] != A[length-2] ) {
            return A[length-1];
        }
        return A[0];
    }
}