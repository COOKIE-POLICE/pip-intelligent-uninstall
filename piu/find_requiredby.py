import pkg_resources


def find_requiredby():
    packages_requiredby = {}
    for package in pkg_resources.working_set:
        packages_requiredby[package.project_name] = {
            pkg.project_name
            for pkg in pkg_resources.working_set
            if package.project_name in {req.project_name for req in pkg.requires()}
        }
    return packages_requiredby
