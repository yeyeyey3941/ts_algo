class Solution {
    public int solution(int n, int w, int num) {
        int answer = 0;
        int MAX_HEIGHT = (int) n/w + 1;
        int[][] boxes = new int[MAX_HEIGHT][w];

        int w_pointer = 0;
        int h_pointer = MAX_HEIGHT-1;
        int signed_pointer = 1;
        int value = 1;

        int target_w = 0;
        int target_h = 0;

        while (value < n+1) {

            // signed_pointer == 1  -> 증가 하다가 도달하면 올라가고, 올라간 다음턴에는 감소하기위해 미리 signed = -1
            // signed_pointer == -1 -> 최댓값에서 할당하고  감소하다가 0도달하면 올라가고, 올라간 다음 턴에 미리 증가하기 위해 signed = 1
            boxes[h_pointer][w_pointer] = value;
            if (value==num) {
                target_w = w_pointer;
                target_h = h_pointer;
            }


            if (signed_pointer>0 && w_pointer == w-1) {
                signed_pointer = -1;
                h_pointer--;
                value++;
                continue;
            }
            if (signed_pointer<0 && w_pointer == 0) {
                signed_pointer = 1;
                h_pointer--;
                value++;
                continue;
            }
            w_pointer += signed_pointer;
            value++;
        }

        answer = (boxes[0][target_w]==0) ? target_h : target_h+1;

        
        return answer;
    }
}