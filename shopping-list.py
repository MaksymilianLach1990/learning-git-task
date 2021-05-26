# Zadanie 1 "Wyprawa po zakupy."
shopping_list = {'piekarnia': ('chleb', 'bułki', 'pączek'), 
                 'warzywniak': ('marchew', 'seler', 'rukola')}


# Nazwy sklepów i produktów wypisane wielką literą
for shop, things in shopping_list.items():
    print("Idę do {} kupuję tu następujące rzeczy: {}".format(shop.capitalize(), str(things).title()))
