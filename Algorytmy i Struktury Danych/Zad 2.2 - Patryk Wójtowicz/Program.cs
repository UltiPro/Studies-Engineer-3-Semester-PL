DateTime startTime = DateTime.Now;

var ReadFile = new System.IO.StreamReader("dane5.txt");

string[] ints = ReadFile.ReadLine().Split();

int n = Convert.ToInt32(ints[0]);
int m = Convert.ToInt32(ints[1]);
int d = Convert.ToInt32(ints[2]);

bool[,,] cave = new bool[n, m, d];
bool select = true;
int deep_cave = 0, max_deep_cave = 0, counter = 0, max_size = 0, closed_caves = 0;
string buf = "";

for (int i = 0; i < d * n; i++)
{
    buf = ReadFile.ReadLine();
    if (i % n == 0 && i != 0)
    {
        deep_cave++;
        buf = ReadFile.ReadLine();
    }
    for (int j = 0; j < m; j++)
    {
        if (buf[j] == 'x') cave[i % n, j, deep_cave] = false;
        else cave[i % n, j, deep_cave] = true;
    }
}

ReadFile.Close();

void cave_rec(int x, int y, int z)
{
    cave[x, y, z] = false;
    counter++;
    if ((x - 1) >= 0 && cave[x - 1, y, z] == true) cave_rec(x - 1, y, z);
    if ((x + 1) < n && cave[x + 1, y, z] == true) cave_rec(x + 1, y, z);
    if ((y - 1) >= 0 && cave[x, y - 1, z] == true) cave_rec(x, y - 1, z);
    if ((y + 1) < m && cave[x, y + 1, z] == true) cave_rec(x, y + 1, z);
    if ((z - 1) >= 0 && cave[x, y, z - 1] == true) cave_rec(x, y, z - 1);
    if ((z + 1) < d && cave[x, y, z + 1] == true)
    {
        if (select && deep_cave <= z + 2) deep_cave = z + 2;
        cave_rec(x, y, z + 1);
    }
}

for (int i = 0; i < d; i++) // D * N * M -> pseudowielomianowa
{
    for (int j = 0; j < m; j++)
    {
        for (int k = 0; k < n; k++)
        {
            if (cave[k, j, i] == true)
            {
                counter = 0;
                deep_cave = 0;
                if (i != 0) closed_caves++;
                cave_rec(k, j, i);
                if (max_size < counter) max_size = counter;
                if (max_deep_cave < deep_cave) max_deep_cave = deep_cave;
                /*
					var thread = new Thread( _ => cave_rec(k,j,i), 2000000);
					thread.Start();
					thread.Join();
				*/
            }
        }
    }
    select = false;
}

var WriteFile = new System.IO.StreamWriter("out.txt");

WriteFile.Write(max_deep_cave + " " + max_size + " " + closed_caves);

WriteFile.Close();

DateTime stopTime = DateTime.Now;
TimeSpan roznica = stopTime - startTime;
Console.WriteLine("Czas pracy w [ms]: " + roznica.TotalMilliseconds);