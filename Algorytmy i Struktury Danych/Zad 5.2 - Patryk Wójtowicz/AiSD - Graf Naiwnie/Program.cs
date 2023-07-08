var ReadFile = new System.IO.StreamReader("dane1.txt");

string[] ints = ReadFile.ReadLine().Split();

int c = Convert.ToInt32(ints[0]);
int r = Convert.ToInt32(ints[1]);
int pr = Convert.ToInt32(ints[2]);

int[,] neighbor_array = new int[c, c];

for (int i = 0; i < r; i++)
{
    ints = ReadFile.ReadLine().Split();
    neighbor_array[Convert.ToInt32(ints[0]) - 1, Convert.ToInt32(ints[1]) - 1] = Convert.ToInt32(ints[2]);
    neighbor_array[Convert.ToInt32(ints[1]) - 1, Convert.ToInt32(ints[0]) - 1] = Convert.ToInt32(ints[2]);
}

int[,] neighbor_array_copy = new int[c, c];

Array.Copy(neighbor_array, neighbor_array_copy, (c * c));

int[,] possible_road = new int[pr, 3];

for (int i = 0; i < pr; i++)
{
    ints = ReadFile.ReadLine().Split();
    possible_road[i, 0] = Convert.ToInt32(ints[0]);
    possible_road[i, 1] = Convert.ToInt32(ints[1]);
    possible_road[i, 2] = Convert.ToInt32(ints[2]);
}

ReadFile.Close();

bool[] visited = new bool[c];
int[] distance = new int[c];
int[] previous = new int[c];

Dijkstra();

bool[] visited_copy = new bool[c];
int[] distance_copy = new int[c];
int[] previous_copy = new int[c];

Array.Copy(visited, visited_copy, c);
Array.Copy(distance, distance_copy, c);
Array.Copy(previous, previous_copy, c);

var WriteFile = new System.IO.StreamWriter("out.txt");

for (int i = 0; i < pr; i++)
{
    Array.Copy(neighbor_array_copy, neighbor_array, (c * c));

    neighbor_array[possible_road[i, 0] - 1, possible_road[i, 1] - 1] = possible_road[i, 2];
    neighbor_array[possible_road[i, 1] - 1, possible_road[i, 0] - 1] = possible_road[i, 2];

    Dijkstra();

    int count = 0;
    for (int j = 0; j < c; j++)
    {
        if (distance[j] < distance_copy[j]) count++;
        if (count == 100) break;
    }
    if (count == 100) WriteFile.WriteLine("100+");
    else WriteFile.WriteLine(count);
}

WriteFile.Close();

void Dijkstra()
{
    Array.Clear(visited);
    for (int i = 0; i < c; i++)
    {
        distance[i] = int.MaxValue;
        previous[i] = -1;
    }

    distance[0] = 0;

    while (IsNotVisited(visited))
    {
        int v = TopOfLowestValueNotVisited(distance, visited);
        visited[v] = true;
        for (int i = 0; i < c; i++)
        {
            if (neighbor_array[v, i] != 0 && distance[v] + neighbor_array[v, i] < distance[i])
            {
                distance[i] = distance[v] + neighbor_array[v, i];
                previous[i] = v;
            }
        }
    }
}

bool IsNotVisited(bool[] visited)
{
    for (int i = 0; i < c; i++)
    {
        if (!visited[i]) return true;
    }
    return false;
}

int TopOfLowestValueNotVisited(int[] distance, bool[] visited)
{
    int min = int.MaxValue;
    int minIndex = 0;

    for (int i = 0; i < c; i++)
    {
        if (visited[i] == false && distance[i] <= min)
        {
            min = distance[i];
            minIndex = i;
        }
    }

    return minIndex;
}