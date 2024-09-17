<div style = "font-size: 18px; font-family: times">
    <h1 style = "font-size: 40px"> 
        725. Split Linked List in Parts 
    </h1>
    <div>
        <div> <b>Type:</b> Medium </div>
        <div>
            <b>Topics:</b> Linked List
        </div>
        <div>
            <b>Companies:</b> Amazon, Google, Bloomberg, Uber
        </div>
    </div><hr>
    <div>
        <p>
            Given the <code style = "font-family: times">head</code> of a singly linked list and an integer <code style = "font-family: times">k</code>, split the linked list into <code style = "font-family: times">k</code> consecutive linked list parts.
        </p>
        <p>
            The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
        </p>
        <p>
            The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
        </p>
        <p>
            Return <i>an array of the <code style = "font-family: times">k</code> parts.</i>
        </p>
    </div><hr>
    <div>
        <div>
            <b>Example 1 :</b><br>
            <img src = "https://assets.leetcode.com/uploads/2021/06/13/split1-lc.jpg" style = "border: 1px solid black; border-radius: 10px">
            <div style = "margin: 20px">
                <b>Input:</b> head = [1,2,3], k = 5 <br>
                <b>Output:</b> [[1],[2],[3],[],[]] <br>
                <b>Explanation:</b><br>
                The first element output[0] has output[0].val = 1, output[0].next = null.<br>
                The last element output[4] is null, but its string representation as a ListNode is [].
            </div>
        </div>
        <div>
            <b>Example 2 :</b><br>
            <img src = "https://assets.leetcode.com/uploads/2021/06/13/split2-lc.jpg" style = "border: 1px solid black; border-radius: 10px">
            <div style = "margin: 20px">
                <b>Input:</b> head = [1,2,3,4,5,6,7,8,9,10], k = 3 <br>
                <b>Output:</b> [[1,2,3,4],[5,6,7],[8,9,10]] <br>
                <b>Explanation:</b><br>
                The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
            </div>
        </div>
    </div><hr>
    <div>
        <b>Constraints:</b>
        <ul>
            <li>
                The number of nodes in the list is in the range <code style = "font-family: times">[0, 1000]</code>.
            </li>
            <li>
                <code style = "font-family: times"> 
                    0 <= Node.val <= 1000
                </code>
            </li>
            <li>
                <code style = "font-family: times"> 
                    1 <= k <= 50
                </code> 
            </li>
        </ul>
    </div><hr>
</div>