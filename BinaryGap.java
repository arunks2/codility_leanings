// @author : Arun Sharma
// problem link :https://app.codility.com/programmers/lessons/1-iterations/

class Solution {
    public int solution(int N) {
        // write your code in Java SE 8
        int number[] =  new int[32];
        int i=0;
        int largest = 0;
        while(N > 0) {
            number[i] = N%2;
            N = N/2;
            i++;
        }
        int j = i-1;
        while(j >0) {
            if(number[j] == 1) {
                int k = j -1;
                int large = 0;
                while(number[k] !=1 && k>0) {
                    large++;
                    k--;
                }
                if(k==0 && number[k] !=1) {
                    break;
                }
                else {
                    if(large > largest) {
                        largest = large;
                    }
                    j=k;
                }
            }
        }
        
        return largest;
    }
}