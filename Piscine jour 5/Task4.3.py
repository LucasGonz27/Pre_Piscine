planning = [
    ["Monday", "3:30 PM", "Joe", "Sam"],
    ["Monday", "4:30 PM", "Bob", "Alice"],
    ["Tuesday", "3:30 PM", "Joe", "Bob", "Alice", "Sam"],
    ["Tuesday", "9:30 AM", "Joe", "Bob"],
]

nom = input("Donne moi un nom: ").strip()
nom = nom.capitalize()

for plan in planning:
    if nom in plan:
        print([plan[0], plan[1]])
