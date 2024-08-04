import unittest

def CountClump(nums):
    if nums is None or len(nums) == 0:
        return 0  # Block A
    count = 0  # Block B
    prev = nums[0]  # Block C
    in_clump = False  # Block D
    
    for i in range(1, len(nums)):  # Block E
        if nums[i] == prev:  # Block F
            if not in_clump:  # Block G
                in_clump = True
                count += 1
        else:  # Block H
            in_clump = False
        prev = nums[i]  # Block I

    return count  # Block J

class TestCountClumps(unittest.TestCase):
    def test_none(self):
        self.assertEqual(CountClump(None), 0)  # Block A
    
    def test_empty(self):
        self.assertEqual(CountClump([]), 0)  # Block A

    def test_with_clumps(self):
        self.assertEqual(CountClump([1, 1, 2, 3, 3]), 2)  # Block B, C, D, E, F, G, H, I, J
    
    def test_some_clumps(self):
        self.assertEqual(CountClump([1, 2, 2, 3, 4, 4]), 2)  # Block B, C, D, E, F, G, H, I, J

if __name__ == '__main__':
    unittest.main()
