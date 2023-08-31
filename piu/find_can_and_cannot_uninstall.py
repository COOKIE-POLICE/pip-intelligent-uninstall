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
