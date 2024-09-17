<div style = "font-family: times; font-size: 18px">
    <h1 style = "font-size: 40px"> 2326. Spiral Matrix IV </h1>
    <div style = "margin: 20px; font-size: 20px">
        <div>
            <b> Type:</b> 
            <span style = "color: blue"> Medium </span>
        </div>
        <div>
            <b> Topics:</b> Array, Linked List, Matrix, Simulation
        </div>
    </div><hr>
    <div>
        <p>
            You are given two integers <code style = "font-family: times">m</code> and <code style = "font-family: times">n</code>, which represent the dimensions of a matrix.
        </p>
        <p>
            You are also given the <code style = "font-family: times">head</code> of a linked list of integers.
        </p>
        <p>
            Generate an <code style = "font-family: times">m x n</code> matrix that contains the integers in the linked list presented in <b>spiral</b> order <b>(clockwise)</b>, starting from the <b>top-left</b> of the matrix. If there are remaining empty spaces, fill them with <code style = "font-family: times">-1</code>.
        </p>
        <p>
            Return <i>the generated matrix</i>.
        </p>
    </div><hr>
    <div>
        <b style = "font-size: 20px"> Examples: </b>
        <div style = "margin: 20px">
            <div>
                <b>Example 1:</b><br>
                <img src = "https://assets.leetcode.com/uploads/2022/05/09/ex1new.jpg">
                <div style = "margin: 20px">
                    <b>Input:</b> m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]<br>
                    <b>Output:</b> [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]] <br>
                    <b>Explanation:</b> The diagram above shows how the values are printed in the matrix.<br>
                    Note that the remaining spaces in the matrix are filled with -1.
                </div>
            </div>
            <div>
                <b>Example 2:</b><br>
                <img src = "https://assets.leetcode.com/uploads/2022/05/11/ex2.jpg">
                <div style = "margin: 20px">
                    <b>Input:</b> m = 1, n = 4, head = [0,1,2]<br>
                    <b>Output:</b> [[0,1,2,-1]] <br>
                    <b>Explanation:</b> The diagram above shows how the values are printed from left to right in the matrix.<br>
                    The last space in the matrix is set to -1.
                </div>
            </div>
        </div>
    </div><hr>
    <div>
        <b style = "font-size: 20px">Constraints:</b>
        <ul>
            <li>
                <code style = "font-family: times">
                    1 <= m, n <= 10<sup>5</sup>
                </code>
            </li>
            <li>
                <code style = "font-family: times">
                    1 <= m * n <= 10<sup>5</sup>
                </code>
            </li>
            <li>
                The number of nodes in the list is in the range
                <code style = "font-family: times">
                    [1, m * n]
                </code>.
            </li>
            <li>
                <code style = "font-family: times">
                    0 <= Node.val <= 1000
                </code>
            </li>
        </ul>
    </div><hr>
    <div>
        <b style = "font-size: 20px">Hints:</b>
        <ol>
            <li> First, generate an m x n matrix filled with -1s.</li>
            <li> Navigate within the matrix at (i, j) with the help of a direction vector ⟨di, dj⟩. At (i, j), you need to decide if you can keep going in the current direction.</li>
            <li> If you cannot keep going, rotate the direction vector clockwise by 90 degrees.</li>
        </ol>
    </div><hr>
</div>