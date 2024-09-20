class Solution:
    # Returns count of buildings that can see sunlight
    def countBuildings(self, height):
        # The first building always sees the sunrise
        count = 1
        max_height = height[0]  # The height of the first building
        
        # Traverse the remaining buildings
        for i in range(1, len(height)):
            if height[i] > max_height:
                count += 1
                max_height = height[i]
        
        return count
