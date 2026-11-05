class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # 1. 전체 아이들 중 가장 많은 사탕 개수 구하기
        max_candies = max(candies)

        # 2. 각 아이의 사탕에 extraCandies를 더 했을 때 최댓값 이상이 되는지 확인하여 True/False로 바꾸기
        return [candy + extraCandies >= max_candies for candy in candies]