import sys
import re
import json
from toolz import get_in


def get_role(v):
    return get_in(["message", "author", "role"], v, "")


def get_message(v):
    return get_in(["message", "content", "parts", 0], v, "")


def format_conversation(conversation, writer=sys.stdout):
    print(f'# {conversation["title"]}\n\n\n\n', end="", file=writer)
    for role, msg in [
        (get_role(v), m)
        for v in conversation["mapping"].values()
        if (m := get_message(v)) != ""
    ]:
        print(f"## {role}", file=writer)
        print(msg, file=writer)
        print("\n\n\n", end="", file=writer)


def main():
    with open("data/conversations.json") as r:
        conversations = json.load(r)

    for conversation in conversations:
        path = f"outputs/{conversation['conversation_id']}.md"
        with open(path, "w") as w:
            format_conversation(conversation, w)


if __name__ == "__main__":
    main()
