import unittest

def CountClump(nums):
    if nums is None or len(nums) == 0:
        return 0  # Condition A, B
    count = 0
    prev = nums[0]
    in_clump = False
    
    for i in range(1, len(nums)):
        if nums[i] == prev:  # Condition C
            if not in_clump:  # Condition D
                in_clump = True
                count += 1
        else:
            in_clump = False
        prev = nums[i]

    return count

class TestCountClumps(unittest.TestCase):
    def test_none(self):
        self.assertEqual(CountClump(None), 0)  # Condition A (True)
    
    def test_empty(self):
        self.assertEqual(CountClump([]), 0)  # Condition A (False), B (True)

    def test_with_clumps(self):
        self.assertEqual(CountClump([1, 1, 2, 3, 3]), 2)  # Condition A (False), B (False), C (True), D (True)
    
    def test_no_clumps(self):
        self.assertEqual(CountClump([1, 2, 2, 3, 4]), 1)  # Condition A (False), B (False), C (False)

if __name__ == '__main__':
    unittest.main()
