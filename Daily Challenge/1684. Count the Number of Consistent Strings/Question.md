<div style = "font-family: times; font-size: 18px">
    <div>
        <h1 style = "font-size: 40px">
            1684. Count the Number of Consistent Strings
        </h1>
    </div>
    <div style = "margin: 10px 0px 20px 20px; font-size: 18px">
        <div>
            <b>Type:</b> &nbsp <span style = "color: green; font-family: sans-serif"> Easy </span>
        </div>
        <div>
            <b>Topics:</b> &nbsp <span style = "font-family: sans-serif">Array, Hash Table, String, Bit Manipulation, Counting </span>
        </div>
        <div>
            <b>Companies:</b> &nbsp <span style = "font-family: sans-serif">Robinhood, Uber, Amazon, Yahoo</span>
        </div>
    </div><hr>
    <div style = "margin: 20px 0px 0px 0px">
        <p>
            You are given a string <code style = "font-family: times">allowed</code> consisting of distinct characters and an array of strings <code style = "font-family: times">words</code>. A string is consistent if all characters in the string appear in the string <code style = "font-family: times">allowed</code>.
        </p>
        <p>
            Return <i>the number of <b>consistent</b> strings in the array</i> <code style = "font-family: times">words</code>.
        </p>
    </div><hr>
    <div>
        <b style = "font-size: 20px">Examples</b>
        <div style = "margin: 10px 0px 0px 20px">
            <div>
                <b>Examples 1:</b>
                <div style = "margin: 10px 0px 20px 20px">
                    <b>Input:</b> allowed = "ab", words = ["ad","bd","aaab","baa","badab"] <br>
                    <b>Output:</b> 2 <br>
                    <b>Explanation:</b> Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
                </div>
            </div>
            <div>
                <b>Examples 2:</b>
                <div style = "margin: 10px 0px 20px 20px">
                    <b>Input:</b> allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"] <br>
                    <b>Output:</b> 7 <br>
                    <b>Explanation:</b> All strings are consistent.
                </div>
            </div>
            <div>
                <b>Examples 3:</b>
                <div style = "margin: 10px 0px 20px 20px">
                    <b>Input:</b> allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"] <br>
                    <b>Output:</b> 4 <br>
                    <b>Explanation:</b> Strings "cc", "acd", "ac", and "d" are consistent.
                </div>
            </div>
        </div>
    </div><hr>
    <div>
        <b style = "font-size: 20px"> Constraints: </b>
        <ul>
            <li>
                <code style = "font-family: times">
                    1 <= words.length <= 10<sup>4</sup>
                </code>
            </li>
            <li>
                <code style = "font-family: times">
                    1 <= allowed.length <= 26
                </code>
            </li>
            <li>
                <code style = "font-family: times">
                    1 <= words[i].length <= 10
                </code>
            </li>
            <li>
                The characters in <code style = "font-family: times">allowed</code> are <b>distinct</b>.
            </li>
            <li>
                <code style = "font-family: times">words[i]</code> and <code style = "font-family: times">allowed</code> contain only lowercase English letters.
            </li>
        </ul>
    </div><hr>
    <div>
        <b style = "font-size: 20px">Hints</b>
        <ul>
            <li> 
                A string is incorrect if it contains a character that is not allowed.
            </li>
            <li>
                Constraints are small enough for brute force
            </li>
        </ul>
    </div><hr>
</div>