class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # 결과 배열을 1로 초기화
        result = [1] * len(nums)
        
        # 왼쪽 누적 곱 계산
        left_product = 1
        for i in range(len(nums)):
            # 현재 자리에 내 왼쪽에 있는 수들의 총곱 먼저 저장
            result[i] = left_product
            # 다음 칸을 위해 현재 숫자를 left_product에 누적하여 곱함
            left_product *= nums[i]
            
        # 오른쪽 누적 곱 계산 및 바로 곱해주기
        right_product = 1
        # 오른쪽 끝에서부터 왼쪽으로 역순 순회
        for i in range(len(nums) - 1, -1, -1):
            # 아까 구한 왼쪽 누적 곱에 내 오른쪽에 있는 수들의 총곱을 곱함
            result[i] *= right_product
            # 다음 칸(왼쪽)을 위해 현재 숫자를 right_product에 누적하여 곱함
            right_product *= nums[i]
            
        return result