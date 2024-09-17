<div style = "font-size: 18px; font-family: times">
    <h1 style = "font-size: 40px"> 1229. Meeting Scheduler </h1>
    <div>
        <div> <b>Type:</b> Medium </div>
        <div> 
            <b>Topics:</b> Arrays, Two Pointers, Sorting 
        </div>
        <div>
            <b>Companies:</b> Paypal, Amazon, Apple
        </div>
    </div><hr>
    <div>
        <p>
            Given the availability time slots arrays <code style = "font-family: times">slots1</code> and <code style = "font-family: times">slots2</code> of two people and a meeting duration <code style = "font-family: times">duration</code>, return the <b>earliest time slot</b> that works for both of them and is of duration <code style = "font-family: times">duration</code>.
        </p>
        <p>
            If there is no common time slot that satisfies the requirements, return an <b>empty array</b>.
        </p>
        <p>
            The format of a time slot is an array of two elements <code style = "font-family: times">[start, end]</code> representing an inclusive time range from <code style = "font-family: times">start</code> to <code style = "font-family: times">end</code>.
        </p>
        <p>
            It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots <code style = "font-family: times">[start1, end1]</code> and <code style = "font-family: times">[start2, end2]</code> of the same person, either <code style = "font-family: times">start1 > end2</code> or <code style = "font-family: times">start2 > end1</code>.
        </p>
    </div><hr>
    <div>
        <h3> Examples</h3>
        <div style = "margin: 20px">
            <div>
                <b>Example 1:</b>
                <div style = "margin: 20px">
                    <b>Input:</b> slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8 <br>
                    <b>Output:</b> [60,68]
                </div>
            </div>
            <div>
                <b>Example 2:</b>
                <div style = "margin: 20px">
                    <b>Input:</b> slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12 <br>
                    <b>Output:</b> []
                </div>
            </div>
        </div>
    </div><hr>
    <div>
        <h3>Constraints:</h3>
        <ul>
            <li>
                <code style = "font-family: times">
                    1 <= slots1.length, slots2.length <= 10<sup>4</sup>
                </code>
            </li>
            <li>
                <code style = "font-family: times">
                    slots1[i].length, slots2[i].length == 2
                </code>
            </li>
            <li>
                <code style = "font-family: times">
                    slots1[i][0] < slots1[i][1]
                </code>
            </li>
            <li>
                <code style = "font-family: times">
                    slots2[i][0] < slots2[i][1]
                </code>
            </li>
            <li>
                <code style = "font-family: times">
                    0 <= slots1[i][j], slots2[i][j] <= 10<sup>9</sup>
                </code>
            </li>
            <li>
                <code style = "font-family: times">
                    1 <= duration <= 10<sup>6</sup>
                </code>
            </li>
        </ul>
    </div><hr>
    <div>
        <h3>Hints:</h3>
        <div style = "margin: 20px">
            <div>
                <b>Hint 1:</b> Assume that in the solution, the selected slot from slotsA is bigger than the respectively selected slot from slotsB.
            </div>
            <div>
                <b>Hint 2:</b> Use two pointers in order to try all the possible intersections, and check the length.
            </div>
            <div>
                <b>Hint 3:</b> Do the same in step N° 1 but now assume that the selected slot from slotsB is bigger, return the minimum of the two options.
            </div>
        <div>
    </div><hr>
</div>