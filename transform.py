def transform(data):
    print("Transformando datos.")

    #Rellenar Sales restantes
    data["Sales"] = data["Sales"].fillna(0)

    #Rellenar Quantity restantes
    if "Quality" not in data.columns:
        data["Quantity"] = 1

    data["Quantity"] = data["Quantity"].fillna(1)

    #Calcular Total Sales
    data["Total Sales"] = data["Sales"] * data["Quantity"]

    #Nivel de Sales
    data["Level Sales"] = data["Sales"].apply(lambda x: "High Sales" if x >= 500 else "Low Sales")

    return data