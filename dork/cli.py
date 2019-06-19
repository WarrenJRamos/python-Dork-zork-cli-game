# -*- coding: utf-8 -*-
from dork.command_manager import CommandManager
"""Basic CLI Dork."""

__all__ = ["main"]


def main(*args):
    """Main CLI runner for Dork
    """
    script_name = args[0] if args else '???'
    if "-h" in args or '--help' in args:
        print("usage:", script_name, "[-h]")
    else:
        print(*args)

    cm = CommandManager()
    cm.start()
    while cm.check_game_over() == False:
        cm.read_command()
        cm.execute_command()
