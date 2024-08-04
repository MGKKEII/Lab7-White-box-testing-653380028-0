import unittest

class CountClump:
    """
    This class provides a method to count the number of "clumps" in a list of integers.
    A clump is a run of 2 or more of the same adjacent numbers.
    """

    @staticmethod
    def count_clumps(nums):
        """
        Counts the number of "clumps" in a list of integers.
        A clump is a run of 2 or more of the same adjacent numbers.

        Args:
            nums: A list of integers.

        Returns:
            The number of clumps in the list.
        """
        if nums is None or len(nums) == 0:
            return 0
        count = 0
        prev = nums[0]
        in_clump = False

        for i in range(1, len(nums)):
            if nums[i] == prev:
                if not in_clump:
                    in_clump = True
                    count += 1
            else:
                in_clump = False
            prev = nums[i]

        return count

class TestCountClumps(unittest.TestCase):
    def test_none(self):
        self.assertEqual(CountClump.count_clumps(None), 0)  # ตรวจสอบกรณี None
    
    def test_empty(self):
        self.assertEqual(CountClump.count_clumps([]), 0)  # ตรวจสอบกรณีรายการว่าง

    def test_with_clumps(self):
        self.assertEqual(CountClump.count_clumps([1, 1, 2, 3, 3, 4, 4, 4]), 3)  # ตรวจสอบกรณีมี clumps
    
    def test_without_clumps(self):
        self.assertEqual(CountClump.count_clumps([1, 2, 3, 4]), 0)  # ตรวจสอบกรณีไม่มี clumps

if __name__ == '__main__':
    unittest.main()
