def load(data, output_path):
    print("Cargando datos")
    data.to_csv(output_path, index = False)
    print(f"Datos cargados en {output_path}.")