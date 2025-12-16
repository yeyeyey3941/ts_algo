import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();

        int count = Integer.parseInt(br.readLine());

        int[] deque = new int[20002];

        int pointer = 10001;
        int starter = 10000;

        for (int i = 0; i<count; i++) {
            String[] input = br.readLine().split(" ");

//            sb.append(input[0]).append(" ");

            if (input[0].equals("size")) {
                sb.append(pointer-starter-1).append("\n");
                continue;
            }
            if (input[0].equals("empty")) {
                if (pointer - starter == 1) {
                    sb.append(1).append("\n");
                    continue;
                }
                sb.append(0).append("\n");
                continue;
            }
            if (input[0].equals("front")) {
                if (pointer - starter > 1) {
                    sb.append(deque[starter+1]).append("\n");
                    continue;
                }
                sb.append(-1).append("\n");
                continue;
            }
            if (input[0].equals("back")) {
                if (pointer - starter > 1) {
                    sb.append(deque[pointer-1]).append("\n");
                    continue;
                }
                sb.append(-1).append("\n");
            }
            if (input[0].charAt(1)=='u') { // push
                if (input[0].charAt(5)=='f') { // front
                    deque[starter--] = Integer.parseInt(input[1]);
                    continue;
                }
                if  (input[0].charAt(5)=='b') { // back
                    deque[pointer++] = Integer.parseInt(input[1]);
                    continue;
                }

            }
            if (input[0].charAt(1)=='o') { // pop
                if (pointer - starter == 1) {
                    sb.append(-1).append("\n");
                    continue;
                }
                if (input[0].charAt(4)=='f') { // front
                    sb.append(deque[++starter]).append("\n");
                    continue;
                }
                if (input[0].charAt(4)=='b') { // back
                    sb.append(deque[--pointer]).append("\n");
                }
            }
        }

        System.out.println(sb);
    }
}
