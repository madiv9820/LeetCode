<div style = "font-size: 18px; font-family: times">
    <div>
        <h1 style = "font-size: 40px"> 
            2807. Insert Greatest Common Divisors in Linked List
        </h1>
    </div>
    <div style = "font-size: 20px">
        <div>
            <b>Type</b>: <span style = "color: blue">Medium</span>
        </div>
        <div>
            <b>Topics:</b> Linked List, Math, Number Theory
        </div>
        <div>
            <b>Companies:</b> Amazon
        </div>
    </div><hr>
    <div>
        <p>
            Given the head of a linked list <code style = "font-family: times">head</code>, in which each node contains an integer value.
        </p>
        <p>
            Between every pair of adjacent nodes, insert a new node with a value equal to the <b>greatest common divisor</b> of them.
        </p>
        <p>
            Return <i>the linked list after insertion.</i>
        </p>
        <p>
            The <b>greatest common divisor</b> of two numbers is the largest positive integer that evenly divides both numbers.
        </p>
    </div><hr>
    <div>
        <b style = "font-size: 20px"> Examples: </b>
        <div style = "margin: 20px">
            <div>
                <b> Example 1: </b><br>
                <img src = "https://assets.leetcode.com/uploads/2023/07/18/ex1_copy.png" style = "border: 1px solid grey; border-radius: 5px">
                <div style = "margin: 20px">
                    <b>Input:</b> head = [18,6,10,3] <br>
                    <b>Output:</b> [18,6,6,2,10,1,3] <br>
                    <b>Explanation:</b> The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).<br>
                    - We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes. <br>
                    - We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes. <br>
                    - We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes. <br>
                    There are no more adjacent nodes, so we return the linked list.
                </div>
            </div>
            <div>
                <b> Example 2: </b><br>
                <img src = "https://assets.leetcode.com/uploads/2023/07/18/ex2_copy1.png" style = "border: 1px solid grey; border-radius: 5px">
                <div style = "margin: 20px">
                    <b>Input:</b> head = [7] <br>
                    <b>Output:</b> [7] <br>
                    <b>Explanation:</b> The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes. <br>
                    There are no pairs of adjacent nodes, so we return the initial linked list.
                </div>
            </div>
        </div>
    </div><hr>
    <div>
        <b style = "font-size: 20px">Constraints:</b>
        <ul>
            <li>
                The number of nodes in the list is in the range <code style = "font-family: times">[1, 5000]</code>.
            </li>
            <li>
                <code style = "font-family: times">
                    1 <= Node.val <= 1000
                </code>
            </li>
        </ul>
    <div><hr>
</div>