# Exercise 2

## Question 1
- One point is that insetad of binary search, where the search always begins from the middle, interpolation search estimates where the position of the key is going to be by comparing it to the minimum and maximum values. That is if it the elements are sorted, if they are not sorted, it would still converge quicker due to its predictions.
- That is if it the elements are sorted, if they are not sorted, it can still converge quicker due to its predictions. Binary search only has one method regardless if it is uniform or not; interpolation search adapts to the fact that it is sorted or not sorted and predicts where it should start the search from. But usually it assumes that the elements are already uniformly sorted, which can sometimes be misleading.

## Question 2
- When the distribution is not uniform, it assumes a random position using the same formula, and it may or may not be closer to the element you are looking for. The performance will be affected because if it is closer, it is closer to the Big($$\omega$$) because it has less elements to look through, however; if it is farther, it is closer to the Big(O) because there are more elements to look through.

## Question 3
- You would need to modify the interpolation formula:
- - "pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))"