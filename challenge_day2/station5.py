import pandas as pd

def solution_station_5(name):
    teamsnames= {
        5: ["Aya", "Shriya", "Lumi", "Anouk", "Walter", "Joeben", "Maria", "Davide", "Leon", "Calson", "Ilias", "Sophia", "Anna", "Markus", "Lucas", "Thaiss", "Fleming", "Wu", "Bey", "Emilie", "Bianka"],
        1: ["Bissola", "Ava", "Rasmus", "Christal", "Catherin", "Philine", "Farah", "Mirre", "Adam", "Scarlett", "Maximilian", "Rafael", "Josy", "Meng", "Collins", "David", "Weizhao", "Anna", "Nojus", "Porter", "Maria", "Nia"],
        2: ["Sean", "Maja", "Emma-Rose", "Irene", "Ana", "Alexandru", "Jacco", "Ömer", "Kimya", "Andre", "Jamie", "Yujia", "Koyo", "Viggo", "In", "Derrick", "Juliette", "Lucia", "Melody", "Federico"],
        3: ["Gadis", "Gabriella", "Alejandro", "Roy", "Nikko", "Wentao", "Felicia", "Micay", "Elnara", "Mana", "Khushi", "Sina", "Tadas", "Daniel", "Alexia", "Alexandra", "Viktor", "Clement", "Sihun", "Merijn", "Mark"],
        4: ["Dorottya", "Lotte", "Volodymyr", "Alva", "Brendan", "Callum", "Angela", "Regina", "Danielius", "Akira", "David", "Noel", "Gabriela", "Marwan", "Kazuya", "Callum", "Danielius", "Dasha", "Cem", "Asjfaaq", "Khushi", "Elpiniki", "Shuting", "Antonin", "Antonio", "Niki"]}

    df = pd.read_excel(teamnames)
    
    try:
        team = df.loc[df['Student firstname'] == name, 'Team'].values[0]
        return int(team)
    except IndexError:
        return "This person is not in the course"
