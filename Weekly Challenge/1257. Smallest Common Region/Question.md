<div style = "font-family: times; font-size: 18px">
    <div>
        <h1 style = "font-size: 40px"> 
            1257. Smallest Common Region 
        </h1>
    </div>
    <div style = "margin: 20px">
        <div>
            <b>Type: </b>
            <span style = "color: blue"> Medium </span> 
        </div>
        <div>
            <b> Topics: </b>
            <span>
                Array, Hash Table, String, Tree, Depth-First Search, Breadth-First Search
            </span>
        </div>
        <div>
            <b> Companies: </b>
            <span> Airbnb, Tiktok </span>
        </div>
    </div><hr>
    <div>
        <p>
            You are given some lists of regions where the first <code style = "font-family: times">region</code> of each list includes all other regions in that list.
        </p>
        <p>
            Naturally, if a region <code style = "font-family: times">x</code> contains another region <code style = "font-family: times">y</code> then <code style = "font-family: times">x</code> is bigger than <code style = "font-family: times">y</code>. Also, by definition, a region <code style = "font-family: times">x</code> contains itself.
        </p>
        <p>
            Given two regions: <code style = "font-family: times">region1</code> and <code style = "font-family: times">region2</code>, return <i>the smallest region that contains both of them.</i>
        </p>
        <p>
            If you are given regions <code style = "font-family: times">r1</code>, <code style = "font-family: times">r2</code>, and <code style = "font-family: times">r3</code> such that <code style = "font-family: times">r1</code> includes <code style = "font-family: times">r3</code>, it is guaranteed there is no <code style = "font-family: times">r2</code> such that <code style = "font-family: times">r2</code> includes <code style = "font-family: times">r3</code>.
        </p>
        <p>
            It is guaranteed the smallest region exists.
        </p>
    </div><hr>
    <div>
        <div>
            <b> Example 1:</b>
            <div style = "margin: 20px">
                <b>Input:</b>
                <div style = "margin: 20px; border: 1px solid black; padding: 10px">
                    <code style = "font-size: 15px">
                        regions = [["Earth","North America","South America"],<br>
                        ["North America","United States","Canada"],<br>
                        ["United States","New York","Boston"],<br>
                        ["Canada","Ontario","Quebec"],<br>
                        ["South America","Brazil"]]<br><br>
                        region1 = "Quebec"<br>
                        region2 = "New York"
                    </code>
                </div>
                <b>Output:</b> "North America"<br>
            </div>
        </div>
        <div>
            <b> Example: 2 </b>
            <div style = "margin: 20px">
                <b>Input:</b>
                <div style = "margin: 20px; border: 1px solid black; padding: 10px">
                    <code style = "font-size: 15px">
                        regions = [["Earth", "North America", "South America"],<br>["North America", "United States", "Canada"],<br>["United States", "New York", "Boston"],<br>["Canada", "Ontario", "Quebec"],<br>["South America", "Brazil"]]<br><br>
                        region1 = "Canada"<br>
                        region2 = "South America"
                    </code>
                </div>
                <b>Output: </b> "Earth"
            </div>
        </div>
    </div><hr>
    <div>
        <b>Constraints:</b>
        <ul>
            <li>
                <code style = "font-size: 15px">
                    2 <= regions.length <= 10<sup>4</sup>
                </code>
            </li>
        <li>
            <code style = "font-size: 15px">
                2 <= regions[i].length <= 20
            </code>
        </li>
        <li>
            <code style = "font-size: 15px">
                1 <= regions[i][j].length, region1.length, region2.length <= 20
            </code>
        </li>
        <li>
            <code style = "font-size: 15px">
                region1 != region2
            </code>
        </li>
        <li>
            <code style = "font-size: 15px">regions[i][j]</code>, <code style = "font-size: 15px">region1</code>, and <code style = "font-size: 15px">region2</code> consist of English letters.
        </li>
        </ul>
    </div><hr>
    <div>
        <b>Constraints:</b>
        <ul>
            <li> 
                Try to model the problem as a graph problem. 
            </li>
            <li> The given graph is a tree. </li>
            <li> 
                The problem is reduced to finding the lowest common ancestor of two nodes in a tree. 
            </li>
        </ul>
    </div><hr>
</div>