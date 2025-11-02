# Pizza
# Toppings - corn, paneer, cheese, jalapeño, olives, capsicum, tomato, onion
# Crust - thin crust, cheese burst, wheat thin

def make_pizza(*toppings):
    return f"Pizza with toppings: {', '.join(toppings)}"

Soumya = make_pizza('corn', 'paneer', 'cheese', 'jalapeño')
print(Soumya)

Ankita = make_pizza('olives', 'capsicum', 'tomato', 'onion', 'mushroom')
print(Ankita)

Raj = make_pizza('chicken', 'pepperoni', 'sausage')
print(Raj)

Vikram = make_pizza('veggie', 'bbq chicken', 'spinach', 'feta cheese')
print(Vikram)
