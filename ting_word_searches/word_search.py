def exists_word(word, instance):
    result = []
    for dict in instance.data:
        lines = []
        for index, line in enumerate(dict["linhas_do_arquivo"]):
            words = line.lower().replace(".", "").split(" ")
            if word.lower() in words:
                lines.append({"linha": index + 1})

        if len(lines) > 0:
            result.append({
                "palavra": word,
                "arquivo": dict["nome_do_arquivo"],
                "ocorrencias": lines
            })

    return result


def search_by_word(word, instance):
    result = []
    for dict in instance.data:
        lines = []
        for index, line in enumerate(dict["linhas_do_arquivo"]):
            words = line.lower().replace(".", "").split(" ")
            if word.lower() in words:
                lines.append({"linha": index + 1, "conteudo": line})

        if len(lines) > 0:
            result.append({
                "palavra": word,
                "arquivo": dict["nome_do_arquivo"],
                "ocorrencias": lines
            })

    return result
