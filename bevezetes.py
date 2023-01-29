def beker():
    auto_neve = input("Autó neve: ")
    gyartasi_datum = int(input("Gyártási dátum: "))
    print("\nI/A: ")
    print(f"\t Autó neve: {auto_neve}")
    print(f"\t Gyártási dátum: {gyartasi_datum}")
    print("I/B: ")

    if gyartasi_datum == 2023:
        print(f"\t Ez az {auto_neve} friss gyártás.")
    elif gyartasi_datum < 2000:
        print(f"\t Ez az {auto_neve} öreg autó.")
    else:
        print(f"\tEz az {auto_neve} átlagos korú.")



