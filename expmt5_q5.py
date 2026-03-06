# Priyanshu Pabari 590022242
n = int(input("Enter number of movies: "))
movies = {}
for i in range(n):
    name = input("\nEnter movie name: ")
    year = int(input("Enter release year: "))
    director = input("Enter director name: ")
    cost = float(input("Enter production cost: "))
    collection = float(input("Enter collection made: "))

    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection
    }
print("\nAll Movie Details:")
for name in movies:
    print("\nMovie Name:", name)
    print("Year:", movies[name]["year"])
    print("Director:", movies[name]["director"])
    print("Cost:", movies[name]["cost"])
    print("Collection:", movies[name]["collection"])

print("\nMovies released before 2015:")
for name in movies:
    if movies[name]["year"] < 2015:
        print(name)
print("\nMovies that made profit:")
for name in movies:
    if movies[name]["collection"] > movies[name]["cost"]:
        print(name)
search_director = input("\nEnter director name to search: ")
print("Movies directed by", search_director, ":")
for name in movies:
    if movies[name]["director"] == search_director:
        print(name)