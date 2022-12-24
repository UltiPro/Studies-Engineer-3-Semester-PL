DateTime startTime = DateTime.Now;

var ReadFile = new System.IO.StreamReader("dane1.txt");
int n,m=300;
n = Convert.ToInt32(ReadFile.ReadLine());

int[] numbers = new int[n];
string[] ints;

for(int i=0;i<n;i++)
{
    ints = ReadFile.ReadLine().Split();
    numbers[i]=Convert.ToInt32(ints[0]);
}

ReadFile.Close();

int[,] x = new int[n+1,m+1];

for(int i=0;i<n+1;i++)
{
    for(int j=0;j<m+1;j++)
    {
        x[i,j]=Select(i,j);
    }
}

int k=n,l=m,count=0;

while(k!=0&&l!=0)
{
    if(x[k,l]!=m+1) 
    {
        count = x[k,l];
        break;
    }
    else
    {
        k--;
        if(k==0) 
        {
            k=n;
            l--;
        }
    }
}

var WriteFile = new System.IO.StreamWriter("out.txt");

if(count!=0)
{
    int max=0,count_copy=count;

    while(count_copy>0)
    {
        if(x[k-1,l]==count_copy) k--;
        else
        {
            count_copy--;
            max+=numbers[k-1];
            l-=numbers[k-1];
            k--;
        }
    }
    WriteFile.WriteLine(max);
    WriteFile.WriteLine(count); 
}
else
{
    WriteFile.WriteLine("NIE");
}

WriteFile.Close();

DateTime stopTime = DateTime.Now;
TimeSpan roznica = stopTime - startTime;
Console.WriteLine("Czas pracy w [ms]: " + roznica.TotalMilliseconds);

// funkcja

int Select(int k, int l)
{
    if(k==0||l==0) return 0;
    if(k==1)
    {
        if(numbers[k-1]==l) return 1;
        else return m+1;
    }
    else
    {
        if(numbers[k-1]>l) return x[k-1,l];
        else if(numbers[k-1]==l) return 1;
        else
        {
            if(x[k-1,l-numbers[k-1]]+1<x[k-1,l]) return x[k-1,l-numbers[k-1]]+1;
            else return x[k-1,l];
        }
    }
}