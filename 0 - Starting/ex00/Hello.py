ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Lists are ordered and mutable.
ft_list[1] = "World!"

# Tuples are immutable packages.
ft_tuple = ("Hello", "France!")

# Sets are unordered and mutable.
# Printing order is random.
ft_set.remove("tutu!")
ft_set.add("Paris!")

# Dictionaries are Key-Value pairs.
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)