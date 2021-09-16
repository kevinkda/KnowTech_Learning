# -*- encoding: utf-8 -*-
"""
@File       :   
@Contact    :   kevin_kda@yahoo.com.au
@License    :   (C)Copyright 2017-2021, KevinKDA

@Modify Time        @Author     @Version    @Description
----------------    ----------- --------    ------------
2021/8/9 2:52     Kevin Tang  0.0.1       None
"""
import doctest
import math
from typing import List
from icecream import ic
from loguru import logger
from traitlets import Int


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def inputNode(nums: List[int]) -> ListNode:
    listNode: ListNode = ListNode()
    cursor = listNode
    for i in range(0, len(nums)):
        cursor.val = nums[i]
        if i != len(nums) - 1:
            cursor.next = ListNode()
            cursor = cursor.next
    return listNode


def getNumsLen(nums):
    if nums > 0:
        return int(math.log10(nums)) + 1
    elif nums == 0:
        return 1
    else:
        return int(math.log10(-nums)) + 2


def inputNodeByInt(nums: int) -> ListNode:
    listNode: ListNode = ListNode()
    temp = nums
    i = getNumsLen(nums)
    cursor = listNode
    for j in range(0, i):
        cursor.val = temp % 10
        temp = temp // 10
        if j != (i):
            cursor.next = ListNode()
            cursor = cursor.next

    # while temp != 0:
    #     temp = temp / 10
    return listNode


def nodeToList(node: ListNode) -> List[int]:
    cursor = node
    list: List[int] = []
    while cursor.next != None:
        list.append(cursor.val)
        cursor = cursor.next
    return list


def lenNode(node: ListNode) -> int:
    cursor = node
    count = 0
    while cursor.next != None:
        count += 1
        cursor = cursor.next
    # ic(count)
    return count


def getNodeNunms(node: ListNode) -> int:
    cursor = node
    retNum: int = 0
    count: int = 1
    while cursor != None:
        # while cursor != None and cursor.next != None:
        count *= 10
        retNum = retNum + cursor.val * count
        cursor = cursor.next
    return retNum//10


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> List[int]:
        """
        :param l1:
        :param l2:
        :return:

        >>> ic(nodeToList(Solution().addTwoNumbers(l1=inputNode(nums=[2, 4, 3]), l2=inputNode(nums=[5, 6, 4]))))
        [7, 0, 8]
        >>> ic(nodeToList(Solution().addTwoNumbers(l1=inputNode(nums=[0]), l2=inputNode(nums=[0]))))
        [0]
        >>> ic(nodeToList(Solution().addTwoNumbers(l1=inputNode(nums=[9, 9, 9, 9, 9, 9, 9]), l2=inputNode(nums=[9, 9, 9, 9]))))
        [8, 9, 9, 9, 0, 0, 0, 1]
        """
        sum: int = getNodeNunms(l1) + getNodeNunms(l2)
        ic(sum)
        return inputNodeByInt(sum)


# ic(Solution().removeDuplicates_TypeA_Scheme_A(nums=[1, 1, 2]))
# print("------------")
# ic(nodeToList(Solution().addTwoNumbers(l1=inputNode(nums=[2, 4, 3]), l2=inputNode(nums=[5, 6, 4]))))
# ic(nodeToList(Solution().addTwoNumbers(l1=inputNode(nums=[2, 4, 3]), l2=inputNode(nums=[5, 8, 4]))))
# ic(nodeToList(Solution().addTwoNumbers(l1=inputNode(nums=[0]), l2=inputNode(nums=[0]))))
ic(nodeToList(Solution().addTwoNumbers(l1=inputNode(nums=[2, 4, 9]), l2=inputNode(nums=[5, 6, 4, 9]))))
# ic(nodeToList(Solution().addTwoNumbers(l1=inputNode(nums=[9, 9, 9, 9, 9, 9, 9]), l2=inputNode(nums=[9, 9, 9, 9]))))

ic(doctest.testmod())
