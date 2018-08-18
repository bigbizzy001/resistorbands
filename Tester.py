import ResistorCalculate as r

c = r.Worker()
print(c.colors_band('green'))
print(c.chip_resistors('562'))

print(c.three_color_band('red', 'gray', 'gold'))
print(c.four_color_band('red', 'green', 'gray', 'gold'))
print(c.five_color_band('orange', 'blue',  'gray', 'black', 'green'))
print(c.chip_resistors.__doc__)
print(c.resistor_tolerance.__doc__)

print(c.resistor_tolerance('green'))

