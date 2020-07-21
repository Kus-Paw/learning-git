print("hello")
print("Wpisuje jakąs zmianę")

print ("lista zakupów")
shopping_dict = {
"piekarnia" : [ 'chleb'.capitalize(), 'pączek'.capitalize(), 'bułki'.capitalize()],
"warzywniak" : ['marchew'.capitalize(), 'seler'.capitalize(), 'rukola'.capitalize()]
}
#print(shopping_dict.values())
#print(shopping_dict.keys())
for product in shopping_dict.keys():  
    print("Idę do",["piekarnia".capitalize()], "kupuję tu następujące rzeczy:", shopping_dict ["piekarnia"])
    print("Idę do", ["warzywniak".capitalize()], "kupuję tu następujące rzeczy",shopping_dict ["warzywniak"])
    break
print("W sumie kupuję", len(shopping_dict["piekarnia"]) + len(shopping_dict["warzywniak"]), "produktów.")
