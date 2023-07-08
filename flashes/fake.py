flashes = [
    {
        "msg": "Sua requisição de relatório terminará em até 24h.",
        "key": "report.request",
        "values": '{"max_time": "24h"}'
    },
    {
        "msg": "Sua requisição de relatório terminará em até 24h.",
        "key": "report.request",
        "values": '{"max_time": "24h"}'
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
        "msg": "Sua requisição de relatório terminará em até 24h.",
        "key": "report.request",
        "values": {
            "max_time": "24h"
        }
    }
]

def get_all_flashes(serialized: bool = False) -> list[dict]:
    if serialized:
        return flashes_to_serialize
    return flashes
