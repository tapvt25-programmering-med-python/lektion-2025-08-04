print("Hello World!") # Detta är en kommentar

my_name = "Christoffer" # Deklarera en variabel med ett värde, i detta fall en sträng
print(my_name) # Skriv ut innehållet i en variabel
print("Hello " + my_name)
age = "36" # Siffra som sträng
my_age = 36 # Datatypen int (heltal)

combined_age = int(age) + 10 # Här gör vi en typomvandling från en sträng till en int

print(age + str(10)) # Här gör vi en typomvandling från en int till en str

is_teacher = True # Datatypen boolean

favorite_hobby = input("Vad är din favorithobby?") # Input-metoden kan användas för att be användaren mata in något som vi sparar i en variabel
print("Min favorithobby: " + favorite_hobby)

name = input("Vad heter du?")

if name == "Christoffer": # If-sats med ett villkor som blir true eller false
    print("Du är lärare!")
elif name == "Magdalena":
    print("Du är utbildningsledare")
else: # Om inget stämmer går koden in hit
    print("Du är troligtvis student eller något annat")

if name == "Christoffer" or name == "Magdalena": # Här behöver ett av två villkor bli true
    print("Du är personal")