
// C# program to print Hello World!
using System;
using System.IO;
using System.Threading.Tasks;
// namespace declaration
namespace HelloWorldApp {
      
    // Class declaration
    class Day1 {
          
        // Main Method
        static void Main(string[] args) {
            string[] input = System.IO.File.ReadAllLines(@"C:\Users\jurij\OneDrive\Dokumenti\Advent Of Code\input10.txt");
            // statement
            // printing Hello World!
            Console.WriteLine("Hello World!");
            System.Console.WriteLine("Contents of WriteLines2.txt = ");
            int index= 0;
            for(int i = 1; i < input.Length-2; i++){    
                if(int.Parse(input[i]) + int.Parse(input[i+1]) +int.Parse(input[i+2]) >int.Parse(input[i-1])+int.Parse(input[i])+int.Parse(input[i+1])){
                    index++;
                }
            }
            Console.WriteLine(index);
            // To prevents the screen from 
            // running and closing quickly
            //Console.ReadKey();
        }
    }
}