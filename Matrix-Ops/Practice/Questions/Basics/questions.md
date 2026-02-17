# NumPy Practice Questions
## From Easy to Hard Level

---

## Table of Contents
1. [Easy Level Questions](#easy-level-questions)
2. [Medium Level Questions](#medium-level-questions)
3. [Hard Level Questions](#hard-level-questions)

---

## Easy Level Questions {#easy-level-questions}

**Q1:** Create a 4x4 array with random integers between 1 and 100. Find its shape, size, and dimensions.

**Q2:** Generate an array of 15 evenly spaced numbers between 0 and 5. Reshape it into a 3x5 matrix.

**Q3:** Create two 1D arrays of length 6 with random integers. Perform element-wise addition, subtraction, multiplication, and division.

**Q4:** Create a 5x5 identity matrix and change all elements in the last row to 7.

**Q5:** Generate an array of 20 random numbers. Calculate and print mean, median, standard deviation, and variance.

**Q6:** Create a 3x4 array with values from 1 to 12. Extract the first two rows and last two columns.

**Q7:** Create a 1D array of 10 random integers. Replace all negative numbers with 0.

**Q8:** Generate two 2x3 matrices. Concatenate them vertically and horizontally.

**Q9:** Create an array of 100 random numbers. Find the indices of numbers greater than 0.8.

**Q10:** Create a 4x4 array. Calculate the sum of each row and each column.

---

## Medium Level Questions {#medium-level-questions}

**Q11:** Create two 3x3 matrices with random integers. Perform matrix multiplication and calculate the determinant of the result.

**Q12:** Generate a 10x10 array of random numbers. Convert it to a binary array where values > 0.5 become 1 and <= 0.5 become 0.

**Q13:** Create a 1D array of 50 random integers. Find and replace all prime numbers with -1.

**Q14:** Generate a 5x5 array. Extract the diagonal elements and create a new array with these diagonal elements squared.

**Q15:** Create two arrays: A (3x3) and B (3x1). Use broadcasting to add B to each column of A.

**Q16:** Generate a 8x8 array of random integers. Find the positions (indices) of the 5 largest values.

**Q17:** Create a 1D array of 30 random numbers. Calculate the moving average with window size 5.

**Q18:** Generate a 4x4 matrix. Calculate its inverse and verify that A * A^(-1) gives identity matrix.

**Q19:** Create a 6x6 array. Extract all elements that are divisible by 3.

**Q20:** Generate two 1D arrays of different lengths. Use broadcasting to create a 2D array of their outer product.

---

## Hard Level Questions (on Basic Topics) {#hard-level-questions}

These questions test deep understanding of basic NumPy concepts through complex scenarios.

---

### Q21: The Missing Data Detective

You're given a dataset with missing values represented as -999. Create a function that:
- Takes a 2D array and replaces -999 with the column mean (ignoring -999)
- Returns both cleaned array and a mask showing where replacements were made
- Handle cases where entire column is -999 (use 0 in that case)

```python
# Example input:
data = np.array([[1, -999, 3],
                 [-999, 5, 6],
                 [7, 8, -999]])
# Your code here