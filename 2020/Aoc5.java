import java.util.*;
import java.io.*;

public class Aoc5{
        public static void main(String[] args)throws IOException{
        Scanner sc = new Scanner(System.in);
        BufferedReader reader = new BufferedReader(new FileReader(args[0]));
        
        
            int[] letalo = new int[891];
            int high = -1;
            for(int i=  0; i <891; i++){
                String line =reader.readLine();
                //System.out.println(line);
                int zac = 0;
                int konc = 127;
                for(int j =0 ; j< 7; j++){
                    if(line.charAt(j) == 'F'){
                        konc= (konc+zac)/2;
                    }
                    else{
                        zac= ((konc+zac)/2)+1;
                    }
                }
                //System.out.println(zac +" "+ konc);
                int seat1 = 0;
                int seat2 = 7;
                for(int j = 7; j <10; j++){
                    if(line.charAt(j) == 'L'){
                        seat2= (seat2+seat1)/2;
                    }
                    else{
                        seat1= ((seat2+seat1)/2)+1;    
                    }
                }
                //System.out.println(seat1 + " " + seat2);
                int seat = (zac*8)+seat1;
                if(seat >high) high =seat;

                letalo[i] = seat;
            }
            Arrays.sort(letalo);
            for(int i = 0; i < 890; i++){
                if(letalo[i+1]-letalo[i] == 2 ){
                    System.out.println(letalo[i]+1);
                }
            }
        //System.out.println(high);

        
        sc.close();
        reader.close();
    }
}