COLOR_TO_CODE = {"Aqua": "#00ffff", "Azure1": "#f0ffff",
                 "Beige": "#f5f5dc", "Bistre": "#3d2b1f",
                 "Black": "#000000", "Blue1": "#0000ff",
                 "BlueViolet": "#8a2be2", "Bole": "#79443b",
                 "Bronze": "#cd7f32", "Brass": "#b5a642"}

COLOR_TO_CODE = {color.lower():code for color, code in COLOR_TO_CODE.items()}

color = input("Enter a color name: ").lower()
while color != "":
    if color in COLOR_TO_CODE:
        print(COLOR_TO_CODE[color])
    else:
        print("Invalid color name")
    color = input("Enter a color name: ").lower()