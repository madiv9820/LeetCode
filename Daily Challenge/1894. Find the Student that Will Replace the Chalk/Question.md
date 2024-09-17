# 1894. Find the Student that Will Replace the Chalk

There are <span style = "color: blue">n</span> students in a class numbered from <span style = "color: blue">0</span> to <span style = "color: blue">n - 1</span>. The teacher will give each student a problem starting with the student number <span style = "color: blue">0</span>, then the student number <span style = "color: blue">1</span>, and so on until the teacher reaches the student number <span style = "color: blue">n - 1</span>. After that, the teacher will restart the process, starting with the student number <span style = "color: blue">0</span> again.

You are given a **0-indexed** integer array <span style = "color: blue">chalk</span> and an integer <span style = "color: blue">k</span>. There are initially <span style = "color: blue">k</span> pieces of chalk. When the student number <span style = "color: blue">i</span> is given a problem to solve, they will use <span style = "color: blue">chalk[i]</span> pieces of chalk to solve that problem. However, if the current number of chalk pieces is **strictly less** than <span style = "color: blue">chalk[i]</span>, then the student number <span style = "color: blue">i</span> will be asked to **replace** the chalk.

Return *the **index** of the student that will **replace** the chalk pieces.*

**Example 1:**

**Input:** chalk = [5,1,5], k = 22 <br>
**Output:** 0 <br>
**Explanation:** The students go in turns as follows:
- Student number 0 uses 5 chalk, so k = 17.
- Student number 1 uses 1 chalk, so k = 16.
- Student number 2 uses 5 chalk, so k = 11.
- Student number 0 uses 5 chalk, so k = 6.
- Student number 1 uses 1 chalk, so k = 5.
- Student number 2 uses 5 chalk, so k = 0.

Student number 0 does not have enough chalk, so they will have to replace it.

**Example 2:**

**Input:** chalk = [3,4,1,2], k = 25 <br>
**Output:** 1 <br>
**Explanation:** The students go in turns as follows:
- Student number 0 uses 3 chalk so k = 22.
- Student number 1 uses 4 chalk so k = 18.
- Student number 2 uses 1 chalk so k = 17.
- Student number 3 uses 2 chalk so k = 15.
- Student number 0 uses 3 chalk so k = 12.
- Student number 1 uses 4 chalk so k = 8.
- Student number 2 uses 1 chalk so k = 7.
- Student number 3 uses 2 chalk so k = 5.
- Student number 0 uses 3 chalk so k = 2.

Student number 1 does not have enough chalk, so they will have to replace it.
 
### Constraints:
- chalk.length == n
- 1 <= n <= 10<sup>5</sup>
- 1 <= chalk[i] <= 10<sup>5</sup>
- 1 <= k <= 10<sup>9</sup>