using System;
using System.Collections.Generic;

namespace Enterprise
{
    class Program
    {
        static List<int> QuickSortOfList(List<int> list) // n * log(n)
        {
            if (list.Count <= 1) return list;
            List<int> left = new List<int>();
            List<int> right = new List<int>();
            for (int i = 0; i < list.Count; i++)
            {
                if (i == list.Count / 2) continue;
                if (list[i] < list[list.Count / 2])
                {
                    left.Add(list[i]);
                }
                else
                {
                    right.Add(list[i]);
                }
            }
            List<int> sorted = QuickSortOfList(left);
            sorted.Add(list[list.Count / 2]);
            sorted.AddRange(QuickSortOfList(right));
            return sorted;
        }
        static void Main(string[] args)
        {
            int AllDegreeinMinutes = 360 * 60, ShootDegreeinMuntes = 90 * 60, count = 0, bufor = 1;
            System.IO.StreamReader ReadFile = new System.IO.StreamReader("in4.txt");
            int n = Convert.ToInt32(ReadFile.ReadLine());
            List<int> ListOfMinutes = new List<int>();
            for (int i = 0; i < n; i++) // liniowa n
            {
                string[] ints = ReadFile.ReadLine().Split();
                ListOfMinutes.Add(Int32.Parse(ints[0]) * 60 + Int32.Parse(ints[1]));
            }
            ReadFile.Close();
            ListOfMinutes = QuickSortOfList(ListOfMinutes);
            for (int i = 0; i < n; i++)
            {
                for (int j = i + 1; j < n; j++) // n(n-1) -> n^2 - n
                {
                    if (ListOfMinutes[i] + ShootDegreeinMuntes >= ListOfMinutes[j] && ListOfMinutes[i] <= ListOfMinutes[j])
                    {
                        bufor++;
                    }
                    else if (ListOfMinutes[i] + ShootDegreeinMuntes < ListOfMinutes[j])
                    {
                        break;
                    }
                }
                if (ListOfMinutes[i] > AllDegreeinMinutes - ShootDegreeinMuntes)
                {
                    for (int h = 0; h < n; h++) // + n
                    {
                        if (ListOfMinutes[h] <= Math.Abs(AllDegreeinMinutes - ListOfMinutes[i] - ShootDegreeinMuntes))
                        {
                            bufor++;
                        }
                        else if (ListOfMinutes[h] > Math.Abs(AllDegreeinMinutes - ListOfMinutes[i] - ShootDegreeinMuntes))
                        {
                            break;
                        }
                    }
                }
                if (count < bufor) count = bufor;
                bufor = 1;
            }
            System.IO.StreamWriter WriteFile = new System.IO.StreamWriter("out.txt");
            WriteFile.Write(count);
            WriteFile.Close();
        }
    }
}