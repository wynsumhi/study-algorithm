class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 1. 두 문자열을 더한 결과가 순서에 상관없이 일치하지 않으면 공통 약수가 없음
        if str1 + str2 != str2 + str1:
            return ''

        # 2. 두 문자열 길이의 최대공약수를 구함
        gcd_length = math.gcd(len(str1), len(str2))

        return str1[:gcd_length]
            