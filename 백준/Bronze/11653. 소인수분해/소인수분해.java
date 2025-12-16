import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int target = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();

        while (target%2==0) {
            sb.append(2).append("\n");
            target /= 2;
        }

        for (int i = 3; i <= target; i = i+2) {
            while(target%i==0) {
                sb.append(i).append("\n");
                target /= i;
            }
            if (target==1) break;
        }
        System.out.println(sb);
    }
}
