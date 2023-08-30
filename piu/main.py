import os

import click
import pkg_resources
from colorama import Fore, Style, deinit, init

init()


def find_requiredby():
    packages_requiredby = {}
    for package in pkg_resources.working_set:
        packages_requiredby[package.project_name] = {
            pkg.project_name
            for pkg in pkg_resources.working_set
            if package.project_name in {req.project_name for req in pkg.requires()}
        }
    return packages_requiredby


def find_dependencies():
    dependencies = {}
    for pkg in pkg_resources.working_set:
        reqs = {req.project_name for req in pkg.requires()}
        dependencies[pkg.project_name] = reqs
    return dependencies


def find_flat_dependencies():
    flat_dependencies = set()
    for pkg in pkg_resources.working_set:
        reqs = {req.project_name for req in pkg.requires()}
        flat_dependencies.update(reqs)
    return flat_dependencies


def find_can_and_cannot_uninstall(package_name, dependencies, packages_requiredby):
    can_uninstall = []
    cannot_uninstall = []
    for n in dependencies[package_name]:
        if len(packages_requiredby[n]) > 1:
            cannot_uninstall.append(n)
        else:
            can_uninstall.append(n)
    can_uninstall.append(package_name)
    return can_uninstall, cannot_uninstall


def join_handler(iterable, seperator):
    if iterable == []:
        return "<Nothing>"
    else:
        return seperator.join(iterable)


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
