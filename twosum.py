# twosum-ozbekchasi
# Bu sahifada leetcode dagi twosum mashqini yechimi ozbek tilida tushunarli qilib yaratilgan -->

from typing import List

import self as self


class Solution:
     def twoSum(self, nums: List[int], target: int) -> List[int]:
         for i in range(len(nums)):
             for j in range(i, len(nums)):
                 if nums[i] + nums[j] == target:
                     return [i, j]
         return []
     print(twoSum(self, nums, target))


""" Birinchisida korinib turibdiki for loop siklida har biri qiymati uchun 
    [nums] listidan olib keyin yana for loop sikliga qaytamiz va bu safar 
    j qiymati uchun huddi osha listdan birinchi qiymatini olamiz va olingan
    qiymatlarni qoshib targetga teng ekanligini if statment orqali aniqlaymiz 
    agar teng bolsa olingan qiymatlarni alohida listga solib uni ekranga chiqaramiz
    targetga teng bolmagan raqamlar chiqadigan bolsa unda bosh list bilan qaytamiz.
    unihanm ekrangga bosh list qilib chiqaramiz. """


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for idx, value in enumerate(nums):
            if target - value in values:
                return [values[target - value], idx]
            else:
                values[value] = idx
    nums = [3, 2, 4]
    target = 6
    print(twoSum(self, nums, target))
