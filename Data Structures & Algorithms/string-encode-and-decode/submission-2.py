class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = "".join([f"{len(s)}#{s}" for s in strs])
        #print(ret)
        return ret

    def decode(self, s: str) -> List[str]:
        strs = []

        i = 0
        while i < len(s):
            #print("i = ", i)
            j = s.find("#", i)
            str_len = int(s[i:j])
            i = j+1
            j = i + str_len
            strs.append(s[i:j])
            i = j
            #print(strs, i, j)
        return strs
