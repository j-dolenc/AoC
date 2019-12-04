


public class n4{
    public static void main(String[] args){
        
        int spMeja = 165432;
        int zgMeja = 707912;


        int koliko= 0;
        
        for(int i = spMeja; i <= zgMeja; i++){
            boolean seVeca = true;
            int num =i;
            int prev = 10;
            while (num!=0) { 
                int rem = num % 10; 
                num /= 10; 
                if (rem > prev){
                    seVeca = false;
                    break;
                } 
            
                prev = rem; 
            } 
            num = i;
            boolean imaDvaZaporedna = false;
            int stPonovitev = 1;
            if(seVeca){
                while (num!=0) { 
                    int rem = num % 10; 
                    num /= 10; 
                    if (rem == prev){
                        stPonovitev++;
                        if(stPonovitev == 2 && num%10 != rem){
                            imaDvaZaporedna = true;
                        }
                    } 
                    else{
                        stPonovitev = 1;
                    }
                    prev = rem; 
                }
            }
            if(imaDvaZaporedna && seVeca){
                koliko++;
            }
        }
        System.out.println(koliko);
    }
}