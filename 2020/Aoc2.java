import java.util.*;
//import java.util.*;
import java.io.*;
//import java.time.*;

public class Aoc2{
    public static void main(String[] args)throws IOException{
        Scanner sc = new Scanner(System.in);
        String in = args[0];
        BufferedReader reader = new BufferedReader(new FileReader(in));
        String line = "x";
        int ok = 0;
        int ok1 = 0;
        while(true){
            line = reader.readLine();
            if(line.equals("aaa")) break;
            String[] split = line.split("-");
            int zac = Integer.parseInt(split[0]);
            String[] split1 = split[1].split(" ");
            int konc = Integer.parseInt(split1[0]);
            char ch = split1[1].charAt(0);
            System.out.println(split1[2]);
            String beseda = split1[2];


            //part 1
            int st = 0;
            for(int i = 0; i <beseda.length();i++){
                if(beseda.charAt(i)==ch) st++;
            }
            if(st >= zac && st<= konc) ok++;


            //part 2
            if(beseda.charAt(zac-1)==ch  && !(beseda.charAt(konc-1)==ch)) ok1++;
            if(!(beseda.charAt(zac-1)==ch)  && (beseda.charAt(konc-1)==ch)) ok1++;
        }
        System.out.println(ok + " " + ok1);




        reader.close();
        sc.close();
    }
}