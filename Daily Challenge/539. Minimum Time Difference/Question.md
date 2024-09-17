<div style = "font-family: times; font-size: 18px">
    <div>
        <h1 style = "font-size: 40px"> 539. Minimum Time Difference </h1>
    </div>
    <div style = "margin: 20px">
        <div>
            <b>Type: </b>
            <span style = "color: blue"> Medium </b>
        </div>
        <div>
            <b> Topics: </b>
            <span>
                Array, Math, String, Sorting
            </span>
        </div>
        <div>
            <b> Companies: </b>
            <span>
                Google, Zoho, Palantir Technologies,
                Amazon, Bloomberg, Microsoft, Adobe, carwale, Yahoo
            </span>
        </div>
    </div><hr>
    <div>
        Given a list of 24-hour clock time points in <b>"HH:MM"</b> format, return <i>the minimum <b>minutes</b> difference between any two time-points in the list.</i>
    </div><hr>
    <div>
        <div>
            <b> Example 1: </b>
            <div style = "margin: 20px">
                <b>Input:</b> 
                <span style = "font-family: sans-serif; font-size: 18px">
                    timePoints = ["23:59","00:00"]
                </span><br>
                <b>Output:</b> <span style = "font-family: sans-serif; font-size: 18px"> 1 </span>
            </div>
        </div>
        <div>
            <b> Example 2: </b>
            <div style = "margin: 20px">
                <b>Input:</b> 
                <span style = "font-family: sans-serif; font-size: 18px">
                    timePoints = ["00:00","23:59","00:00"]
                </span><br>
                <b>Output:</b> <span style = "font-family: sans-serif; font-size: 18px"> 0 </span>
            </div>
        </div>
    </div><hr>
    <div>
        <b>Constraints:</b>
        <ul>
            <li>
                <code style = "font-size: 15px">
                    2 <= timePoints.length <= 2 * 10<sup>4</sup>
                </code>
            </li>
            <li>
                <code style = "font-size: 15px">timePoints[i]</code> is in the format <b>"HH:MM"</b>.
            </li>
        </ul>
    </div><hr>
</div>