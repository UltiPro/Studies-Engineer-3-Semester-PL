class AVL
{
    Node root;
    public void Add(int number)
    {
        if (root == null) root = new Node(number);
        else root = AddRecursive(root, number);
    }
    private Node AddRecursive(Node current, int number)
    {
        if (current == null) current = new Node(number);
        else if (number < current.Number) current.leftNode = AddRecursive(current.leftNode, number);
        else if (number > current.Number) current.rightNode = AddRecursive(current.rightNode, number);
        return current = BalanceTree(current);
    }
    private Node BalanceTree(Node current)
    {
        current.CalculateHeight();
        if (current.CalculateBalance() > 1)
        {
            if (current.leftNode.CalculateBalance() == 1) current = CaseLL(current);
            else current = CaseLR(current);
        }
        else if (current.CalculateBalance() < -1)
        {
            if (current.rightNode.CalculateBalance() == -1) current = CaseRR(current);
            else current = CaseRL(current);
        }
        current.CalculateNodes();
        return current;
    }
    private Node CaseRR(Node parent)
    {
        Node newNode = parent.rightNode;
        parent.rightNode = newNode.leftNode;
        newNode.leftNode = parent;
        parent.CalculateHeight();
        newNode.CalculateHeight();
        parent.CalculateNodes();
        newNode.CalculateNodes();
        return newNode;
    }
    private Node CaseLL(Node parent)
    {
        Node newNode = parent.leftNode;
        parent.leftNode = newNode.rightNode;
        newNode.rightNode = parent;
        parent.CalculateHeight();
        newNode.CalculateHeight();
        parent.CalculateNodes();
        newNode.CalculateNodes();
        return newNode;
    }
    private Node CaseLR(Node parent)
    {
        parent.leftNode = CaseRR(parent.leftNode);
        return CaseLL(parent);
    }
    private Node CaseRL(Node parent)
    {
        parent.rightNode = CaseLL(parent.rightNode);
        return CaseRR(parent);
    }
    public void Remove(int number)
    {
        root = RemoveRecursive(root, number);
    }
    private Node RemoveRecursive(Node current, int number)
    {
        if (number < current.Number && current.leftNode != null) current.leftNode = RemoveRecursive(current.leftNode, number);
        else if (number > current.Number && current.rightNode != null) current.rightNode = RemoveRecursive(current.rightNode, number);
        else if (number == current.Number)
        {
            if (current.rightNode != null) current.rightNode = GetNext(current, current.rightNode);
            else return current.leftNode;
        }
        return current = BalanceTree(current);
    }
    private Node GetNext(Node ToSet, Node current)
    {
        if (current.leftNode != null)
        {
            current.leftNode = GetNext(ToSet, current.leftNode);
            return current = BalanceTree(current);
        }
        else
        {
            ToSet.Number = current.Number;
            if (current.rightNode != null)
            {
                current = current.rightNode;
                return current;
            }
            return null;
        }
    }
    public bool Find(int number)
    {
        if (root.Find(number) != null) return true;
        else return false;
    }
    public int GetCount(int number1, int number2)
    {
        return root.Nodes - GetLowerThan(root, number1 - 1) - GetHigherThan(root, number2 + 1);
    }
    private int GetLowerThan(Node current, int number)
    {
        if (current.Number == number && current.leftNode != null) return current.leftNode.Nodes + 1;
        if (current.Number == number && current.leftNode == null) return 1;
        if (current.Number < number && current.leftNode != null && current.rightNode != null) return current.leftNode.Nodes + 1 + GetLowerThan(current.rightNode, number);
        if (current.Number < number && current.leftNode != null && current.rightNode == null) return current.leftNode.Nodes + 1;
        if (current.Number < number && current.leftNode == null && current.rightNode != null) return 1 + GetLowerThan(current.rightNode, number);
        if (current.Number < number && current.leftNode == null && current.rightNode == null) return 1;
        if (current.Number > number && current.leftNode != null) return GetLowerThan(current.leftNode, number);
        return 0;
    }
    private int GetHigherThan(Node current, int number)
    {
        if (current.Number == number && current.rightNode != null) return current.rightNode.Nodes + 1;
        if (current.Number == number && current.rightNode == null) return 1;
        if (current.Number > number && current.rightNode != null && current.leftNode != null) return current.rightNode.Nodes + 1 + GetHigherThan(current.leftNode, number);
        if (current.Number > number && current.rightNode != null && current.leftNode == null) return current.rightNode.Nodes + 1;
        if (current.Number > number && current.rightNode == null && current.leftNode != null) return 1 + GetHigherThan(current.leftNode, number);
        if (current.Number > number && current.rightNode == null && current.leftNode == null) return 1;
        if (current.Number < number && current.rightNode != null) return GetHigherThan(current.rightNode, number);
        return 0;
    }
    public void PrintTree()
    {
        root.PrintTree("", true);
    }
}