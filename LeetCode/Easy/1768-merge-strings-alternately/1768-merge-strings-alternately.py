class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        # word1과 word2를 번갈아가며 가리킬 투 포인터(i, j)를 0으로 시작
        i, j = 0, 0

        # 두 단어 중 하나라도 아직 안 끝났다면 계속 반복
        while i < len(word1) or j < len(word2):

            # word1이 아직 남아있다면 글자 하나를 꺼내서 결과통에 넣고, i를 1증가
            if i < len(word1):
                result.append(word1[i])
                i += 1

            # word2가 아직 남아있다면 글자 하나를 꺼내서 결과통에 넣고, j를 1증가
            if j < len(word2):
                result.append(word2[j])
                j += 1

        # 리스트에 모인 글자들을 하나의 문자열로 합쳐서 반환
        return "".join(result)