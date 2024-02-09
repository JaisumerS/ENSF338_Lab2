# Exercise 4

## Question 1
- Since I do not know what the room number pattern is on the right side of the building, I will start with linear search starting from 100 and checking if each room is 128, all the way up until room 128. However, if I know that the end of the array is 130, I would start on that side and work backwords using linear search, a.k.a linear regression.
## Question 2
- A step would be defined as going inside and checking what the room number is. I am assuming that the room number is not listed outside of the room. Therefore, it will take me 14 steps to find room 128. Since I start at 100 and it goes up 2 numbers every room, it will take me 14 tries to find the room I am looking for.
## Question 3
- This is neither a best-case or worst-case scenario, however, it is pretty close to the worst case scenario. We did not look inside every room, which does not make it a worst-case scenario.
## Question 4
- The worst-case scenario would be looking for room 138 but starting on the left, or room 100. The other worst case scenario would be looking for room 100 but starting from room 138 and going down. The best case scenario would be looking for room 100 and starting from room 100, as this would be an 0(1). 
## Question 5
- If I know the fllor layout, I would use interpolation search. This way I would not have to look into every room, and can start from the best value, which would be closest to the room number I am searching for. 
    - In our case, to find room 128, our interpolation search would have to have the best possible starting index value. We would calculate this by looking at the difference between our start(left) and end(right) index values, then dividing it by how many elements there are in the list to see the incrementing value (Our case, 2). Then we would look at the difference between our key value and our value at left index (128-100), and then dividing that by our incrementing value (28/2), and finally adding that index value to the start(left) index (14+0).
- This way, we start right at the best case scenario of room 128 and there most likely would not be a need for recursion since it gets the room number on the first try.