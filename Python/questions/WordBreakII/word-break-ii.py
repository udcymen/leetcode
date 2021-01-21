class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s or not wordDict or len(wordDict) == 0:
            return []

        return self.dfs(s, wordDict, {})
        
    def dfs(self, s: str, wordDict: List[str], memo: dict[str, List[str]]) -> None:
        if s in memo:
            return memo[s]
        
        if s == "":
            return [""]
        
        result = []

        for word in wordDict:
            if s.startswith(word):
                for sub in self.dfs(s[len(word):], wordDict, memo):
                    result.append(word + ("" if sub == "" else " ") + sub)
        
        memo[s] = result
        
        return result