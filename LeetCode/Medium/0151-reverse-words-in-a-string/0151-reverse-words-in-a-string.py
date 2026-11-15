class Solution:
    def reverseWords(self, s: str) -> str:
        # 1. 공백을 기준으로 단어들을 리스트로 분리
        words = s.split()

        # 2. 단어 리스트의 순서를 뒤집기
        words.reverse()

        # 또는
        # words = words[::-1]
        
        # 3. 단어들을 하나의 공백으로 연결하여 반환
        return " ".join(words)
