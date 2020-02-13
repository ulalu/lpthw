name = "Ursula MV"
age = 29
height = 69
weight = 135
eyes = "Brown"
teeth = "white"
hair = "Brown"
height_cm = round(height * 2.54)
weight_kg = round(weight / 2.205)

print(f"Let's talk about {name}.")
print(f"She's {height} inches tall.")
print(f"She's {weight} pounds heavy.")
print(f"In metric, that's {height_cm} cm tall and {weight_kg} kg heavy")
print("Actually that's not too heavy.")
print(f"She's got {eyes} eyes and {hair} hair.")
print(f"Her teeth are usually {teeth} depending on the tea intake.")

total = age + height + weight


print(f"If I add {age}, {height}, and {weight} I get {total}")