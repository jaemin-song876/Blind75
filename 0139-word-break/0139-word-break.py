class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_set = set(wordDict)
        n = len(s)
        #모두 false로 채운 n+1의 리스트 생성
        dp = [False]*(n + 1) 

        #starting point
        dp[0] = True

        #go through list
        for i in range(n +1):
            if dp[i] == True:
                for j in range(i+1, n+1):
                    current_word = s[i:j]

                    if current_word in word_set:
                        dp[j] = True

        return dp[n]
                    