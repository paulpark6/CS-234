import modules.pair as pair

# Create an instance of the Pair class
p = pair.Pair("paul", "park")

# Print the instance of Pair
print(p)

print("paul" in p)
print("pk" in p)

p.add_first("junwon")
print(p)