using System;

namespace Bokforing
{
    class Bokforing
    {
        static void Main(string[] args)
        {
            string[] inputs = Console.ReadLine().Split(' ');
            int N = Int32.Parse(inputs[0]);
            int Q = Int32.Parse(inputs[1]);

            Console.WriteLine (N);
            Console.WriteLine (Q);
        }
    }
}
