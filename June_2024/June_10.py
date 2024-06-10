from typing import List

class Solution:
    def matchPairs(self, n: int, nuts: List[str], bolts: List[str]) -> None:
        # Define the order of elements
        order = ['!', '#', '$', '%', '&', '*', '?', '@', '^']

        # Create a dictionary to store the position of each character
        order_map = {ch: i for i, ch in enumerate(order)}

        # Sort nuts and bolts according to the predefined order
        nuts.sort(key=lambda x: order_map[x])
        bolts.sort(key=lambda x: order_map[x])

# Example usage:
if __name__ == '__main__':
    # Test case 1
    n = 5
    nuts = ['@', '%', '$', '#', '^']
    bolts = ['%', '@', '#', '$', '^']
    solution = Solution()
    solution.matchPairs(n, nuts, bolts)
    print("Nuts: ", ' '.join(nuts))   # Output: # $ % @ ^
    print("Bolts: ", ' '.join(bolts)) # Output: # $ % @ ^

    # Test case 2
    n = 9
    nuts = ['^', '&', '%', '@', '#', '*', '$', '?', '!']
    bolts = ['?', '#', '@', '%', '&', '*', '$', '^', '!']
    solution.matchPairs(n, nuts, bolts)
    print("Nuts: ", ' '.join(nuts))   # Output: ! # $ % & * ? @ ^
    print("Bolts: ", ' '.join(bolts)) # Output: ! # $ % & * ? @ ^
