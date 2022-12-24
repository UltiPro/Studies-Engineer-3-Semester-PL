var ReadFile = new System.IO.StreamReader("dane8.txt");
int n,m=100;
n = Convert.ToInt32(ReadFile.ReadLine());

int[,] numbers = new int[n,3];
string[] ints;

for(int i=0;i<n;i++)
{
    ints = ReadFile.ReadLine().Split();
    numbers[i,0]=Convert.ToInt32(ints[0]);
    numbers[i,1]=Convert.ToInt32(ints[1]);
    numbers[i,2]=Convert.ToInt32(ints[2]);
}

ReadFile.Close();

int[,,] tab = new int[m+1,m+1,m+1];
int[,,] pom = new int[m+1,m+1,m+1];

for(int i=0;i<n;i++)
{
    for(int j=0;j<m+1;j++)
    {
        for(int k=0;k<m+1;k++)
        {
            for(int l=0;l<m+1;l++)
            {
                tab[j,k,l]=Select(i,j,k,l);
            }
        }
    }
    pom=(int[,,])tab.Clone();
}

int y=m,count=0;

while(true)
{
    if(y==0) break;
    if(tab[y,y,y]!=m+1) 
    {
        count = tab[y,y,y];
        break;
    }
    y--;
}

int max=y*3;

var WriteFile = new System.IO.StreamWriter("out.txt");

if(count==0)
{
    WriteFile.WriteLine("NIE");
}
else
{
    WriteFile.WriteLine(max);
    WriteFile.WriteLine(count);
}

WriteFile.Close();

int Select(int i, int j, int k, int l)
{
    if(i==0)
    {
        if(numbers[i,0]==j&&numbers[i,1]==k&&numbers[i,2]==l) return 1;
        else return m+1;
    }
    else
    {
        if(numbers[i,0]==j&&numbers[i,1]==k&&numbers[i,2]==l) return 1;  
        else if(numbers[i,0]<=j&&numbers[i,1]<=k&&numbers[i,2]<=l)
        {
            if(pom[j-numbers[i,0],k-numbers[i,1],l-numbers[i,2]]+1<pom[j,k,l]) return pom[j-numbers[i,0],k-numbers[i,1],l-numbers[i,2]]+1;
            else return pom[j,k,l];
        }
        else 
        {
            return pom[j,k,l];
        }
    }
}