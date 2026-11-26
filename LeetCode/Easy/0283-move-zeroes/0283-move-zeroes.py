class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0이 아닌 숫자가 순서대로 들어갈 위치를 가리키는 포인터
        pos = 0

        # 1. 배열을 순회하며 0이 아닌 숫자를 앞쪽부터 차례대로 채움
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1
        
        # 2. 0이 아닌 숫자를 다 채운 뒤, 남은 뒷자리를 모두 0으로 채움
        for i in range(pos, len(nums)):
            nums[i] = 0


        # ---------
        # 또는 배열을 한 번만 순회하면서 0이 아닌 숫자를 pos와 맞교환
        # pos 위치에는 이미 확인이 끝난 0또는 자기자신이 있으므로 순서가 유지됨
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         if i != pos:
        #             nums[pos], nums[i] = nums[i], nums[pos]
        #        pos += 1