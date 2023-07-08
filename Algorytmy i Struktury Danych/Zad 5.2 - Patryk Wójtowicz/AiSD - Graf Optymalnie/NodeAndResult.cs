class Node
{
    int Destination, Distance;
    public Node(int Destination, int Distance)
    {
        this.Destination = Destination;
        this.Distance = Distance;
    }
    public int Dest { get { return Destination; } }
    public int Dist { get { return Distance; } }
}
class Result
{
    int[] Distance, Previous;
    public Result(int[] Distance, int[] Previous)
    {
        this.Distance = Distance;
        this.Previous = Previous;
    }
    public Result(Result ToCopy)
    {
        Distance = new int[ToCopy.D_Array.Length];
        Previous = new int[ToCopy.D_Array.Length];
        Array.Copy(ToCopy.D_Array, Distance, ToCopy.D_Array.Length);
        Array.Copy(ToCopy.P_Array, Previous, ToCopy.D_Array.Length);
    }
    public int[] D_Array { get { return Distance; } }
    public int[] P_Array { get { return Previous; } }
    public override string ToString()
    {
        string text = "";
        for (int i = 0; i < Distance.Length; i++) text += Distance[i] + " ";
        text += "\n";
        for (int i = 0; i < Previous.Length; i++) text += Previous[i] + " ";
        return text;
    }
}