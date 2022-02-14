with open("russian_nouns.txt", encoding='utf8') as f:
    with open("data", "w", encoding='utf8') as f1:
        for line in f:
            if len(line) == 6:
                f1.write(line)
