def find_can_and_cannot_uninstall(package_name, dependencies, packages_required_by):
    can_uninstall = []
    cannot_uninstall = []
    for dependency in dependencies[package_name]:
        if len(packages_required_by[dependency]) > 1:
            cannot_uninstall.append(dependency)
        else:
            can_uninstall.append(dependency)
    can_uninstall.append(package_name)
    return can_uninstall, cannot_uninstall
