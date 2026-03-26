class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # int(string, 2) converts binary string to integer
        # bin(number) converts integer to binary string (starts with '0b')
        return bin(int(a, 2) + int(b, 2))[2:]