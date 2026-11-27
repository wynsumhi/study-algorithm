class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
            # s에서 현재 맞춰야 할 글자의 인덱스
            i = 0

            # t를 한 글자씩 순회
            for j in t:
                # 아직 s에 남은 글자가 있고, 현재 t의 글자(j)와 일치하면 다음 글자로 이동
                if i < len(s) and s[i] == j:
                    i += 1
            
            # s의 모든 글자를 순서대로 다 찾았으면 i가 len(s)와 같음
            return i == len(s)