# 1634. Add Two Polynomials Represented as Linked Lists

A polynomial linked list is a special type of linked list where every node represents a term in a polynomial expression.

Each node has three attributes:
- ***coefficient***: an integer representing the number multiplier of the term. The coefficient of the term <span style = "color: blue"> *9x<sup>4</sup>* </span> is <span style = "color: blue"> *9* </span>.
- ***power***: an integer representing the exponent. The power of the term <span style = "color: blue"> *9x<sup>4</sup>* </span> is <span style = "color: blue"> *4* </span>.
- ***next***: a pointer to the next node in the list, or <span style = "color: blue"> *null* </span> if it is the last node of the list.

For example, the polynomial <span style = "color: blue"> *5x<sup>3</sup> + 4x - 7* </span> is represented by the polynomial linked list illustrated below:

<img src = "https://assets.leetcode.com/uploads/2020/09/30/polynomial2.png" style = "border: 2px solid grey">

The polynomial linked list must be in its standard form: the polynomial must be in strictly descending order by its **power** value. Also, terms with a **coefficient** of <span style = "color: blue"> **0** </span> are omitted.

Given two polynomial linked list heads, **poly1** and **poly2**, add the polynomials together and return *the head of the sum of the polynomials.*

**PolyNode** format:

The input/output format is as a list of *n* nodes, where each node is represented as its *[coefficient, power]*. For example, the polynomial <span style = "color: blue"> ***5x<sup>3</sup> + 4x - 7*** </span> would be represented as: <span style = "color: blue"> **[[5,3],[4,1],[-7,0]]** </span>.

**Example 1:**
<img src = "https://assets.leetcode.com/uploads/2020/10/14/ex1.png" style = "border: 2px solid grey">

**Input:** poly1 = [[1,1]], poly2 = [[1,0]] <br>
**Output:** [[1,1],[1,0]] <br>
**Explanation:** poly1 = x. poly2 = 1. The sum is x + 1.

**Example 2:** <br>
**Input:** poly1 = [[2,2],[4,1],[3,0]], poly2 = [[3,2],[-4,1],[-1,0]] <br>
**Output:** [[5,2],[2,0]] <br>
**Explanation:** poly1 = <span style = "color: blue"> 2x<sup>2</sup> + 4x + 3 </span>. poly2 = <span style = "color: blue"> 3x<sup>2</sup> - 4x - 1 </span>. The sum is <span style = "color: blue"> 5x<sup>2</sup> + 2 </span> . Notice that we omit the <span style = "color: blue"> "0x" </span> term.

**Example 3:** <br>
**Input:** poly1 = [[1,2]], poly2 = [[-1,2]] <br>
**Output:** [] <br>
**Explanation:** The sum is 0. We return an empty list.

**Constraints:** <br>
- *0 <= n <= 10<sup>4</sup>*
- *10<sup>-9</sup> <= PolyNode.coefficient <= 10<sup>9</sup>*
- *PolyNode.coefficient != 0*
- *0 <= PolyNode.power <= 10<sup>9</sup>*
- *PolyNode.power > PolyNode.next.power*