# 1945. Sum of Digits of String After Convert

You are given a string <span style = "color:blue">s</span> consisting of lowercase English letters, and an integer <span style = "color:blue">k</span>.

First, **convert** <span style = "color:blue">s</span> into an integer by replacing each letter with its position in the alphabet (i.e., replace <<span style = "color:blue">>'a'</span> with <span style = "color:blue">1</span>, <span style = "color:blue">'b'</span> with <span style = "color:blue">2</span>, ..., <span style = "color:blue">'z'</span> with <span style = "color:blue">26</span>). Then, **transform** the integer by replacing it with the **sum of its digits**. Repeat the **transform** operation <span style = "color:blue">k</span> **times** in total.

For example, if <span style = "color:blue">s = "zbax"</span> and <span style = "color:blue">k = 2</span>, then the resulting integer would be <span style = "color:blue">8</span> by the following operations:

- **Convert:** <span style = "color:blue">"zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124</span>
- **Transform #1:** <span style = "color:blue">262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17</span>
- **Transform #2:** <span style = "color:blue">17 ➝ 1 + 7 ➝ 8</span>

Return *the resulting integer after performing the operations described above.*

**Example 1:**<br>
**Input:** s = "iiii", k = 1<br>
**Output:** 36<br>
**Explanation:** The operations are as follows:
- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36

Thus the resulting integer is 36.

**Example 2:**<br>
**Input:** s = "leetcode", k = 2<br>
**Output:** 6<br>
**Explanation:** The operations are as follows:
- Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
- Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
- Transform #2: 33 ➝ 3 + 3 ➝ 6

Thus the resulting integer is 6.

**Example 3:**<br>
**Input:** s = "zbax", k = 2<br>
**Output:** 8
 

### Constraints:

- *1 <= s.length <= 100*
- *1 <= k <= 10*
- <span style = "color:blue">s</span> consists of lowercase English letters.