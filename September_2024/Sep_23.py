class Solution:
    def findTwoElement(self, arr): 
        # Step 1: Calculate expected sum and sum of squares for the first n natural numbers
        n = len(arr)
        S = n * (n + 1) // 2
        S_square = n * (n + 1) * (2 * n + 1) // 6
        
        # Step 2: Calculate the actual sum and sum of squares from the array
        S_actual = 0
        S_square_actual = 0
        for num in arr:
            S_actual += num
            S_square_actual += num * num
        
        # Step 3: Calculate the differences
        sum_diff = S - S_actual  # A - B
        square_diff = S_square - S_square_actual  # A^2 - B^2
        
        # Step 4: Using the formula A^2 - B^2 = (A - B)(A + B), find A + B
        sum_AB = square_diff // sum_diff  # (A + B)
        
        # Step 5: Solve for A and B
        A = (sum_diff + sum_AB) // 2
        B = sum_AB - A
        
        return B, A
