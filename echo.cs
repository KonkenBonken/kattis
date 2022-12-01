using System;

namespace EchoEcho
{
    class Echo
    {
        static void Main(string[] args)
        {
            string phrase = Console.ReadLine();
            Console.WriteLine(phrase + " " + phrase + " " + phrase + " ");
        }
    }
}
