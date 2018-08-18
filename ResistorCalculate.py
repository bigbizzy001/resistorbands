import math


class Worker:
    # def __init__(self):
    #    # self.band_type = band_type
    #     pass

    def colors_band(self, color_band):
        '''a dictionary representation of the color bands with values'''
        color = {'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4',
                 'green': '5', 'blue': '6', 'violet': '7', 'gray': '8', 'white': '9'}
        return color[color_band]

    def resistor_tolerance(self, color):
        ''':returns the resistor tolerance for a 4-band and 5-band resistors'''
        tolerance = {'silver': 0.1, 'gold': 0.05, 'no color band': 0.2, 'brown': 0.01,
                     'red': 0.02, 'green': 0.005, 'blue': 0.0025, 'violet': 0.001}

        return tolerance[color]

    def three_color_multiplier(self, color):
        '''gives the color multiplier for a 3-band resistor'''
        multiplier = {'gold': 0.1, 'silver': 0.01}

        return multiplier[color]

    def three_color_band(self, color1, color2, color3):
        ''':returns the resistor value for a 3-band resistor'''
        a = self.colors_band(color1) + self.colors_band(color2)
        b = int(a) * self.three_color_multiplier(color3)

        return 'The resistor value is '+ str(b) + 'Ω'

    def four_color_band(self, color1, color2, color3, color4):
        ''':returns the resistor value for a 4-band resistor'''
        a = self.colors_band(color1) + self.colors_band(color2)
        b = int(a) * math.pow(10, int(self.colors_band(color3)))
        c = self.resistor_tolerance(color4)
        d = b * c

        e = round(b + d)
        f = round(b - d)

        if len(str(e)) > 6 and len(str(f)) > 6:
            return 'The resistor range is ' + str(f)+'Ω(' + str(f/1000000) + 'kΩ) ' + 'to ' + str(e)+'Ω(' + str(e/1000000) + 'kΩ)'
        # return 'The resistor range is ' + str(f)+'Ω(' + str(f/1000) + 'kΩ) ' + 'to ' + str(e)+'Ω(' + str(e/1000) + 'kΩ)'

    def five_color_band(self, color1, color2, color3, color4, color5):
        ''':returns the resistor value for a 5-band resistor'''
        a = self.colors_band(color1) + self.colors_band(color2) + self.colors_band(color3)
        b = int(a) * math.pow(10, int(self.colors_band(color4)))
        c = b * self.resistor_tolerance(color5)

        d = round(b + c)
        e = round(b - c)

        return 'The resistor range is ' + str(e)+'Ω(' + str(e/1000) + 'kΩ)' + ' to ' + str(d)+'Ω(' + str(d/1000) + 'kΩ)'

    def chip_resistors(self, val):
        ''':returns the chip resistor value'''
        if len(val) == 3:
            a = int(val[:2])
            b = int(val[2])

            return str(round(a * math.pow(10, b))) + 'Ω' + ' or ' + str(round(a * math.pow(10, b))/1000) + 'kΩ'
        else:
            return 'chip resistor value must be three(3) digits'




