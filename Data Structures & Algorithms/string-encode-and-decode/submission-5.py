class Solution:

    def encode(self, strs: List[str]) -> str:
        full_str = ""

        for s in strs:
            full_str += str(len(s)) + "#" + s

        return full_str

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            jump = ""
            while s[i] != "#":
                jump += s[i]
                i += 1
            jump = int(jump)
            start = i + 1
            end = start + jump
            word = s[start:end]
            strs.append(word)
            i = end
        
        return strs
