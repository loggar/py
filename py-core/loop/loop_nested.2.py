languages = [['Spanish', 'English',  'French', 'German'],
             ['Python', 'Java', 'Javascript', 'C++']]

for lang in languages:
    print(lang)

for x in languages:
    print("------")
    for lang in x:
        print(lang)
