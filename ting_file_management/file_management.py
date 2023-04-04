import sys


def txt_importer(path_file):
    try:
        with open(path_file, mode="r") as file:
            if path_file.endswith(".txt"):
                return file.read().split("\n")

            else:
                print("Formato inválido", file=sys.stderr)
                # sys.stderr.write("Formato inválido")

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        # sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
