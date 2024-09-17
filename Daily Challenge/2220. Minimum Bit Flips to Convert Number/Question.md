<div style = "font-size: 18px; font-family: times">
    <div>
        <h1 style = "font-size: 40px"> 
            2220. Minimum Bit Flips to Convert Number 
        </h1>
    </div>
    <div style = "font-size: 20px; margin: 20px">   
        <div>
            <b> Type: </b>
            <span style = "color: green"> Easy 
        </div>
        <div> <b> Topics: </b> Bit Manipulation </div>
        <div>
            <b> Companies: </b> Microsoft, persistent systems, Amazon, Google
        </div>
    </div><hr>
    <div>
        <p>
            A <b>bit flip</b> of a number <code style = "font-family:times">x</code> is choosing a bit in the binary representation of <code style = "font-family:times">x</code> and flipping it from either <code style = "font-family:times">0</code> to <code style = "font-family:times">1</code> or <code style = "font-family:times">1</code> to <code style = "font-family:times">0</code>.
        </p>
        <ul>
            <li>
                <p>
                    For example, for <code style = "font-family:times">x = 7</code>, the binary representation is <code style = "font-family:times">111</code> and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get <code style = "font-family:times">110</code>, flip the second bit from the right to get <code style = "font-family:times">101</code>, flip the fifth bit from the right (a leading zero) to get <code style = "font-family:times">10111</code>, etc.
                </p>
            </li>
        </ul>
        <p>
            Given two integers <code style = "font-family:times">start</code> and <code style = "font-family:times">goal</code>, return <i>the <b>minimum</b> number of <b>bit flips</b> to convert <code style = "font-family:times; font-style: normal">start</code> to <code style = "font-family:times; font-style: normal">goal</code></i>.
        </p>
    </div><hr>
    <div>
        <b style = "font-size: 20px"> Examples: </b>
        <div style = "margin: 20px">
            <div>
                <b> Example 1: </b>
                <div style = "margin: 20px">
                    <b>Input:</b> start = 10, goal = 7 <br>
                    <b>Output:</b> 3 <br>
                    <b>Explanation:</b> The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:<br>
                    <ul>
                        <li>Flip the first bit from the right: 1010 -> 1011.</li>
                        <li>Flip the third bit from the right: 1011 -> 1111.</li>
                        <li>Flip the fourth bit from the right: 1111 -> 0111.</li>
                    </ul>
                    It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.
                </div>
            </div>
            <div>
                <b> Example 2: </b>
                <div style = "margin: 20px">
                    <b>Input:</b> start = 3, goal = 4 <br>
                    <b>Output:</b> 3 <br>
                    <b>Explanation:</b> The binary representation of 3 and 4 are 011 and 100 respectively. We can convert 3 to 4 in 3 steps:<br>
                    <ul>
                        <li>Flip the first bit from the right: 011 -> 010.</li>
                        <li>Flip the second bit from the right: 010 -> 000.</li>
                        <li>Flip the third bit from the right: 000 -> 100.</li>
                    </ul>
                    It can be shown we cannot convert 3 to 4 in less than 3 steps. Hence, we return 3.
                </div>
            </div>
        </div>
    </div><hr>
    <div>
        <b style = "font-size: 20px"> Constraints: </b>
        <ul>
            <li>
                <code style = "font-family: times"> 
                    0 <= start, goal <= 10<sup>9</sup> 
                </code>
            </li>
        </ul>
    </div><hr>
    <div>
        <b style = "font-size: 20px">Hints:</b>
        <ul>
            <li> 
                If the value of a bit in start and goal differ, then we need to flip that bit. 
            </li>
            <li>
                Consider using the XOR operation to determine which bits need a bit flip.
            </li>
        </ul>
    </div><hr>
</div>