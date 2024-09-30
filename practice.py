Items = ["candy bar", "water bottle", "trash bags", "soda", "milk"]
Prices = [2.49, 5, 9.99, 2.99, 4.99]

print("Length of items", len(Items))
print("What is this doing", range(len(Items)))
for i in range(len(Items)):
    print(f"I bought {Items[i]}for ${Prices[i]}")

total_cost = 0
for c in Prices:
    total_cost = total_cost + c
print(f"I spent ${total_cost} at Walmart")

#cheapest =Prices[0]
#for i in range(len(Prices)):
    if(Prices[i] <= cheapest):
        cheapest = Prices[i]
        name = Items[i]
#print(f"The cheapest item was {name}")
#print(f"The most expensive item was {name}")
least = Prices.index(min(Prices))
print(f"The cheapest item was {Items[least]}")
most = Prices.index(max(Prices))
print(f"The most expensive item was {Items[most]}")