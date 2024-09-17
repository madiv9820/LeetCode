<div style = "font-family: times; font-size: 18px">
    <div>
        <h1 style = "font-size: 40px">
            2419. Longest Subarray With Maximum Bitwise AND
        </h1>
    </div>
    <div style = "margin: 20px">
        <div>
            <b>Type: </b>
            <span style = "color: Blue"> Medium </span>
        </div>
        <div>
            <b>Topics: </b>
            Array, Bit Manipulation, Brainteaser
        </div>
        <div>
            <b>Companies: </b>
            fourkites, Siemens
        </div>
    </div><hr>
    <div>
        <p>
            You are given an integer array nums of size <code style = "font-family: times">n</code>.
        </p>
        <p>
            Consider a <b>non-empty</b> subarray from <code style = "font-family: times">nums</code> that has the <b>maximum</b> possible <b>bitwise AND</b>.
            <ul>
                <li>
                    In other words, let <code style = "font-family: times">k</code> be the maximum value of the bitwise AND of <b>any</b> subarray of <code style = "font-family: times">nums</code>. Then, only subarrays with a bitwise AND equal to <code style = "font-family: times">k</code> should be considered.
                </li>
            </ul>
        </p>
        <p>
            Return <i>the length of the <b>longest</b> such subarray.</i>
        </p>
        <p>
            The bitwise AND of an array is the bitwise AND of all the numbers in it.
        </p>
        <p>
            A <b>subarray</b> is a contiguous sequence of elements within an array.
        </p>
    </div><hr>
    <div>
        <div>
            <b>Example 1:</b>
            <div style = "margin: 20px">
                <b>Input:</b> nums = [1,2,3,3,2,2] <br>
                <b>Output:</b> 2 <br>
                <b>Explanation:</b><br>
                The maximum possible bitwise AND of a subarray is 3.</br>
                The longest subarray with that value is [3,3], so we return 2.
            </div>
        </div>
        <div>
            <b>Example 2:</b>
            <div style = "margin: 20px">
                <b>Input:</b> nums = [1,2,3,4] <br>
                <b>Output:</b> 1 <br>
                <b>Explanation:</b><br>
                The maximum possible bitwise AND of a subarray is 4.<br>
                The longest subarray with that value is [4], so we return 1.
            </div>
        </div>
    </div><hr>
    <div>
        <b>Constraints:</b>
        <ul>
            <li>
                <code style = "font-family: times">
                    1 <= nums.length <= 10<sup>5</sup>
                </code>
            </li>
            <li>
                <code style = "font-family: times">
                    1 <= nums[i] <= 10<sup>6</sup>
                </code>
            </li>
        </ul>
    </div><hr>
    <div>
        <b>Hints:</b>
        <ul>
            <li>
                Notice that the bitwise AND of two different numbers will always be strictly less than the maximum of those two numbers.
            </li>
            <li>
                What does that tell us about the nature of the subarray that we should choose?
            </li>
        </ul>
    </div><hr>
</div>