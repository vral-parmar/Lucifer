import argparse
import os
import sys

from .LuciferShell import Shell
from .LuciferManager import LuciferManager


class VAAETParser(argparse.ArgumentParser):
    def __init__(self, lucifer_manager: LuciferManager, *args, **kwargs):
        super().__init__(args, kwargs)
        self.luciferManager = lucifer_manager

    def error_usage(self, message: str):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(os.EX_USAGE)

    def check_args(self):
        if len(sys.argv) == 1:
            self.error_usage("No Arguments")

    def check_gui(self):
        if self.args.gui:
            self.luciferManager.gui = True
            print("Show GUI")
        else:
            self.luciferManager.colorama.init(autoreset=True)
            print(self.luciferManager.termcolor.colored("Lucifer Prototype 1", "red", attrs=["bold", "underline"]))
            self.luciferManager.main_shell = Shell(self.luciferManager.next_shell_id, self.luciferManager)
            self.luciferManager.next_shell_id += 1
            self.luciferManager.main_shell.spawn()