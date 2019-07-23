languages = [['Spanish', 'English',  'French', 'German'],
             ['Python', 'Java', 'Javascript', 'C++']]

for x in languages:
    print("------")
    for lang in x:
        if lang == "German":
            continue
        print(lang)
