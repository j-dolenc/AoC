import java.util.*;



public class Naloga1{

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] tabela = new int[100];
        for(int i = 0; i < 100; i++){
            if(sc.hasNextInt()){
            tabela[i] = sc.nextInt();
            }
            else break;
        }
        System.out.println("kul " + Arrays.toString(tabela));
        
        //System.out.println("kul " + Arrays.toString(tabela));
       
        
        int[] fuel = tabela;
        
        for(int i = 0; i< 100; i++){
            tabela[i] /= 3;
            tabela[i] -= 2;
            
        }

        for(int i = 0; i <100; i++){
            int input = 0;
            int sest = fuel[i];
            System.out.println(fuel[i]);
            while((sest /3) - 2 >= 0){
                sest /= 3;
                sest -=2;
                input+=sest;
                
            }
            System.out.println(input);
            fuel[i] += input;
        }
        int asum = 0;
        for(int i = 0; i< 100; i++){
            
            asum += fuel[i];
        }
        System.out.println("rezultat: " + asum);

        sc.close();
    }
}