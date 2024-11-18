class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 10000, 100 전부 set화 해도 백만 딕셔너리의 key값에는 set불가
        answerDict = dict()
        for i in strs:
            tmp = "".join(sorted(i))
            if tmp not in answerDict:
                answerDict[tmp] = [i]
            else:
                answerDict[tmp] += [i]
        return sorted(list(answerDict.values()))