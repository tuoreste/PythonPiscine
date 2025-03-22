ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#lists: mutable, lists in python can be changed!
ft_list[1] = "World!" 

#tuple: immutable, tuples are unchangeable
#...trick: convert tuple to a list, make changes then reconvert to tuples.
templateList = list(ft_tuple)
templateList[1] = "Germany!"
ft_tuple = tuple(templateList)

#ft_set: immutable
ft_set.remove("Hello")
ft_set.remove("tutu!")
newItems = {"Hello", "Heilbronn!"}
ft_set.update(newItems)

#ft_set: mutable
ft_dict["Hello"] = "42Heilbronn!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

print("\n\n\n\n==NOTES:==\n")
print("LIST:    Ordered    Allow Duplicates            Mutable     []")
print("TUPLE:   Ordered    Allow Duplicates            Immutable   ()")
print("SET:     Ordered    Does Not Allow Duplicates   Immutable   {\}")
print("DICT:    Yes/No     Does Not Allow Duplicates   Mutable     {key\:value\}")
