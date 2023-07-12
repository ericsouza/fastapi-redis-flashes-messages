flashes = [
    {
        "msg": "Sua requisição de relatório terminará em até 24h.",
        "key": "report.request",
        "values": '{"max_time": "24h"}'
    },
    {
        "msg": "Muitas palavras serao ditas sem contexto nesse universo ao tentar avisar alguém que uma flash message ocorreu.",
        "key": "teste.longo.chave.grande.muitas.palavras.doidas.mas.mesmo.assim.e.nois",
        "values": {
            "max_time": "24h",
            "chave_doida1": "doida chave 1",
            "chave_doida2": "doida chave 2",
            "chave_doida3": "doida chave 3",
            "chave_doida4": "doida chave 4",
            "chave_doida5": "doida chave 5"
        }
    },
    {
        "msg": "Muitas palavras serao ditas sem contexto nesse universo ao tentar avisar alguém que uma flash message ocorreu.",
        "key": "teste.longo.chave.grande.muitas.palavras.doidas.mas.mesmo.assim.e.nois",
        "values": {
            "max_time": "24h",
            "chave_doida1": "doida chave 1",
            "chave_doida2": "doida chave 2",
            "chave_doida3": "doida chave 3",
            "chave_doida4": "doida chave 4",
            "chave_doida5": "doida chave 5"
        }
    }
]

flashes_to_serialize = [
    {
        "msg": "Sua requisição de relatório terminará em até 24h.",
        "key": "report.request",
        "values": {
            "max_time": "24h"
        }
    },
    {
        "msg": "Muitas palavras serao ditas sem contexto nesse universo ao tentar avisar alguém que uma flash message ocorreu.",
        "key": "teste.longo.chave.grande.muitas.palavras.doidas.mas.mesmo.assim.e.nois",
        "values": {
            "max_time": "24h",
            "chave_doida1": "doida chave 1",
            "chave_doida2": "doida chave 2",
            "chave_doida3": "doida chave 3",
            "chave_doida4": "doida chave 4",
            "chave_doida5": "doida chave 5"
        }
    },
    {
        "msg": "Muitas palavras serao ditas sem contexto nesse universo ao tentar avisar alguém que uma flash message ocorreu.",
        "key": "teste.longo.chave.grande.muitas.palavras.doidas.mas.mesmo.assim.e.nois",
        "values": {
            "max_time": "24h",
            "chave_doida1": "doida chave 1",
            "chave_doida2": "doida chave 2",
            "chave_doida3": "doida chave 3",
            "chave_doida4": "doida chave 4",
            "chave_doida5": "doida chave 5"
        }
    }
]

def get_all_flashes(serialized: bool = False) -> list[dict]:
    if serialized:
        return flashes_to_serialize
    return flashes
