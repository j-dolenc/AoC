
// C# program to print Hello World!
using System;
using System.IO;
using System.Threading.Tasks;
// namespace declaration
namespace HelloWorldApp {
      
    // Class declaration
    class Day2 {
          
        // Main Methods
        static void Main(string[] args) {
            string[] input = System.IO.File.ReadAllLines(@"C:\Users\jurij\OneDrive\Dokumenti\Advent Of Code\input20.txt");
            // statement
            // printing Hello World!
            int forward= 0;
            int depth = 0;
            int aim  =0;
            for(int i = 0; i < input.Length; i++){    
                string[] besedi =  input[i].Split(' ');
                Console.WriteLine(besedi[1]);
                if(besedi[0].Equals("up")){
                    //depth-=int.Parse(besedi[1]);
                    aim -=int.Parse(besedi[1]);
                }
                else if(besedi[0].Equals("forward")){
                    forward += int.Parse(besedi[1]);
                    depth+=int.Parse(besedi[1])*aim;
                }
                else if(besedi[0].Equals("down")){
                    //depth+=int.Parse(besedi[1]);
                    aim +=int.Parse(besedi[1]);
                }
            }
            int res = forward * depth;
            Console.WriteLine(forward*depth);
            // To prevents the screen from 
            // running and closing quickly
            //Console.ReadKey();
        }
    }
}