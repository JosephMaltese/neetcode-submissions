class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        temp = n

        while temp >= 1:
            bit = temp % 2
            temp = temp // 2
            bits.append(bit)
        while len(bits) < 32:
            bits.append(0)
        res = 0
        m = len(bits)
        for i in range(len(bits)):
            res += bits[i] * (2**(m-1-i))
        return res

        