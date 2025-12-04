import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Main {
    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static int[] field = new int[1001];

    public static void main(String[] args) throws IOException {
        int answer = 0;

        Integer n = Integer.valueOf(bf.readLine());
        Arrays.setAll(field, x-> x%2);
        field[1] = 0; field[2] = 1;

        // Eratosthenes's field
        for (int i=3;i<1001; i=i+2) {
            if (field[i] == 1) {
                for (int j = 2 * i; j < 1001; j = j + i) {
                    field[j] = 0;
        }}}

        ArrayList<Integer> primeList = new ArrayList<>();
        StringTokenizer primeBuffers = new StringTokenizer(bf.readLine());

        for (int i=0;i<n;i++) {
            answer += field[Integer.valueOf(primeBuffers.nextToken())];
        }

        System.out.println(answer);
    }
}
