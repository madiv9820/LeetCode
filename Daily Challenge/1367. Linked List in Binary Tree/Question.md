<div style = "font-size: 18px; font-family: Times New Roman">
    <h1 style = "font-size: 40px">
        1367. Linked List in Binary Tree
    </h1>
    <div>
        <p>
            Given a binary tree <code style = "font-family: Times New Roman">root</code> and a linked list with <code style = "font-family: Times New Roman">head</code> as the first node. 
        </p>
        <p>
            Return <b>True</b> if all the elements in the linked list starting from the <code style = "font-family: Times New Roman">head</code> correspond to some <i>downward path</i> connected in the binary tree otherwise return <b>False</b>.
        </p>
        <p>
            In this context downward path means a path that starts at some node and goes downwards.
        </p>
    </div>
    <hr>
    <div>
        <div>
            <b> Example 1: </b> <br>
            <img src = "https://assets.leetcode.com/uploads/2020/02/12/sample_1_1720.png", style = "border: 1px solid black; border-radius: 5px">
            <div style = "margin: 20px">
                <b>Input:</b> head = [4,2,8], root = [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3] <br>
                <b>Output:</b> true <br>
                <b>Explanation:</b> Nodes in blue form a subpath in the binary Tree.
            </div>
        </div>
        <div>
            <b> Example 2: </b> <br>
            <img src = "https://assets.leetcode.com/uploads/2020/02/12/sample_2_1720.png", style = "border: 1px solid black; border-radius: 5px">
            <div style = "margin: 20px">
                <b>Input:</b> head = [1,4,2,6], root = [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3] <br>
                <b>Output:</b> true <br>
            </div>
        </div>
        <div>
            <b> Example 3: </b> <br>
            <div style = "margin: 20px">
                <b>Input:</b> head = [1,4,2,6,8], root = [1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3] <br>
                <b>Output:</b> false <br>
                <b>Explanation:</b> There is no path in the binary tree that contains all the elements of the linked list from <code style = "font-family: Times New Roman">head</code>.
            </div>
        </div>
    </div>
    <hr>
    <div>
        <b> Constraints: </b><br>
        <ul>
            <li>
                The number of nodes in the tree will be in the range <code style = "font-family: Times New Roman">[1, 2500]</code>.
            </li>
            <li>
                The number of nodes in the list will be in the range <code style = "font-family: Times New Roman">[1, 100]</code>.
            </li>
            <li>
                <code style = "font-family: Times New Roman">1 <= Node.val <= 100</code> for each node in the linked list and binary tree.
            </li>
        </ul>
    </div> 
    <hr>
    <div>
        <b> Type: </b> Medium
        <div>
            <b> Topics: </b> Linked List, Tree, Depth-First Search, Breadth-First Search, Binary Tree
        </div>
        <div>
            <b> Companies:</b> SoundHound, Amazon, Adobe, Google
        </div>
    </div>
    <hr>
</div>