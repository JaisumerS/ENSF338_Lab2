# Exercise 2

## Question 1
- One point is that insetad of binary search, where the search always begins from the middle, interpolation search estimates where the position of the key is going to be by comparing it to the minimum and maximum values. That is if it the elements are sorted, if they are not sorted, it would still converge quicker due to its predictions.
- That is if it the elements are sorted, if they are not sorted, it can still converge quicker due to its predictions. Binary search only has one method regardless if it is uniform or not; interpolation search adapts to the fact that it is sorted or not sorted and predicts where it should start the search from. But usually it assumes that the elements are already uniformly sorted, which can sometimes be misleading.

## Question 2
- When the distribution is not uniform, it assumes a random position using the same formula, and it may or may not be closer to the element you are looking for. The performance will be affected because if it is closer, it is closer to the Big(Ω) because it has less elements to look through, however; if it is farther, it is closer to the Big(O) because there are more elements to look through.

## Question 3
- You would need to modify the interpolation formula:
    * "pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))"

## Question 4
- You would use linear search when the elements are not sorted. This is because binary or interpolation search would keep checking if it is bigger or smaller, and depending on that they move towards one section, however, since it is unsorted, it does not know if it is truely on that section. Linear would look through everything one at a time.

## Question 5
- Linear search would outperform both binary and interpolation search, when the number is at the start of the list or object. This is because linear search starts from one end and binary and interpolation search start from the middle, so if the key is at the starting end, linear will always outperform binary and interpolation search.

## Question 6
- There is no way to solve this issue since binary starts from the middle, but interpolation can rarely get it on the first try because since it is unsorted, it can assume to start searching from the first element. Other than that, there is no way binary and interpolation can match or be faster than linear search if the element is first in the order.