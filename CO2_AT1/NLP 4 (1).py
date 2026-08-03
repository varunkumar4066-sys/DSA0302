words = ["writes", "writing", "written"]

print("{:<12}{:<25}{:<12}{:<12}{:<12}".format(
    "Word","State Path","Pattern","Root","Normalized"))

for word in words:

    if word == "writes":
        path = "Start->Verb->+s->End"
        pattern = "Regular"

    elif word == "writing":
        path = "Start->Verb->+ing->End"
        pattern = "Regular"

    elif word == "written":
        path = "Start->Irregular->End"
        pattern = "Irregular"

    print("{:<12}{:<25}{:<12}{:<12}{:<12}".format(
        word,path,pattern,"write","write"))