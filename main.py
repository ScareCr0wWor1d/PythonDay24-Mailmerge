with open("./input/letter.txt", encoding='utf-8') as letter:
    lettre = letter.read()

with open("./input/name.txt", encoding='utf-8') as names:
    for line in names:
        new_letter = lettre.replace("[Name]", line.replace("\n", ""))
        lettername = line.replace("\n", "") + ".txt"
        with open(f"./output/ready_letter/{lettername}", 'w', encoding='utf-8') as let:
            let.write(new_letter)
