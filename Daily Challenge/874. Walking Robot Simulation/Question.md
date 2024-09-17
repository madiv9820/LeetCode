<div style = "font-family: verdana; font-size: 1.2em">
    <h1> 874. Walking Robot Simulation </h1>
    <div>
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
            width: 290px;
            padding: 10px;
            border-radius: 10px;
            text-align: center; /* Center text horizontally */
            display: inline-flex; /* Use inline-flex for inline elements */
            align-items: center; /* Center text vertically */
            justify-content: center; /* Center text horizontally */
            height: 200px; /* Ensure a height for vertical centering */
            box-sizing: border-box; /* Include padding and border in width and height*/height: 30px ">
            Topics:- Array, Hash Table, Simulation
        </span>
        <span style = "
            color: black;
            border: 1px solid black;
            margin: 0 auto;
            width: 255px;
            padding: 10px;
            border-radius: 10px;
            text-align: center; /* Center text horizontally */
            display: inline-flex; /* Use inline-flex for inline elements */
            align-items: center; /* Center text vertically */
            justify-content: center; /* Center text horizontally */
            height: 200px; /* Ensure a height for vertical centering */
            box-sizing: border-box; /* Include padding and border in width and height*/height: 30px ">
            Companies:- Jane Street, Amazon
        </span>    
    </div><br>
    <div>
        <p>
            A robot on an infinite XY-plane starts at point
            <span style = "
                color: black;
                border: 1px solid black;
                margin: 0 auto;
                width: 45px;
                padding: 10px;
                border-radius: 10px;
                text-align: center; /* Center text horizontally */
                display: inline-flex; /* Use inline-flex for inline elements */
                align-items: center; /* Center text vertically */
                justify-content: center; /* Center text horizontally */
                height: 200px; /* Ensure a height for vertical centering */
                box-sizing: border-box; /* Include padding and border in width and height*/height: 30px ">
                (0,0)
            </span>
            facing north. The robot can receive a sequence of these three possible types of
            <span style = "
                color: black;
                border: 1px solid black;
                margin: 0 auto;
                width: 85px;
                padding: 10px;
                border-radius: 10px;
                text-align: center; /* Center text horizontally */
                display: inline-flex; /* Use inline-flex for inline elements */
                align-items: center; /* Center text vertically */
                justify-content: center; /* Center text horizontally */
                height: 200px; /* Ensure a height for vertical centering */
                box-sizing: border-box; /* Include padding and border in width and height*/height: 30px ">
                commands
            </span>:
            <ul>
                <li>
                    <span style = "
                        color: black;
                        border: 1px solid black;
                        margin: 0 auto;
                        width: 2px;
                        padding: 10px;
                        border-radius: 10px;
                        text-align: center; /* Center text horizontally */
                        display: inline-flex; /* Use inline-flex for inline elements */
                        align-items: center; /* Center text vertically */
                        justify-content: center; /* Center text horizontally */
                        height: 200px; /* Ensure a height for vertical centering */
                        box-sizing: border-box; /* Include padding and border in width and height*/height: 30px ">
                        -2
                    </span>: 
                    Turn left 
                    <span style = "
                        color: black;
                        border: 1px solid black;
                        margin: 0 auto;
                        width: 2px;
                        padding: 10px;
                        border-radius: 10px;
                        text-align: center; /* Center text horizontally */
                        display: inline-flex; /* Use inline-flex for inline elements */
                        align-items: center; /* Center text vertically */
                        justify-content: center; /* Center text horizontally */
                        height: 200px; /* Ensure a height for vertical centering */
                        box-sizing: border-box; /* Include padding and border in width and height*/height: 30px ">
                        90 
                    </span>
                    degrees.
                </li><br>
                <li>
                    <span style = "
                        color: black;
                        border: 1px solid black;
                        margin: 0 auto;
                        width: 2px;
                        padding: 10px;
                        border-radius: 10px;
                        text-align: center; /* Center text horizontally */
                        display: inline-flex; /* Use inline-flex for inline elements */
                        align-items: center; /* Center text vertically */
                        justify-content: center; /* Center text horizontally */
                        height: 200px; /* Ensure a height for vertical centering */
                        box-sizing: border-box; /* Include padding and border in width and height*/height: 30px ">
                        -1
                    </span>: 
                    Turn right
                    <span style = "
                        color: black;
                        border: 1px solid black;
                        margin: 0 auto;
                        width: 2px;
                        padding: 10px;
                        border-radius: 10px;
                        text-align: center; /* Center text horizontally */
                        display: inline-flex; /* Use inline-flex for inline elements */
                        align-items: center; /* Center text vertically */
                        justify-content: center; /* Center text horizontally */
                        height: 200px; /* Ensure a height for vertical centering */
                        box-sizing: border-box; /* Include padding and border in width and height*/height: 30px ">
                        90
                    </span>
                    degrees.
                </li><br>
                <li>
                    <span style = "
                        color: black;
                        border: 1px solid black;
                        margin: 0 auto;
                        width: 110px;
                        padding: 10px;
                        border-radius: 10px;
                        text-align: center; /* Center text horizontally */
                        display: inline-flex; /* Use inline-flex for inline elements */
                        align-items: center; /* Center text vertically */
                        justify-content: center; /* Center text horizontally */
                        height: 200px; /* Ensure a height for vertical centering */
                        box-sizing: border-box; /* Include padding and border in width and height*/height: 30px ">
                        1 <= k <= 9
                    </span>: 
                    Move forward k units, one unit at a time.
                </li>
            </ul>
        </p>
        <p>
            Some of the grid squares are 
            <span style = "
                        color: black;
                        border: 1px solid black;
                        margin: 0 auto;
                        width: 75px;
                        padding: 10px;
                        border-radius: 10px;
                        text-align: center; /* Center text horizontally */
                        display: inline-flex; /* Use inline-flex for inline elements */
                        align-items: center; /* Center text vertically */
                        justify-content: center; /* Center text horizontally */
                        height: 200px; /* Ensure a height for vertical centering */
                        box-sizing: border-box; /* Include padding and border in width and height*/height: 30px ">
                obstacles
            </span>. 
            The 
            <span style = "
                color: black;
                border: 1px solid black;
                margin: 0 auto;
                width: 11px;
                padding: 10px;
                border-radius: 10px;
                text-align: center; /* Center text horizontally */
                display: inline-flex; /* Use inline-flex for inline elements */
                align-items: center; /* Center text vertically */
                justify-content: center; /* Center text horizontally */
                height: 200px; /* Ensure a height for vertical centering */
                box-sizing: border-box; /* Include padding and border in width and height*/height: 30px ">
                i<sup>th</sup> 
            </span>
            obstacle is at grid point 
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
                box-sizing: border-box; /* Include padding and border in width and height*/height: 30px ">
                obstacles[i] = (x<sub>i</sub>, y<sub>i</sub>)
            </span>. If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.
        </p>
        <p>
            Return <i>the <b>maximum Euclidean distance</b> that the robot ever gets from the origin <b>squared</b> (i.e. if the distance is 
            <span style = "
                color: black;
                border: 1px solid black;
                margin: 0 auto;
                width: 20px;
                padding: 10px;
                border-radius: 10px;
                text-align: center; /* Center text horizontally */
                display: inline-flex; /* Use inline-flex for inline elements */
                align-items: center; /* Center text vertically */
                justify-content: center; /* Center text horizontally */
                height: 200px; /* Ensure a height for vertical centering */
                box-sizing: border-box; /* Include padding and border in width and height*/height: 30px ">
                5
            </span>, return 
            <span style = "
                color: black;
                border: 1px solid black;
                margin: 0 auto;
                width: 17px;
                padding: 10px;
                border-radius: 10px;
                text-align: center; /* Center text horizontally */
                display: inline-flex; /* Use inline-flex for inline elements */
                align-items: center; /* Center text vertically */
                justify-content: center; /* Center text horizontally */
                height: 200px; /* Ensure a height for vertical centering */
                box-sizing: border-box; /* Include padding and border in width and height*/height: 30px ">
                25
            </span> ).</i>
        </p>
        <p>
            <b>Note:</b>
            <ul>
                <li>North means +Y direction.</li>
                <li>East means +X direction.</li>
                <li>South means -Y direction.</li>
                <li>West means -X direction.</li>
                <li>There can be obstacle in [0,0].</li>
            </ul>
        </p>
    </div>
    <div>
        <b>Example 1:</b>
        <div style = "margin: 20px">
            <b>Input:</b> commands = [4,-1,3], obstacles = [] <br>
            <b>Output:</b> 25 <br>
            <b>Explaination:</b>
            The robot starts at (0, 0): <br>
            1. Move north 4 units to (0, 4). <br>
            2. Turn right. <br>
            3. Move east 3 units to (3, 4). <br>
            The furthest point the robot ever gets from the origin is (3, 4), which squared is 3<sup>2</sup> + 4<sup>2</sup> = 25 units away.
        </div>
    </div>
    <div>
        <b>Example 2:</b>
        <div style = "margin: 20px">
            <b>Input:</b> commands = [4,-1,4,-2,4], obstacles = [[2,4]] <br>
            <b>Output:</b> 65 <br>
            <b>Explaination:</b>
            The robot starts at (0, 0): <br>
            1. Move north 4 units to (0, 4). <br>
            2. Turn right. <br>
            3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4). <br>
            4. Turn left. <br>
            5. Move north 4 units to (1, 8). <br>
            The furthest point the robot ever gets from the origin is (1, 8), which squared is 1<sup>2</sup> + 8<sup>2</sup> = 65 units away.
        </div>
    </div>
    <div>
        <b>Example 3:</b>
        <div style = "margin: 20px">
            <b>Input:</b> commands = [6,-1,-1,6], obstacles = [] <br>
            <b>Output:</b> 36 <br>
            <b>Explaination:</b>
            The robot starts at (0, 0): <br>
            1. Move north 6 units to (0, 6). <br>
            2. Turn right. <br>
            3. Turn right. <br>
            4. Move south 6 units to (0, 0). <br>
            The furthest point the robot ever gets from the origin is (0, 6), which squared is 6<sup>2</sup> = 36 units away.
        </div>
    </div>
    <div>
        <b>Constraints:</b>
        <ul>
            <li> 1 <= commands.length <= 10<sup>4</sup> </li>
            <li> commands[i] is either -2, -1, or an integer in the range [1, 9]. </li>
            <li> 0 <= obstacles.length <= 10<sup>4</sup> </li>
            <li> 3 * 10<sup>4</sup> <= x<sub>i</sub>, y<sub>i</sub> <= 3 * 10<sup>4</sup> </li>
            <li> The answer is guaranteed to be less than 2<sup>31</sup>. </li>
        </ul>
    </div>
</div>