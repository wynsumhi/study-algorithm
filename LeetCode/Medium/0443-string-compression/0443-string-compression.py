class Solution:
    def compress(self, chars: list[str]) -> int:
        # 압축된 결과를 chars 배열의 어느 위치에 쓸지 가리키는 포인터 (쓰기 위치)
        write = 0
        # 원본 배열 chars를 앞에서부터 읽어나가는 포인터 (읽기 위치)
        read = 0
        # 입력 배열의 전체 길이
        n = len(chars)

        # 아직 읽지 않은 문자가 남아 있는 동안 반복
        while read < n:
            # 현재 연속 그룹의 기준이 되는 문자 저장
            char = chars[read]
            # 현재 문자가 몇 번 연속으로 나오는지 세는 변수
            count = 0

            # 배열 끝을 넘지 않고, 현재 문자가 기준 문자(char)와 같은 동안 계속 전진
            while read < n and chars[read] == char:
                # 다음 문자를 확인하기 위해 읽기 포인터를 한 칸 이동
                read += 1
                # 연속된 문자 개수를 1 증가
                count += 1

            # 연속 그룹 세기가 끝났으므로, 먼저 기준 문자(char)를 write 위치에 기록
            chars[write] = char
            # 다음 문자를 쓸 수 있도록 쓰기 포인터를 한 칸 이동
            write += 1

            # 연속된 개수가 2 이상일 때만 숫자를 기록 (1개일 때는 생략)
            if count > 1:
                # 12처럼 두 자리 이상일 떄도 한 글자씩 쪼개기 위해 문자열로 변환해 순회
                for digit in str(count):
                    # 각 자릿수 문자('1', '2' 등)을 write 위치에 저장
                    chars[write] = digit
                    # 다음 칸을 위해 쓰기 포인터를 한 칸 이동
                    write += 1
            
        # write는 방금 쓴 마지막 칸 다음 위치를 가리키므로, 곧 압축된 총 길이가 됨
        return write