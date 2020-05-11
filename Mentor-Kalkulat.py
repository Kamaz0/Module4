def dodaj(x, y):
  return x + y

def odejmij(x, y):
 return x - y

def pomnoz(x, y):
  return x * y

def podziel(x, y):
  return x / y

print("Podaj działanie, posługując się odpowiednią liczbą: ")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnozenie")
print("4. Dzielenie")

choice = input("Ktora operaje chcesz wykonac? Wybierz 1/2/3/4): ")

num1 = float(input("Podaj pierwszą wartość: "))
num2 = float(input("Podaj drugą wartość: "))

if choice == '1':
  print(num1,"+",num2,"=", dodaj(num1,num2))
elif choice == '2':
  print(num1,"-",num2,"=", odejmij(num1,num2))
elif choice == '3':
  print(num1,"x",num2,"=", pomnoz(num1,num2))
elif choice == '4':
  print(num1,":",num2,"=", podziel(num1,num2))
else:
  print("Nieprawidlowa wartosc")