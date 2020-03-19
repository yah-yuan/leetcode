class Solution:
    def intToRoman(self, num: int) -> str:
        _1 = ('', 'I','II','III','IV','V', 'VI', 'VII', 'VIII', 'IX')
        _10 = ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC')
        _100 = ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM')
        _1000 = ('', 'M', 'MM', 'MMM')
        res = ''
        res += _1000[int(num/1000)]
        res += _100[int((num%1000)/100)]
        res += _10[int((num%100)/10)]
        res += _1[int(num%10)]
        return res