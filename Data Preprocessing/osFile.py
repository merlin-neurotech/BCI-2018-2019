import os

items = os.listdir("/Users/jonathanlieberman/PycharmProjects/WizardHat2/scripts/data")

newList = []
for names in items:
    if names.endswith(".json") or "EEG" not in names:
        os.remove("/Users/jonathanlieberman/PycharmProjects/WizardHat2/scripts/data/" + names)



