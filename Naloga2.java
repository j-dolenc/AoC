import java.util.*;

import javax.annotation.PostConstruct;

import java.io.*;
public class Naloga2{
    public static void main(String[] args) throws IOException{
        String in = args[0];
        String out = args[1];


        BufferedReader reader = new BufferedReader(new FileReader(in));
        BufferedWriter writer = new BufferedWriter(new FileWriter(out));

        String line;

        line = reader.readLine();

        String[] tabela = line.split(",");
        int[] stevilke = new int[tabela.length];

        //System.out.println(Arrays.toString(tabela));

        for(int i = 0; i < tabela.length; i++){
            stevilke[i] = Integer.parseInt(tabela[i]);
        }
        //writer.write(Arrays.toString(stevilke));

        int dolzina = stevilke.length;

        //stevilke[1] = 12;
        //stevilke[2] = 2;
       
        int[] rezerva = new int[dolzina];
        rezerva = stevilke;
        
        
        
        
        for(int j = 0; j < 100; j++){
            //stevilke[1] = j;
            for(int k = 0; k < 100; k++){
                
                for(int i = 0; i < dolzina; i++){
                    rezerva[i] = stevilke[i];
                }
                rezerva[1] = j;
                rezerva[2] = k;
                //stevilke[2] = k;
                
                for(int i = 0; i <dolzina; i= i +4 ){
                    
                    int posZero = rezerva[i];
                    int posOne = rezerva[i + 1];
                    int posTwo = rezerva[i + 2];
                    int posTri = rezerva[i + 3];
                    
                    
                    
                    if(posZero == 1){
                        rezerva[posTri] = rezerva[posOne] + rezerva[posTwo];
                    }
                    else if(posZero == 2){
                        rezerva[posTri] = rezerva[posOne] * rezerva[posTwo];
                    }
                    else{
                        
                        break;
                    }
                  
                }
                if(rezerva[0] == 19690720){
                    System.out.println(j + " "  + k + " " + stevilke[0]);
                }
            }
            
        }

        

        


        

        reader.close();
        writer.close();
    }
}