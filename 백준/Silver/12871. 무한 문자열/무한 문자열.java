import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static char bufferChar[] = new char[51];
    static char s[] = new char[2501]; // input : "abab"
    static char t[] = new char[2501]; // input : "ababab"

    public static void main(String[] args) throws IOException {
        // input to s & check length
        bufferChar = br.readLine().toCharArray();
        int len_s = bufferChar.length;
        for (int i=0; i<len_s; i++)
            s[i] = bufferChar[i];
        
        // input to t
        bufferChar = br.readLine().toCharArray();
        int len_t = bufferChar.length;
        for (int i=0; i<len_t; i++)
            t[i] = bufferChar[i];
        
        // gcd to get uclide method
        int gcd = uclidean_algorithm(len_s, len_t);
        int repeat_s = len_t/gcd;
        int repeat_t = len_s/gcd;

        for (int i = 1; i < repeat_s; i++) {
            for (int j = 0; j < len_s; j++) {
                s[len_s * i + j] = s[j];
            }
        }

        for (int i=1;i<repeat_t;i++){
            for (int j=0;j<len_t;j++){
                t[len_t * i + j] = t[j];
            }
        }

        for (int i = 0; i < len_s*repeat_s; i++) {
            if (s[i] != t[i]) {
                System.out.println(0);
                return;
            }
        }
        System.out.println(1);
        return;

    }

    static int uclidean_algorithm(int a,int b) {
        if (a < b) {
            int temp = a;
            a = b;
            b = temp;
        }
        while (a%b!=0) {
            int temp = a%b;
            a = b;
            b = temp;
        }
        return b;
    }
}
