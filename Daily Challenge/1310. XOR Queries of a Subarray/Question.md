<div style = "font-size: 18px; font-family: times">
    <div>
        <h1 style = "font-size: 40px"> 
            1310. XOR Queries of a Subarray 
        </h1>
    </div>
    <div style = "margin: -10px 0px 10px 20px; font-size: 18px">
        <div>
            <b> Type: </b> <span style = "color: blue"> Medium </span>
        </div>
        <div>
            <b> Topics:</b> Array, Bit Manipulation, Prefix Sum
        </div>
        <div>
            <b> Companies: </b> Airtel, Amazon
        </div>
    </div><hr>
    <div>
        <p>
            You are given an array <code style = "font-family:times">arr</code> of positive integers. You are also given the array <code style = "font-family: times">queries</code> where <code style = "font-family: times">queries[i] = [left<sub>i</sub>, right<sub>i</sub>]</code>.
        </p>
        <p>
            For each query <code style = "font-family: times">i</code> compute the <b>XOR</b> of elements from <code style = "font-family: times">left<sub>i</sub></code> to <code style = "font-family: times">right<sub>i</sub></code> (that is, <code style = "font-family: times">arr[left<sub>i</sub>] XOR arr[left<sub>i</sub> + 1] XOR ... XOR arr[right<sub>i</sub>]</code> ).
        </p>
        <p>
            Return an array <code style = "font-family: times">answer</code> where <code style = "font-family: times">answer[i]</code> is the answer to the <code style = "font-family: times">i<sup>th</sup></code> query.
        </p>
    </div><hr>
    <div>
        <b style = "font-size: 20px">Examples</b>
        <div style = "margin: 10px 0px 20px 20px; font-size: 18px">
            <div>
                <b>Example 1:</b>
                <div style = "margin: 0px 0px 20px 20px">
                    <b>Input:</b> arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]] <br>
                    <b>Output:</b> [2,7,14,8] <br>
                    <b>Explanation:</b> <br> 
                    The binary representation of the elements in the array are: <br>
                    <div style = "margin: 0px 0px 0px 20px">
                        1 = 0001 <br>
                        3 = 0011 <br>
                        4 = 0100 <br>
                        8 = 1000 <br>
                    </div>
                    The XOR values for queries are:<br>
                    <div style = "margin: 0px 0px 0px 20px">
                        [0,1] = 1 xor 3 = 2 <br>
                        [1,2] = 3 xor 4 = 7 <br>
                        [0,3] = 1 xor 3 xor 4 xor 8 = 14 <br> 
                        [3,3] = 8 
                    </div>
                </div>  
            </div>
            <div>
                <b> Example 2: </b>
                <div style = "margin: 10px 0px 20px 20px">
                    <b>Input:</b> arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]] <br>
                    <b>Output:</b> [8,0,4,4]
                </div>
            </div>
        </div>
    </div><hr>
    <div>   
        <b> Constraints: </b>
        <div style = "margin: 10px 0px 20px 20px">
            <ul>
                <li>
                    <code style = "font-family: times">
                        1 <= arr.length, queries.length <= 3 * 10<sup>4</sup>
                    </code>
                </li>
                <li>
                    <code style = "font-family: times">
                        1 <= arr[i] <= 10<sup>9</sup>
                    </code>
                </li>
                <li>
                    <code style = "font-family: times">
                        queries[i].length == 2
                    </code>
                </li>
                <li>
                    <code style = "font-family: times">
                        0 <= left<sub>i</sub> <= right<sub>i</sub> < arr.length
                    </code>
                </li>
            </ul>
        </div>
    </div><hr>
    <div>
        <b>Hints</b>
        <div style = "margin: 10px 0px 20px 20px">
            <ul>
                <li> What is the result of x ^ y ^ x ? </li>
                <li> Compute the prefix sum for XOR. </li>
                <li> Process the queries with the prefix sum values. </li>
            </ul>
        </div>
    </div><hr>
</div>