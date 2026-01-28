class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            # 1. 홀수 길이 중심 확장
            l, r = i, i #중심이 (i,i)에서시작
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1

            # 2. 짝수 길이 중심 확장
            l, r = i, i + 1 #중심이 (i,i+1)에서 시작
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1

        return ans