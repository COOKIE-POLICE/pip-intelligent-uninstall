import os

import click
from colorama import Fore, Style, deinit, init

from .find_can_and_cannot_uninstall import *
from .find_dependencies import *
from .find_requiredby import *
from .join_handler import *

init()

packages_requiredby = find_requiredby()
dependencies = find_dependencies()
flat_dependencies = find_flat_dependencies()


@click.group()
def cli():
    pass


@cli.command
@click.argument("package_name", type=str)
def uninstall(package_name):
    if package_name in flat_dependencies:
        click.echo(
            f"{Fore.RED}You cannot uninstall {package_name} as it is required by {join_handler(packages_requiredby[package_name], ', ')}{Style.RESET_ALL}"
        )
    else:
        can_uninstall, cannot_uninstall = find_can_and_cannot_uninstall(
            package_name, dependencies, packages_requiredby
        )
        click.echo(
            f"{Fore.RED}You cannot uninstall: {join_handler(cannot_uninstall, ', ')} (Other packages depend on them){Style.RESET_ALL}\n"
            f"{Fore.GREEN}You can uninstall: {join_handler(can_uninstall, ', ')} (Other packages do not depend on them){Style.RESET_ALL}\n"
        )
        if click.confirm(
            f"{Fore.BLUE}Do you want to proceed to uninstall the packages: {join_handler(can_uninstall, ', ')}?{Style.RESET_ALL}"
        ):
            pip_command = f"pip uninstall {join_handler(can_uninstall, ' ')} -y"
            click.echo(f"Running: {pip_command}")
            os.system(pip_command)


deinit()
