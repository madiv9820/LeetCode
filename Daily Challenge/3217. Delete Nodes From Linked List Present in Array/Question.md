<h1 style = "font-size: 40px">3217. Delete Nodes From Linked List Present in Array </h1>

<div style = "margin: 0px 10px; font-size: 15px">
        <span style = "
            color: black;
            border: 1px solid black;
            margin: 0 auto;
            width: 80px;
            padding: 10px;
            border-radius: 10px;
            text-align: center; /* Center text horizontally */
            display: inline-flex; /* Use inline-flex for inline elements */
            align-items: center; /* Center text vertically */
            justify-content: center; /* Center text horizontally */
            height: 200px; /* Ensure a height for vertical centering */
            box-sizing: border-box; /* Include padding and border in width and height*/height: 30px ">
            Medium
        </span>
        <span style = "
            color: black;
            border: 1px solid black;
            margin: 0 auto;
            width: 280px;
            padding: 10px;
            border-radius: 10px;
            text-align: center; /* Center text horizontally */
            display: inline-flex; /* Use inline-flex for inline elements */
            align-items: center; /* Center text vertically */
            justify-content: center; /* Center text horizontally */
            height: 200px; /* Ensure a height for vertical centering */
            box-sizing: border-box; /* Include padding and border in width and height*/height: 30px ">
            Topics:- Array, Hash Table, Linked List
        </span>
        <span style = "
            color: black;
            border: 1px solid black;
            margin: 0 auto;
            width: 170px;
            padding: 10px;
            border-radius: 10px;
            text-align: center; /* Center text horizontally */
            display: inline-flex; /* Use inline-flex for inline elements */
            align-items: center; /* Center text vertically */
            justify-content: center; /* Center text horizontally */
            height: 200px; /* Ensure a height for vertical centering */
            box-sizing: border-box; /* Include padding and border in width and height*/height: 30px">
            Companies:- Google
        </span>    
    </div><br>

<div>
<p style = "font-size:15px">
    You are given an array of integers <code>nums</code> and the <code>head</code> of a linked list. Return the <code>head</code> of the modified linked list after removing all nodes from the linked list that have a value that exists in <code>nums</code> .
</p>
</div>

<div style = "font-size:15px">
    <b>Example 1:</b><br>
    <div style = "margin: 20px">
    <b>Input:</b> nums = [1,2,3], head = [1,2,3,4,5]<br>
    <b>Output:</b> [4,5] <br>
    <b>Explanation:</b><br>
    <img src = "https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample0.png", style = "border: 1px solid black; border-radius: 10px"><br>
    Remove the nodes with values 1, 2, and 3.
    </div>
</div>

<div style = "font-size:15px">
    <b>Example 2:</b><br>
    <div style = "margin: 20px">
    <b>Input:</b> nums = [1], head = [1,2,1,2,1,2]<br>
    <b>Output:</b> [2,2,2] <br>
    <b>Explanation:</b><br>
    <img src = "https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample1.png", style = "border: 1px solid black; border-radius: 10px"><br>
    Remove the nodes with value 1.
    </div>
</div>

<div style = "font-size:15px">
    <b>Example 3:</b><br>
    <div style = "margin: 20px">
    <b>Input:</b> nums = [5], head = [1,2,3,4]<br>
    <b>Output:</b> [1,2,3,4] <br>
    <b>Explanation:</b><br>
    <img src = "https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample2.png", style = "border: 1px solid black; border-radius: 10px"><br>
    No node has value 5.
    </div>
</div>

<div style = "font-size:15px">
    <b>Constraints:</b>
    <ul>
        <li>
            <code>
                1 <= nums.length <= 10<sup>5</sup>
            </code>
        </li>
        <li>
            <code>
                1 <= nums[i] <= 10<sup>5</sup>
            </code>
        </li>
        <li>
            All elements in <code>nums</code> are unique.
        </li>
        <li>
            The number of nodes in the given list is in the range <code>[1, 10<sup>5</sup>]</code> .
        </li>
        <li>
            <code>
                1 <= Node.val <= 10<sup>5</sup>
            </code>
        </li>
        <li>
            The input is generated such that there is at least one node in the linked list that has a value not present in <code>nums</code> .
        </li>
    </ul>
</div>