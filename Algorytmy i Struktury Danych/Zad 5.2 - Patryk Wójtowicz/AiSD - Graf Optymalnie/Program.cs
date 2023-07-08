#pragma warning disable 8602

var ReadFile = new System.IO.StreamReader("dane1.txt");

string[] ints = ReadFile.ReadLine().Split();

int c = Convert.ToInt32(ints[0]);
int r = Convert.ToInt32(ints[1]);
int pr = Convert.ToInt32(ints[2]);

List<Node>[] graph = new List<Node>[c];

for (int i = 0; i < c; i++) graph[i] = new List<Node>();

for (int i = 0; i < r; i++)
{
    ints = ReadFile.ReadLine().Split();
    graph[Convert.ToInt32(ints[0]) - 1].Add(new Node(Convert.ToInt32(ints[1]) - 1, Convert.ToInt32(ints[2])));
    graph[Convert.ToInt32(ints[1]) - 1].Add(new Node(Convert.ToInt32(ints[0]) - 1, Convert.ToInt32(ints[2])));
}

Result result = Dijkstra(c, graph, 0);

Result result_copy = new Result(result);

var WriteFile = new System.IO.StreamWriter("out.txt");

for (int i = 0; i < pr; i++)
{
    ints = ReadFile.ReadLine().Split();

    bool AnyCorrections = CheckToCorrect(result, Convert.ToInt32(ints[0]) - 1, Convert.ToInt32(ints[1]) - 1, Convert.ToInt32(ints[2]));

    if (AnyCorrections)
    {
        int count = 0;
        for (int j = 0; j < c; j++)
        {
            if (result.D_Array[j] != result_copy.D_Array[j]) count++;
            if (count == 100) break;
        }
        if (count == 100) WriteFile.WriteLine("100+");
        else WriteFile.WriteLine(count);
    }
    else WriteFile.WriteLine(0);

    if (AnyCorrections) result = new Result(result_copy);
}

ReadFile.Close();
WriteFile.Close();

// funkcje

Result Dijkstra(int CountOfNodes, List<Node>[] Graph, int Capital)
{
    int[] Distance = new int[CountOfNodes];
    int[] Previous = new int[CountOfNodes];

    for (int i = 0; i < CountOfNodes; i++) Distance[i] = int.MaxValue;

    Distance[Capital] = 0;
    Previous[Capital] = -1;

    PriorityQueue<Node, int> queue = new PriorityQueue<Node, int>();

    queue.Enqueue(new Node(Capital, 0), 0);

    while (queue.Count > 0)
    {
        Node current = queue.Dequeue();
        foreach (Node n in graph[current.Dest])
        {
            if (Distance[current.Dest] + n.Dist < Distance[n.Dest])
            {
                Distance[n.Dest] = Distance[current.Dest] + n.Dist;
                Previous[n.Dest] = current.Dest;
                queue.Enqueue(new Node(n.Dest, Distance[n.Dest]), Distance[n.Dest]);
            }
        }
    }

    return new Result(Distance, Previous);
}

bool CheckToCorrect(Result result, int From, int To, int Distance)
{
    if (result.D_Array[From] + Distance < result.D_Array[To])
    {
        CorrectRoute(result, From, To, Distance);
        return true;
    }
    else if (result.D_Array[To] + Distance < result.D_Array[From])
    {
        CorrectRoute(result, To, From, Distance);
        return true;
    }
    return false;
}

void CorrectRoute(Result result, int From, int To, int Distance)
{
    if (result.D_Array[From] + Distance < result.D_Array[To])
    {
        result.D_Array[To] = result.D_Array[From] + Distance;
        result.P_Array[To] = From;
        for (int i = 0; i < graph[To].Count; i++)
        {
            CorrectRoute(result, To, graph[To][i].Dest, graph[To][i].Dist);
        }
    }
}