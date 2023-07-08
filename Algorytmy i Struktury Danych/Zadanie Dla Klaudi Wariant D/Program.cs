DateTime startTime = DateTime.Now;

var ReadFile = new System.IO.StreamReader("dane1.txt");
int n, T = 3000;
n = Convert.ToInt32(ReadFile.ReadLine());

int[,] numbers = new int[n, 2];
string[] ints;

for (int i = 0; i < n; i++)
{
    ints = ReadFile.ReadLine().Split();
    numbers[i, 0] = Convert.ToInt32(ints[0]);
    numbers[i, 1] = Convert.ToInt32(ints[1]);
}

ReadFile.Close();

int[] wynik = new int[T + 1];

wynik[0] = 0;

for (int t = 1; t <= T; t++)
{
    wynik[t] = wynik[t - 1];
    for (int k = 0; k < n; k++)
    {
        if (t == numbers[k, 1])
        {
            if (wynik[t] < wynik[numbers[k, 0]] + (t - numbers[k, 0])) wynik[t] = wynik[numbers[k, 0]] + (t - numbers[k, 0]);
        }
    }
}

var WriteFile = new System.IO.StreamWriter("out.txt");

WriteFile.Write(wynik[T]);

WriteFile.Close();

DateTime stopTime = DateTime.Now;
TimeSpan roznica = stopTime - startTime;
Console.WriteLine("Czas pracy w [ms]: " + roznica.TotalMilliseconds);