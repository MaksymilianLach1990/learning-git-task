# Zadanie 1 "Wyprawa po zakupy."
shopping_list = {'piekarnia': ('chleb', 'bułki', 'pączek'), 
                 'warzywniak': ('marchew', 'seler', 'rukola')}
namber_of_products = 0
# Nazwy sklepów i produktów wypisane wielką literą
for shop, things in shopping_list.items():
    print("Idę do {} kupuję tu następujące rzeczy: {}".format(shop.capitalize(), str(things).title()))
    namber_of_products += len(list(things))
#  Wyświetla sumę kupionych produktów
print("W sumię kupuję {} produktów".format(namber_of_products))
