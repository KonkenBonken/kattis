using System;

namespace Alphabet
{
    class Spam
    {
        static void Main(string[] args)
        {
            string phrase = Console.ReadLine();

            double white = 0;
            double lower = 0;
            double upper = 0;
            double symbol = 0;

            for (int i = 0; i < phrase.Length; i++)
            {
                if (phrase[i] == '_')
                    white++;
                else if (char.IsLower(phrase[i]))
                    lower++;
                else if (char.IsUpper(phrase[i]))
                    upper++;
                else
                    symbol++;
            }

            Console.WriteLine(white / phrase.Length);
            Console.WriteLine(lower / phrase.Length);
            Console.WriteLine(upper / phrase.Length);
            Console.WriteLine(symbol / phrase.Length);
        }
    }
}
