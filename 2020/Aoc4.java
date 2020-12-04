
//lol neki sm spremenu ne dela vec :D
import java.io.*;
import java.util.*;




public class Aoc4 {
    public static void main(String[] args)throws IOException{
        BufferedReader reader = new BufferedReader(new FileReader(args[0]));
        Scanner sc = new Scanner(System.in);

        
        //String line  = reader.readLine();


        //part 1
        int ok = 0;
        //boolean curr = false;
        //boolean got = false;
        int koliko = 0;
        int[] check = new int[8];
        for(int i = 0; i  <1023; i++){

            String line = reader.readLine();
            System.out.println(line);
            if(line.equals("")){
                //koliko++;
                int ku = 0;
                for(int j  = 0; j <7; j++){
                    if(check[j] ==1) ku++;
                    
                }
                // if(ku == 8)ok++;
                // else if(ku ==  7 && check[7] == 0) ok++;
                if(ku == 7) ok++;
                for(int j  = 0; j <8; j++){
                    check[j] = 0;
                }                 
                System.out.println(ok);
            }
            else{
                //System.out.println("kuku");
                String[] split = line.split(" ");
                for(int j = 0; j < split.length; j++){
                    String[] insplit  = split[j].split(":");
                    if(insplit[0].equals("byr")){
                        boolean tru = true;
                        for(int k = 1; k <insplit[1].length(); k++){
                            if(insplit[1].charAt(k)< 48 || insplit[1].charAt(k)> 57){
                                tru = false;
                                break;
                            }
                        }
                        if(tru){
                            int leto = Integer.parseInt(insplit[1]);
    
                            if(leto >= 1920 && leto<= 2002)
                                check[0] = 1;   
                        }
                    }
                    else if(insplit[0].equals("iyr")){boolean tru = true;
                        for(int k = 1; k <insplit[1].length(); k++){
                            if(insplit[1].charAt(k)< 48 || insplit[1].charAt(k)> 57){
                                tru = false;
                                break;
                            }
                        }
                        if(tru){
                            int leto = Integer.parseInt(insplit[1]);
                            if(leto >= 2010 && leto<= 2020)
                                check[1] = 1;
                           
                        }
                        
                    }
                    else if(insplit[0].equals("eyr")){
                        boolean tru = true;
                        for(int k = 1; k <insplit[1].length(); k++){
                            if(insplit[1].charAt(k)< 48 || insplit[1].charAt(k)> 57){
                                tru = false;
                                break;
                            }
                        }
                        if(tru){
                            
                            int leto = Integer.parseInt(insplit[1]);
                            if(leto >= 2020 && leto<= 2030)
                                check[2] = 1;
                        }
                        
                    }
                    else if(insplit[0].equals("hgt")){
                        String st = "";
                        String mera = "";
                        for(int k = 0; k <insplit[1].length(); k++){
                            char c = insplit[1].charAt(k);
                            if(c >= 48 && c <= 57){
                                st = st.concat(String.valueOf(c));
                            }
                            else{
                                mera = mera.concat(String.valueOf(c));
                            }
                        }
                        int visina = Integer.parseInt(st);
                        if(mera.equals("cm")){
                            if(visina >= 150 && visina<= 193) check[3]= 1;
                        }
                        else if(mera.equals("in"))
                            if(visina >= 59 && visina<= 76) check[3]= 1;
                        //check[3] = 1;
                    }
                    else if(insplit[0].equals("hcl")){
                        if(insplit[1].charAt(0) == '#'){
                            boolean tru = true;
                            for(int k = 1; k <insplit[1].length(); k++){
                                if(insplit[1].charAt(k)< '0' || (insplit[1].charAt(k)> '9' && insplit[1].charAt(k)< 'a') || insplit[1].charAt(k)> 'f'){
                                    tru = false;
                                    break;
                                }
                            }
                            if(tru) check[4] = 1;
                        }
                        //check[4] = 1;
                    }
                    else if(insplit[0].equals("ecl")){
                        if(insplit[1].equals("amb") ||insplit[1].equals("blu") ||insplit[1].equals("brn") ||insplit[1].equals("gry") ||insplit[1].equals("grn") ||insplit[1].equals("hzl") ||insplit[1].equals("oth"))
                            check[5] = 1;
                    }
                    else if(insplit[0].equals("pid")){
                        boolean tru = true;
                            for(int k = 1; k <insplit[1].length(); k++){
                                if(insplit[1].charAt(k)< '0' || insplit[1].charAt(k)> '9'){
                                    tru = false;
                                    break;
                                }
                            }
                        if(tru)
                            check[6] = 1;
                    }
                    // else if(insplit[0].equals("cid")){
                    //     check[7] = 1;
                    // }
                }
            }
        }
        int ku = 0;
        for(int j  = 0; j <7; j++){
            if(check[j] ==1) ku++;
        }
        // if(ku == 8)ok++;
        // else if(ku ==  7 && check[7] == 0) ok++;
        if(ku == 7) ok++;                 
        System.out.println(ok);
        System.out.println(koliko);


        //part 2
        reader.close();
        sc.close();
    }
}
