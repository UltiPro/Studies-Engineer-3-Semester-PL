class Node
{
    private int number, height, CountOfNodes;
    private Node left, right;
    public Node(int number)
    {
        this.number = number;
        height = 1;
        CountOfNodes = 1;
    }
    public int Number
    {
        get { return number; }
        set { number = value; }
    }
    public Node leftNode
    {
        get { return left; }
        set { left = value; }
    }
    public Node rightNode
    {
        get { return right; }
        set { right = value; }
    }
    public int Nodes
    {
        get { return CountOfNodes; }
    }
    public void CalculateHeight()
    {
        int lh = 0, rh = 0;
        if (left != null) lh = left.height;
        if (right != null) rh = right.height;
        height = Math.Max(lh, rh) + 1;
    }
    public int CalculateBalance()
    {
        int lh = 0, rh = 0;
        if (left != null) lh = left.height;
        if (right != null) rh = right.height;
        return lh - rh;
    }
    public void CalculateNodes()
    {
        int ln = 0, rn = 0;
        if (left != null) ln = left.CountOfNodes;
        if (right != null) rn = right.CountOfNodes;
        CountOfNodes = ln + rn + 1;
    }
    public Node Find(int number)
    {
        if (number < this.number && left != null)
        {
            return left.Find(number);
        }
        else if (number > this.number && right != null)
        {
            return right.Find(number);
        }
        else if (number == this.number)
        {
            return this;
        }
        return null;
    }
    public void PrintTree(string bufor, bool last)
    {
        Console.Write(bufor);
        if (last)
        {
            Console.Write("└─");
            bufor += "  ";
        }
        else
        {
            Console.Write("├─");
            bufor += "| ";
        }
        Console.WriteLine(number + ":" + height + ":" + CountOfNodes);
        int i = 0, j = 0;
        if (left != null) j++;
        if (right != null) j++;
        if (left != null)
        {
            left.PrintTree(bufor, i == j - 1);
            i++;
        }
        if (right != null) right.PrintTree(bufor, i == j - 1);
    }
}