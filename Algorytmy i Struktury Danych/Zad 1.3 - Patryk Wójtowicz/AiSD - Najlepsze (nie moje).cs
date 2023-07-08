using System;
using System.Diagnostics;
using System.IO;

namespace Szybki
{
    class Szybki
    {
        static void Main(string[] args)
        {
            #region Pobranie danych do tabeli
            StreamReader file = new(@"C:\test.txt");
            int amount = int.Parse(file.ReadLine());
            int[,] initialdata = new int[amount, 2];
            for (int i = 0; i < amount; i++)
            {
                string[] XY = file.ReadLine().Split(' ');
                initialdata[i, 0] = Convert.ToInt32(XY[0]);
                initialdata[i, 1] = Convert.ToInt32(XY[1]);
            }
            file.Close();
            #endregion

            decimal sum = 0, trials = 1;

            for (int o = 0; o < trials; o++)
            {
                Stopwatch stopWatch = new();
                stopWatch.Start();
                int[] places = new int[21600];

                for (int i = 0; i < amount; i++)
                {
                    places[initialdata[i, 0] * 60 + initialdata[i, 1]]++;
                }

                int answer, current = 0, index = 0;

                while (index < 5401)
                {
                    current += places[index++];
                }
                answer = current;
                for (index = 0; index < 16199; index++)
                {
                    current += places[index + 5401] - places[index];
                    if (current > answer) answer = current;
                }
                for (index = 0; index < 5399; index++)
                {
                    current += places[index] - places[index + 16200];
                    if (current > answer) answer = current;
                }

                stopWatch.Stop();
                sum += stopWatch.ElapsedMilliseconds;
                Console.WriteLine(answer);
            }
            Console.WriteLine(sum / trials);
            Console.ReadKey();
        }
    }
}