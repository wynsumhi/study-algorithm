class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        count = 0
        length = len(flowerbed)
        
        while i < length:

            # 1. 현재 자리가 비어 있고, 양옆도 안전한지 확인
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
                
                # 꽃을 심을 수 있음
                flowerbed[i] = 1  # 1로 바꿔서 다음에 영향 주게 함
                count += 1        # 심은 개수 증가
                i += 2            # 바로 다음 칸은 못 심으니까 두 칸 건너뛰기
            else:
                # 못 심으면 그냥 한 칸 앞으로 이동
                i += 1
                
        # 우리가 심은 총 개수가 n 이상인지 확인
        return count >= n