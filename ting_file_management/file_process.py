import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file = txt_importer(path_file)
    dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    if len(instance.data) > 0:
        names = [e["nome_do_arquivo"] for e in instance.data]
        if path_file not in names:
            instance.enqueue(dict)
            print(dict, file=sys.stdout)

    else:
        instance.enqueue(dict)
        print(dict, file=sys.stdout)


def remove(instance):
    if len(instance.data) > 0:
        file = instance.dequeue()["nome_do_arquivo"]
        print(f"Arquivo {file} removido com sucesso", file=sys.stdout)

    else:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    try:
        value = instance.search(position)
        print(value, file=sys.stdout)

    except IndexError:
        print("Posição inválida", file=sys.stderr)
