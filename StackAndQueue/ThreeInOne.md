### Problem
    Describe how you could use a single array to implement three stacks.

### Method 1

Divide the array into three piece equally.Eg,assume given an array with length 30, so each parts are range 0-9, 10-19, 20-29 respectively. Assigned each range to each stack. Each stack track the start index and end index, so they don't overlap each other. After that, use each array to represent a single stack.