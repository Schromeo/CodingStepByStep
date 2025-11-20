from typing import List
class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + ':' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            j = s.find(":",i)
            length = int(s[i:j])
            decoded.append(s[j+1: j+1+length])
            i = j + 1 + length
        return decoded
    
test = Codec()
print(test.encode(["Hello", "World"]))
print(test.decode("5:Hello5:World"))
print("Hello".find("l",4))