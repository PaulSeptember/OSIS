using System;
using System.Collections.Generic;
using System.IO;

namespace ConsoleApp2
{
    class Program
    {      
        static void Main(string[] args) {
            string p = "D:\\";
            string r = "C:\\Users\\37529\\Downloads\\OSiS-Labs-master\\OSiS-Labs-master\\lab1\\ConsoleApp2\\result.txt";
            Console.WriteLine($"Searching files on {p} drive...");
            string[] fD = Directory.GetDirectories(p);
            string pR = "\nFounded files on " + p + " :\n";
            List<string> fF = new List<string>();
            foreach (string folder in fD)
                try
                {
                    string[] files = Directory.GetFiles(folder, "*HJSAFl*" + "*.txt", SearchOption.AllDirectories);
                    foreach (string file in files)
                    {
                        pR += file + "\n";
                        fF.Add(file);
                    }
                }
                catch
                {
                    Console.WriteLine("Access denied: " + folder);
                }
            if (fF.Count != 0)
                Console.WriteLine(pR);
            else
                Console.WriteLine("\nNothing found in this directory");
            List<string> ans = new List<string>();
            foreach (string file in fF)
                ans.AddRange(File.ReadAllLines(file));
            File.AppendAllLines(r, ans);
            Console.ReadKey();
        }
    }
}
