# Grind 75  

# Table of Contents

1. [Arrays](#array)
   1. [Two Sum](#two-sum)
   2. [Best Time to Buy and Sell Stock.py](#best-time-to-buy-and-sell-stock)
   3. [Majority Element](#majority-element)
   4. [Contains Duplicate](#contains-duplicate)
   5. [Meeting Rooms - Leetcode Premium](#meeting-rooms)
   6. [Move Zeroes](#move-zeroes)
2. [Stack](#stack)
   1. [Valid Parentheses](#valid-parentheses)
3. [Linked List](#linked-list)
   1. [Merge Two Sorted Lists](#merge-two-sorted-lists)
4. [String](#string)
   1. [Valid Palindrome](#valid-palindrome)

# Arrays <a name="array"></a>

1. [Two Sum](https://github.com/Oluwxtope/Grind-75/blob/main/1-arrays/1-two-sum.py) <a name="two-sum"></a>  
    > [Leetcode](https://leetcode.com/problems/two-sum/)  
    Initialize hashmap with element as key and index as value. Iterate through array checking if target number minus current element in hashmap. If yes, return indexes of both elements from hashmap
2. [Best Time to Buy and Sell Stock](https://github.com/Oluwxtope/Grind-75/blob/main/1-arrays/2-best-time-to-buy-and-sell-stock.py) <a name="best-time-to-buy-and-sell-stock"></a>  
    > [Leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)  
    Use sliding window to keep track of start index and end = start + 1 index. Keep track of max and current profit starting at 0. If end - start less than 0, update start to end and end to start + 1. Else, if end - start > max profit, update max profit and move end to next element.
3. [Majority Element](https://github.com/Oluwxtope/Grind-75/blob/main/1-arrays/3-majority-element.py) <a name="majority-element"></a>  
    > [Leetcode](https://leetcode.com/problems/majority-element/)  
    Use hashmap to keep count of how many times an element appears in array, then iterate over hashmap and return element with a count > ceiling(n/2)  
    More optimal solution would be using the Boyer-Moore algorithm. Initialize count to 0 and potential candidate to first element in array. Then increment or decrement count by iterating through the array and seeing if potential candidate is present or not. Once count reaches 0, change potential candidate to be present element. Return potential candidate left.
4. [Contains Duplicate](https://github.com/Oluwxtope/Grind-75/blob/main/1-arrays/4-contains-duplicate.py) <a name="contains-duplicate"></a>  
    > [Leetcode](https://leetcode.com/problems/contains-duplicate/)  
    Use hashmap to keep count of how many times an element appears while iterating through the array. If current element already in hashmap, return true. If loop concludes, return false as no duplicate elements.
5. Meeting Rooms<a name="meeting-rooms"></a>  
    > [Leetcode](https://leetcode.com/problems/meeting-rooms/)  
    *Premium leetcode required, didn't solve*
6. [Move Zeroes](https://github.com/Oluwxtope/Grind-75/blob/main/1-arrays/5-move-zeroes.py) <a name="move-zeroes"></a>  
    > [Leetcode](https://leetcode.com/problems/move-zeroes/)  
    Use 2 pointers starting from indices 0 and 1. 3 scenarios possible: both pointers = 0, move right one until find nonzero then swap; left pointer at 0 and right at nonzero, swap. left pointer at nonzero and right at zero, move both pointers 1 down array.

# Stack <a name="stack"></a>

1. [Valid Parentheses](https://github.com/Oluwxtope/Grind-75/blob/main/2-stack/1-valid-parentheses.py) <a name="valid-parentheses"></a>  
    > [Leetcode](https://leetcode.com/problems/valid-parentheses/)  
    Intialize hashmap matching all types of open brackets as keys to closing brackets as values. Then intialize stack adt using array, pushing opening brackets and only popping last one when you encounter a matching closing bracket. If array is empty, then all matching brackets are positioned in valid locations.

# Linked List <a name="linked-list"></a>

1. [Merge Two Sorted Lists](https://github.com/Oluwxtope/Grind-75/blob/main/3-linked-list/1-merge-two-sorted-lists.py) <a name="merge-two-sorted-lists"></a>  
    > [Leetcode](https://leetcode.com/problems/merge-two-sorted-lists/)  
    Initialize linkedlist called new and let a variable called prev point to it. Start while loop that checks if both lists 1 and 2 are not empty. 2 scenarios: val of curr node in list 1 less than that of 2 so let the next node of new be curr node of l1, and move to next node of l1; else, do the same for l2. Then set prev to next node of new and repeat. At end of loop, let prev.next equal to the non-empty list and return new.next as new.val is 0 and we started by changing new.next.

# String <a name="string"></a>

1. [Valid Palindrome](https://github.com/Oluwxtope/Grind-75/blob/main/4-string/1-valid-palindrome.py) <a name="valid-palindrome"></a>  
    > [Leetcode](https://leetcode.com/problems/valid-palindrome/)  
    Initalize start and end pointers on the array moving in opposite directions. If start and end pointing to alnum characters, check if they're equal (apply lowercase method) and return false if not else move pointers. If a pointer not pointing to alnum char, move the pointer. If loop finishes running, return true.
2. [Valid Anagram](https://github.com/Oluwxtope/Grind-75/blob/main/4-string/2-valid-anagram.py) <a name="valid-anagram"></a>  
    > [Leetcode](https://leetcode.com/problems/valid-anagram/)  
    Initialize hash map to keep track of count of letters in first string, repeat for second string. Then iterate through both hash maps checking if a char is present in one and not the other or if count of characters in one not equal to count in other and return false. if all loops finish running, return true.