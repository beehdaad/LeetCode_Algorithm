from typing import List


class Solution:
    """
    This class takes a list of numbers and a target number
    The sum of two numbers must be equal to
    the target and the output is a list of number indexes
    In case of change, a message will be returned as output
    """
    @staticmethod
    def twoSum(numbers: List[int], target: int) -> List[int]:
        count = len(numbers)
        for number in range(count):
            for num in range(count):
                if number >= num:
                    continue
                elif (numbers[number] + numbers[num]) == target:
                    list_of_index = [number, num]
                    return list_of_index
        else:
            return f"The sum of no two numbers was equal to the '{target}'"
