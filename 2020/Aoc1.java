import java.util.*;


public class Aoc1{
    public static int[] n = new int[10001];
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int ind = 0;
        
        while(sc.hasNextInt()){
            n[ind] =  sc.nextInt();
            ind++;
        }
        ind = 0;
        //int rez = 0;
        while(n[ind] != 0){

            int j = ind+1;
            while(n[j] != 0){

                int k = j+1;
                while(n[k] != 0){

                    if(n[ind]+ n[j]+ n[k] == 2020){
                        System.out.println(n[ind]*n[j]*n[k]);   
                    }
                    k++;
                }

                j++;
            }
            
            ind++;
        }

        sc.close();
    }
}