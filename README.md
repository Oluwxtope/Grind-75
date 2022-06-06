# Grind 75  

# Table of Contents

1. [Array](#array)
   1. [Two Sum](#two-sum)
   2. [Best Time to Buy and Sell Stock.py](#buy-sell-stock)

# Array <a name="array"></a>
1. [Two Sum](https://github.com/Oluwxtope/Grind-75/blob/main/Arrays/1%20Two%20Sum.py) <a name="two-sum"></a>  
    > [Leetcode](https://leetcode.com/problems/two-sum/)  
    Initialize hashmap with element as key and index as value. Iterate through array checking if target number minus current element in hashmap. If yes, return indexes of both elements from hashmap
2. [Best Time to Buy and Sell Stock](https://github.com/Oluwxtope/Grind-75/blob/main/Arrays/2%20Best%20Time%20to%20Buy%20and%20Sell%20Stock.py) <a name="buy-sell-stock"></a>  
    > [Leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)  
    Use sliding window to keep track of start index and end = start + 1 index. Keep track of max and current profit starting at 0. If end - start less than 0, update start to end and end to start + 1. Else, if end - start > max profit, update max profit and move end to next element.
3. [Majority Element](https://github.com/Oluwxtope/Grind-75/blob/main/Arrays/3%20Majority%20Element.py) <a name="majority-element"></a>  
    > [Leetcode](https://leetcode.com/problems/majority-element/)  
    Use hashmap to keep count of how many times an element appears in array, then iterate over hashmap and return element with a count > ceiling(n/2)
    
