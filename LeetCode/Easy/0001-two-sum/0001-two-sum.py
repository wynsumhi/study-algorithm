class Solution:
    def twoSum(self, nums: list[int], target:int) -> list[int]:
        # 1. 지나쳐 온 숫자들과 그 인덱스를 저장할 빈 딕셔너리(장부) 생성
        # 형태: { 숫자 : 인덱스 }
        seen = {}

        # 2. 리스트를 처음부터 끝까지 하나씩 확인
        # enumerate는 (인덱스, 숫자) 쌍으로 꺼내줌
        for i, num in enumerate(nums):

            # 3. 목표값(target)에서 현재 숫자(num)를 빼서,
            # 내가 찾고 있는 짝궁 숫자(temp)가 무엇인지 계산
            temp = target - num

            # 4. 만약 그 짝궁 숫자를 이미 예전에 지나쳐온 적이 있다면? (장부에 있다면)
            if temp in seen:
                # 짝궁의 인덱스(seen[temp])와 현재 나의 인덱스(i)를 바로 반환
                return [seen[temp], i]

            # 5. 짝궁을 아직 못 찾았다면,
            # 방금 확인한 내 숫자와 인덱스를 장부(seen)에 기록해 두고 다음으로 넘어감
            seen[num] = i