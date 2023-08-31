import pkg_resources


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
