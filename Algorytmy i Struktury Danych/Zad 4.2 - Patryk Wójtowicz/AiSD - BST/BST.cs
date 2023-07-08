class BST
{
    Node root;
    public Node Root()
    {
        return root;
    }
    public void Add(int value)
    {
        if (root != null) root.Add(value);
        else root = new Node(value);
    }
    public Node Find(int value)
    {
        if (root != null) return root.Find(value);
        else return null;
    }
    public void Remove(int value)
    {
        if (root == null)
        {
            return;
        }
        Node current = root;
        Node parent = root;
        bool isLeftChild = false;
        while (current != null && current.Number() != value)
        {
            parent = current;
            if (value < current.Number())
            {
                current = current.leftNode;
                isLeftChild = true;
            }
            else
            {
                current = current.rightNode;
                isLeftChild = false;
            }
        }
        if (current == null) return;
        if (current.rightNode == null && current.leftNode == null)
        {
            if (current == root)
            {
                root = null;
            }
            else
            {
                if (isLeftChild) parent.leftNode = null;
                else parent.rightNode = null;
            }
        }
        else if (current.rightNode == null)
        {
            if (current == root) root = current.leftNode;
            else
            {
                if (isLeftChild) parent.leftNode = current.leftNode;
                else parent.rightNode = current.leftNode;
            }
        }
        else if (current.leftNode == null)
        {
            if (current == root) root = current.rightNode;
            else
            {
                if (isLeftChild) parent.leftNode = current.rightNode;
                else parent.rightNode = current.rightNode;
            }
        }
        else
        {
            Node next = GetNext(current);
            if (current == root) root = next;
            else if (isLeftChild) parent.leftNode = next;
            else parent.rightNode = next;
        }
    }
    Node GetNext(Node node)
    {
        Node ParentOfNext = node, next = node, current = node.rightNode;
        while (current != null)
        {
            ParentOfNext = next;
            next = current;
            current = current.leftNode;
        }
        if (next != node.rightNode)
        {
            ParentOfNext.leftNode = next.rightNode;
            next.rightNode = node.rightNode;
        }
        next.leftNode = node.leftNode;
        return next;
    }
    public int GetCount(int value1, int value2)
    {
        int count = 0;
        for (int i = value1; i <= value2; i++)
        {
            if (Find(i) != null) count++;
        }
        return count;
    }
    public void PrintTree()
    {
        root.PrintTree("", true);
    }
}