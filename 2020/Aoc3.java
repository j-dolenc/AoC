import java.io.*;
import java.math.BigInteger;

public class Aoc3 {
    public static void main(String[] args) throws IOException{
        BufferedReader reader = new BufferedReader(new FileReader(args[0]));
        char[][] grid = new char[323][31];
        for(int i = 0; i <323; i++){
            String line = reader.readLine();
            for(int j = 0; j< line.length(); j++){
                grid[i][j] = line.charAt(j);
            }
        }
        //part 1
        int k = 0;
        int h =0;
        int drevesa = 0;
        while(k != 323){
            if(grid[k][h] == '#'){
                drevesa++;
            }
            k+=1;
            h+=3;
            if(h>= 31) h %= 31;
        }
        System.out.println(drevesa);


        //part 2
        BigInteger drevesa1 = BigInteger.ZERO;
        BigInteger drevesa2 = BigInteger.ZERO;;
        BigInteger drevesa3 = BigInteger.ZERO;;
        BigInteger drevesa4 = BigInteger.ZERO;;
        BigInteger drevesa5 = BigInteger.ZERO;;




        k = 0;
        h =0;
        while(k != 323){
            if(grid[k][h] == '#'){
                BigInteger test = new BigInteger("1");
                drevesa1=drevesa1.add(test);
            } 
                
            k+=1;
            h+=1;
            if(h>= 31) h %= 31;
        }
        k = 0;
        h =0;
        while(k != 323){
            if(grid[k][h] == '#'){
                BigInteger test = new BigInteger("1");
                drevesa2=drevesa2.add(test);
            }
            k+=1;
            h+=3;
            if(h>= 31) h %= 31;
        }
        k = 0;
        h =0;
        while(k != 323){
            if(grid[k][h] == '#'){
                BigInteger test = new BigInteger("1");
                drevesa3=drevesa3.add(test);
            }
            k+=1;
            h+=5;
            if(h>= 31) h %= 31;
        }
        k = 0;
        h =0;
        while(k != 323){
            if(grid[k][h] == '#'){
                BigInteger test = new BigInteger("1");
                drevesa4=drevesa4.add(test);
            }
            k+=1;
            h+=7;
            if(h>= 31) h %= 31;
        }
        k = 0;
        h = 0;
        while(k < 323){
            if(grid[k][h] == '#') {
                BigInteger test = new BigInteger("1");
                drevesa5=drevesa5.add(test);
            }
            k+=2;
            h+=1;
            if(h == 31) h = 0;
        }
        //System.out.println(drevesa1 +" "+drevesa2 +" "+drevesa3 +" "+drevesa4 +" "+drevesa5 +" ");
        String hm  =drevesa1.multiply(drevesa2.multiply(drevesa3.multiply(drevesa4.multiply(drevesa5)))).toString();
        System.out.println(hm);    
        reader.close();
    }
}
