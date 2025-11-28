class Solution {
    public String solution(int num) {
        String answer = ((num%2+2)%2==1 ? "Odd" : "Even");
        // System.out.printf("%d",-1%2);
        return answer;
    }
}