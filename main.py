country_codes = {
  "+370":"Lithuania",
  "+371":"Latvia",
  "+372":"Estonia",
  "+373":"Moldova",
  "+374":"Armenia",
  "+375":"Belarus"
}

number = input("Ievadi telefona numuru!")
print(country_codes.get(number[:4])) if country_codes.get(number[:4]) != None else print("Neatradu šādu ierakstu! :(")