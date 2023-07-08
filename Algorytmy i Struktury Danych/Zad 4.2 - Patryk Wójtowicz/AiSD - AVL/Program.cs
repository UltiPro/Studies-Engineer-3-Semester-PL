var ReadFile = new System.IO.StreamReader("dane2.txt");
int n = Convert.ToInt32(ReadFile.ReadLine());

char[] operations = new char[n];
int[,] numbers = new int[n, 2];
string[] ints;

for (int i = 0; i < n; i++)
{
    ints = ReadFile.ReadLine().Split();
    operations[i] = Convert.ToChar(ints[0]);
    numbers[i, 0] = Convert.ToInt32(ints[1]);
    if (ints.Length == 3) numbers[i, 1] = Convert.ToInt32(ints[2]);
    else numbers[i, 1] = -1;
}

ReadFile.Close();

AVL tree = new AVL();

var WriteFile = new System.IO.StreamWriter("out.txt");

for (int i = 0; i < n; i++)
{
    switch (operations[i])
    {
        case 'W': tree.Add(numbers[i, 0]); break;
        case 'U': tree.Remove(numbers[i, 0]); break;
        case 'S':
            if (tree.Find(numbers[i, 0])) WriteFile.WriteLine("TAK");
            else WriteFile.WriteLine("NIE");
            break;
        case 'L': WriteFile.WriteLine(tree.GetCount(numbers[i, 0], numbers[i, 1])); break;
    }
}

WriteFile.Close();

//tree.PrintTree();