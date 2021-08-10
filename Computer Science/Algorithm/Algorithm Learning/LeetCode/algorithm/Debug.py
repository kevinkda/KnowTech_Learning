# -*- encoding: utf-8 -*-
"""
@File       :   
@Contact    :   kevin_kda@yahoo.com.au
@License    :   (C)Copyright 2017-2021, KevinKDA

@Modify Time        @Author     @Version    @Description
----------------    ----------- --------    ------------
2021/8/9 2:52     Kevin Tang  0.0.1       None
"""
from typing import List
from icecream import ic
from loguru import logger


class Solution:
    # def removeDuplicates_TypeA_Scheme_A(self, nums: List[int]) -> int:
    def removeDuplicates_TypeA_Scheme_A(self, nums: List[int]) -> tuple[int, list[int]]:
        if not nums:
            # return 0
            return 0, nums
        maxId: int = len(nums)
        currentId = cursor = 1
        while cursor < maxId:
            ic(maxId, currentId, cursor, nums)
            if nums[cursor] != nums[cursor - 1]:
                nums[currentId] = nums[cursor]
                currentId += 1
                # maxId -= 1
            cursor += 1
        ic("Result", maxId, currentId, cursor, nums[0:currentId], nums)
        # return currentId
        return currentId, nums[0:currentId]


# ic(Solution().removeDuplicates_TypeA_Scheme_A(nums=[1, 1, 2]))
# print("------------")
ic(Solution().removeDuplicates_TypeA_Scheme_A(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
