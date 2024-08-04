import unittest

def CountClump(nums):
    if nums is None or len(nums) == 0:
        return 0  # Branch A (True)
    count = 0
    prev = nums[0]
    in_clump = False
    
    for i in range(1, len(nums)):
        if nums[i] == prev:  # Branch B
            if not in_clump:  # Branch C
                in_clump = True
                count += 1
        else:  # Branch D
            in_clump = False
        prev = nums[i]

    return count

class TestCountClumps(unittest.TestCase):
    def test_none(self):
        self.assertEqual(CountClump(None), 0)  # Branch A (True)
    
    def test_empty(self):
        self.assertEqual(CountClump([]), 0)  # Branch A (True)

    def test_with_clumps(self):
        self.assertEqual(CountClump([1, 1, 2, 3, 3]), 2)  # Branch A (False), B (True), C (True), D (False)
    
    def test_some_clumps(self):
        self.assertEqual(CountClump([1, 2, 2, 3, 4]), 1)  # Branch A (False), B (False), C (False), D (True)

if __name__ == '__main__':
    unittest.main()
