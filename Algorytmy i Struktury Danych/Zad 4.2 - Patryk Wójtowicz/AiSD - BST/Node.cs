class Node
{
    int number;
    Node left, right;
    public Node(int number)
    {
        this.number = number;
    }
    public int Number()
    {
        return number;
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
    public void Add(int value)
    {
        if (value > number)
        {
            if (rightNode == null) rightNode = new Node(value);
            else rightNode.Add(value);
        }
        else if (value < number)
        {
            if (leftNode == null) leftNode = new Node(value);
            else leftNode.Add(value);
        }
    }
    public Node Find(int value)
    {
        if (number == value) return this;
        else if (number > value && leftNode != null) return leftNode.Find(value);
        else if (number < value && rightNode != null) return rightNode.Find(value);
        else return null;
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
        Console.WriteLine(number);
        int i=0,j=0;
        if (this.left != null) j++;
        if (this.right != null) j++;
        if (this.left != null) 
        {
            this.left.PrintTree(bufor,i==j-1);
            i++;
        }
        if (this.right != null) this.right.PrintTree(bufor,i==j-1);
    }
}
