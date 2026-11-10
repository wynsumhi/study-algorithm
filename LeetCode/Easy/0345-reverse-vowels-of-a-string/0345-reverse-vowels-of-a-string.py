class Solution:
    def reverseVowels(self, s: str) -> str:

        # 1. 문자열 내의 모든 모음(대문자 포함)을 순서대로 추출하여 리스트에 저장
        vowels = [char for char in s if char in 'aeiouAEIOU']

        # 2. 문자열의 글자 하나씩 수정하기 위해 리스트로 변환
        s_list = list(s)

        # 3. 문자열을 다시 순회하면서 모음 위치를 거꾸로 채워 넣는다.
        for i in range(len(s_list)):
            if s_list[i] in "aeiouAEIOU":
                # pop()은 리스트의 가장 마지막 요소를 꺼내므로,
                # 나중에 들어온 모음부터 차례대로 꺼내어 배치하게 된다.
                s_list[i] = vowels.pop()
            
        # 4. 리스트를 다시 하나의 문자열로 합쳐서 변환
        return ''.join(s_list)

        for x in range(len(s_list)):
            if s_list[x] in "aeiouAEIOU":
                s_list[x] = temp.pop(0)

            return ''.join(s_list)
            