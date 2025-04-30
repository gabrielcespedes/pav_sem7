from extract import extract
from transform import transform
from load import load

def main():
    print("\n -- Pipeline ETL: Ventas -- \n")

    #Solicitar archivos
    input_file = input("Ingrese el nombre del archivo de entrada: ")
    output_file = input("Ingrese el nombre del archivo de salida: ")

    #Orquestar el flujo
    data_raw = extract(input_file)
    data_clean = transform(data_raw)
    load(data_clean, output_file)

    print("Pipeline finalizado correctamente.")

if __name__ == "__main__":
    main()