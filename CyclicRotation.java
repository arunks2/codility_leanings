// @author: Arun Sharma
// Problem link : https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/start/

class Solution {
    public int[] solution(int[] A, int K) {
        // write your code in Java SE 8
        int length = A.length;
        if(A.length == K  || length ==0) {
            return A;
        }
        K = K%length;
        int newArray [] = new int[length];
        
        for(int i=0; i<length; i++) {
            int index = K+i;
            if(index >=length) {
                index = index%length;
            }
            newArray[index] = A[i];
        }
        return newArray;
    }
}