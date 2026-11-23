class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        # 첫 번째(가장 작은 수)를 무한대로 설정 (아직 비교 전이라 어떤 숫자든 들어올 수 있게 함)
        first = float('inf')
        # 두 번째 수(첫 번쨰 수보다 큰 수 후보)를 무한대로 설정
        second = float('inf')

        # 배열의 숫자를 앞에서부터 하나씩 꺼내며 확인
        for n in nums:
            # 현재 숫자가 지금껏 본 가장 작은 수 이라라면 first를 더 작은 값으로 갱신
            if n <= first:
                first = n
            # first보다 크지만 second 이하려면, 두 번째 후보로 쓸 수 있는 가장 작은 값으로 second 갱신
            elif n <= second:
                second = n
            # first보다도 크고 second 보다도 크다는 뜻이므로 증가하는 3개 숫자 완성!
            else:
                return True
            
        # 끝까지 돌아도 조건에 맞는 세 숫자를 못 찾았다면 False 반환
        return False