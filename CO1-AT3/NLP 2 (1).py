def dfa(string):
    state = "q0"
    path = ["q0"]

    for ch in string:
        if state == "q0":
            if ch == 'a':
                state = "q1"
            else:
                state = "q0"

        elif state == "q1":
            if ch == 'a':
                state = "q1"
            else:
                state = "q2"

        elif state == "q2":
            if ch == 'a':
                state = "q1"
            else:
                state = "q0"

        path.append(state)

    print("\nInput :", string)
    print("Transition Path :", " → ".join(path))

    if state == "q2":
        print("Accepted")
    else:
        print("Rejected")


n = int(input("Enter number of strings: "))

for i in range(n):
    s = input("Enter string: ")
    dfa(s)