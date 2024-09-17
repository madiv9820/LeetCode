<div style = "font-size:2em"> 
    <h1> 2028. Find Missing Observations </h2> 
</div>

<div style = "font-size:1.5em">
    <span style = "
        color: black;
        border: 1px solid black;
        margin: 0 auto;
        width: 100px;
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
        width: 330px;
        padding: 10px;
        border-radius: 10px;
        text-align: center; /* Center text horizontally */
        display: inline-flex; /* Use inline-flex for inline elements */
        align-items: center; /* Center text vertically */
        justify-content: center; /* Center text horizontally */
        height: 200px; /* Ensure a height for vertical centering */
        box-sizing: border-box; /* Include padding and border in width and height*/height: 30px ">
        Topics:- Array, Math, Simulation
    </span>
    <span style = "
        color: black;
        border: 1px solid black;
        margin: 0 auto;
        width: 420px;
        padding: 10px;
        border-radius: 10px;
        text-align: center; /* Center text horizontally */
        display: inline-flex; /* Use inline-flex for inline elements */
        align-items: center; /* Center text vertically */
        justify-content: center; /* Center text horizontally */
        height: 200px; /* Ensure a height for vertical centering */
        box-sizing: border-box; /* Include padding and border in width and height*/height: 30px ">
        Companies:- Microsoft, Amazon, Stubhub
    </span>    
</div><br>

<div style = "font-size:1.5em">
    <p>
        You have observations of <b><i>n + m</i></b>, <b><i>6-sided</i></b> dice rolls with each face numbered from <b><i>1</i></b> to <b><i>6</i></b>. <b><i>n</i></b> of the observations went missing, and you only have the observations of <b><i>m</i></b> rolls. Fortunately, you have also calculated the <b>average value</b> of the <b><i>n + m</i></b> rolls.
    </p>
    <p>
        You are given an integer array <b><i>rolls</i></b> of length <b><i>m</i></b> where <b><i>rolls[i]</i></b> is the value of the <b><i>i<sup> th</sup></i></b> observation. You are also given the two integers <b><i>mean</i></b> and <b><i>n</i></b>.
    </p>
    <p>
        Return <i>an array of length <b>n</b> containing the missing observations such that the <b>average value</b> of the <b>n + m</b> rolls is <b>exactly</b> <b>mean</b></i>. If there are multiple valid answers, return any of them. If no such array exists, return an empty array.
    </p>
    <p>
        The <b>average value</b> of a set of <b><i>k</i></b> numbers is the sum of the numbers divided by <b><i>k</i></b>.
    </p>
    <p>
        Note that <b><i>mean</i></b> is an integer, so the sum of the <b><i>n + m</i></b> rolls should be divisible by <b><i>n + m</i></b>.
    </p>
</div>

<div style = "font-size:1.5em">
    <div>
        <b> Example 1: </b>
        <div style = "margin:20px">
            <b> Input: </b> rolls = [3,2,4,3], mean = 4, n = 2 <br>
            <b> Output: </b> [6,6] <br>
            <b> Explanation: </b> The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
        </div>
    </div>
    <div>
        <b> Example 2: </b>
        <div style = "margin:20px">
            <b> Input: </b> rolls = [1,5,6], mean = 3, n = 4 <br>
            <b> Output: </b> [2,3,2,2] <br>
            <b> Explanation: </b> The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
        </div>
    </div>
    <div>
        <b> Example 3: </b>
        <div style = "margin:20px">
            <b> Input: </b> rolls = [1,2,3,4], mean = 6, n = 4 <br>
            <b> Output: </b> [] <br>
            <b> Explanation: </b> It is impossible for the mean to be 6 no matter what the 4 missing rolls are.
        </div>
</div>

<div>
    <h3> Constraints:</h3>
    <ul>
        <li> m == rolls.length </li>
        <li> 1 <= n, m <= 10<sup>5</sup> </li>
        <li> 1 <= rolls[i], mean <= 6 </li>
    </ul>
</div>