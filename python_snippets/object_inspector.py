import inspect

from pprint import pformat
from typing import Any


def format_inspection(name, detail) -> str:
    formatted_text = f"{name}:\n"
    if isinstance(detail, (list, dict)):
        formatted_text += pformat(detail, indent=4, compact=True, width=100)
    else:
        formatted_text += str(detail)
    return formatted_text + "\n\n"


def inspect_obj(obj) -> dict[str, Any]:
    return {
        "Members": inspect.getmembers(obj),
        "Static Members": inspect.getmembers_static(obj),
        "Module": inspect.getmodule(obj),
        "Docstring": inspect.getdoc(obj),
        "Signature": inspect.signature(type(obj)),
        "Signature Parameters": inspect.signature(type(obj)).parameters,
        "Parameter Kind": {
            param: param.kind
            for param in inspect.signature(type(obj)).parameters.values()
        },
        "Class Tree": inspect.getclasstree([type(obj)]),
        "Annotations": inspect.get_annotations(type(obj)),
    }


def inspect_and_print(obj) -> None:
    for name, detail in inspect_obj(obj).items():
        print(format_inspection(name, detail))
