def find_lt_group(name):
    lt_groups = {
        5: ["Aya", "Shriya", "Lumi", "Anouk", "Walter", "Joeben", "Maria", "Davide", "Leon", "Calson", "Ilias", "Sophia", "Anna", "Markus", "Lucas", "Thaiss", "Fleming", "Wu", "Bey", "Emilie", "Bianka"],
        1: ["Bissola", "Ava", "Rasmus", "Christal", "Catherin", "Philine", "Farah", "Mirre", "Adam", "Scarlett", "Maximilian", "Rafael", "Josy", "Meng", "Collins", "David", "Weizhao", "Anna", "Nojus", "Porter", "Maria", "Nia"],
        2: ["Sean", "Maja", "Emma-Rose", "Irene", "Ana", "Alexandru", "Jacco", "Ömer", "Kimya", "Andre", "Jamie", "Yujia", "Koyo", "Viggo", "In", "Derrick", "Juliette", "Lucia", "Melody", "Federico"],
        3: ["Gadis", "Gabriella", "Alejandro", "Roy", "Nikko", "Wentao", "Felicia", "Micay", "Elnara", "Mana", "Khushi", "Sina", "Tadas", "Daniel", "Alexia", "Alexandra", "Viktor", "Clement", "Sihun", "Merijn", "Mark"],
        4: ["Dorottya", "Lotte", "Volodymyr", "Alva", "Brendan", "Callum", "Angela", "Regina", "Danielius", "Akira", "David", "Noel", "Gabriela", "Marwan", "Kazuya", "Callum", "Danielius", "Dasha", "Cem", "Asjfaaq", "Khushi", "Elpiniki", "Shuting", "Antonin", "Antonio", "Niki"]
    }
    
    for lt_number, names in lt_groups.items():
        if name in names:
            return f"{name} is in LT{lt_number}"
    
    return f"{name} is not in any LT group"

# Example usage:
print(find_lt_group("Aya"))  # Output: Aya is in LT5
print(find_lt_group("Markus"))  # Output: Markus is in LT5
print(find_lt_group("Rafael"))  # Output: Rafael is in LT1
print(find_lt_group("John"))  # Output: John is not in any LT group
