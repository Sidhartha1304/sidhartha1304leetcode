class Solution(object):
    def convertTemperature(self, celsius):
        Kelvin=celsius+273.15
        Fahrenhet=celsius*1.80+32.00
        return Kelvin,Fahrenhet
        