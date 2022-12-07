
// C# program to print Hello World!
using System;
using System.IO;
using System.Threading.Tasks;
using System.Collections.Generic;
// namespace declaration
namespace HelloWorldApp {
      
    // Class declaration
    class Day2 {
          
        // Main Methods
        static void Main(string[] args) {
            string[] input = System.IO.File.ReadAllLines(@"C:\Users\jurij\OneDrive\Dokumenti\Advent Of Code\input3.txt");
            // statement
            // printing Hello World!
            //string max = "";
            
            
            //string res1 = "";
            //string res2 = "";
            int nule =0;
            int enke  =0;
            List<string> zrak = new List<string>();
            List<string> codva = new List<string>();
            for(int i  = 0; i < input.Length; i++){
                string beseda = input[i];   
                zrak.Add(beseda);
                codva.Add(beseda);
            }
            int index = 0;

            while(zrak.Count != 1){
                nule =0;
                enke  =0;
                for(int i = 0; i < zrak.Count; i++){ 
                    string beseda = zrak[i];   
                    if(beseda[index].Equals('1')){
                        enke ++;
                    }
                    else if(beseda[index].Equals('0')) {
                        nule++;
                    }
                }

                if(enke >= nule){
                    for(int i  = 0; i < zrak.Count; i++){
                        string beseda = zrak[i];   
                        if(beseda[index].Equals('0')){
                            zrak.Remove(zrak[i]);
                            i--;
                        }
                    }
                }
                else {
                    for(int i  = 0; i < zrak.Count; i++){
                        if(zrak[i][index].Equals('1')){
                            zrak.Remove(zrak[i]);
                            i--;
                        }
                    }
                }
                index++;
                if(index == 12) break;
            }
            index = 0;
            while(codva.Count != 1){
                nule =0;
                enke  =0;
                for(int i = 0; i < codva.Count; i++){ 
                    string beseda = codva[i];   
                    if(beseda[index].Equals('1')){
                        enke ++;
                    }
                    else if(beseda[index].Equals('0')) {
                        nule++;
                    }
                }

                if(nule<=enke){
                    for(int i  = 0; i < codva.Count; i++){
                        string beseda = codva[i];   
                        if(beseda[index].Equals('1')){
                            codva.Remove(codva[i]);
                            i--;
                        }
                    }
                }
                else {
                    for(int i  = 0; i < codva.Count; i++){
                        if(codva[i][index].Equals('0')){
                            codva.Remove(codva[i]);
                            i--;
                        }
                    }
                }
                index++;
                if(index == 12) break;
            }
            

            Console.WriteLine(zrak.Count);
            Console.WriteLine(codva.Count);
            for(int i  = 0; i <zrak.Count; i++){
                Console.WriteLine(zrak[i]);
            }
             for(int i  = 0; i <codva.Count; i++){
                Console.WriteLine(codva[i]);
            }
            int zr = Convert.ToInt32(zrak[0],2);
            int co = Convert.ToInt32(codva[0],2);
            Console.WriteLine(zr*co);
            Console.WriteLine(co);
            // To prevents the screen from 
            // running and closing quickly
            //Console.ReadKey();
        }
    }
}