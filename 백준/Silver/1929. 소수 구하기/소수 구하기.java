import java.io.*;

public class Main{
    public static void main(String[] args)  throws IOException {

        int[] field = new int[1000001];
        field[2] = 1;
        for (int i = 3;i<field.length;i=i+2) {
            field[i] = 1;
        }
        for (int i = 3;i<field.length;i=i+2) {
            if (field[i] ==1 ) {
                for (int j = 2; j< (int)(field.length/i);j++) {
                    field[j*i] = 0;
                }
            }
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");

        StringBuilder sb = new StringBuilder();

        int start = Integer.parseInt(input[0]);
        int end = Integer.parseInt(input[1]);

        for (int i = start; i <= end; i++) {
            if (field[i] == 1) {
                sb.append(i).append("\n");
            }
        }

        System.out.println(sb);
        // System.out.println(Arrays.toString(field));


    }
}
