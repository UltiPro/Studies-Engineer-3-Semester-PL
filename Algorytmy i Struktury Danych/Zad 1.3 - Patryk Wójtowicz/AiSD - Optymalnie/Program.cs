using System;
using System.Collections.Generic;

namespace Enterprise
{
    class Program
    {
        static int IndexOfBinnary(List<int> list,int n,int search) // log2(n)
        {
            int left = 0, right = n-1, middle = 0;
            while(left<=right)
            {
                middle = (left+right)/2;
                if(list[middle] == search)
                {
                    if(middle == n-1) break;
                    if(list[middle+1]==search) left = middle + 1;
                    else break;
                }
                else if(list[middle] < search) left = middle + 1;
                else right = middle - 1;
            }
            if(list[middle]>search) return middle;
            else return middle + 1;
        }
        static List<int> QuickSortOfList(List<int> list) // n * log(n)
        {
            if(list.Count<=1) return list;
            List<int> left = new List<int>();
            List<int> right = new List<int>();
            for(int i=0;i<list.Count;i++)
            {
                if(i==list.Count/2) continue;
                if(list[i]<list[list.Count/2])
                {
                    left.Add(list[i]);
                }
                else
                {
                    right.Add(list[i]);
                }
            }
            List<int> sorted = QuickSortOfList(left);
            sorted.Add(list[list.Count/2]);
            sorted.AddRange(QuickSortOfList(right));
            return sorted;
        }
        static void Main(string[] args)
        {
            int AllDegreeinMinutes = 360*60, ShootDegreeinMintes = 90*60, count = 0, bufor = 0;
            System.IO.StreamReader ReadFile = new System.IO.StreamReader("in5.txt");
            int n = Convert.ToInt32(ReadFile.ReadLine());
            List<int> ListOfMinutes = new List<int>();   
            for(int i=0;i<n;i++) // liniowa n
            {
                string[] ints = ReadFile.ReadLine().Split();
                ListOfMinutes.Add(Int32.Parse(ints[0])*60+Int32.Parse(ints[1]));
            }
            ReadFile.Close();
            ListOfMinutes=QuickSortOfList(ListOfMinutes); 
            for(int i=0;i<n;i++) // liniowa n
            {
                bufor = IndexOfBinnary(ListOfMinutes,n,ListOfMinutes[i]+ShootDegreeinMintes) - i;
                if(ListOfMinutes[i]>AllDegreeinMinutes-ShootDegreeinMintes)
                {
                    bufor = bufor + IndexOfBinnary(ListOfMinutes,n,Math.Abs(AllDegreeinMinutes-ListOfMinutes[i]-ShootDegreeinMintes));
                }
                if(count<bufor) count = bufor;
                bufor = 0;
            }
            System.IO.StreamWriter WriteFile = new System.IO.StreamWriter("out.txt");
            WriteFile.Write(count);
            WriteFile.Close();
        }
    }
}