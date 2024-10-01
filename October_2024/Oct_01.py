class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def multiply_two_lists(self, first, second):
        MOD = 10**9 + 7
        
        # Convert the first linked list to a number
        num1 = 0
        while first:
            num1 = (num1 * 10 + first.data) % MOD
            first = first.next
        
        # Convert the second linked list to a number
        num2 = 0
        while second:
            num2 = (num2 * 10 + second.data) % MOD
            second = second.next
        
        # Multiply both numbers and take modulo
        result = (num1 * num2) % MOD
        
        return result
