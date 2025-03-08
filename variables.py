def get_variables():
    light_variables_dict = {}
    dark_variables_dict = {}
    f = open("./variables.txt")
    content = f.read()
    variables = content.split("\n")
    light_theme_variables = variables[0 : variables.index(':root[data-theme="dark"] {')]
    dark_theme_variables = variables[variables.index(':root[data-theme="dark"] {') :]
    for line in light_theme_variables:
        if line.startswith(":root") or line == "}" or line == "{" or line == "":
            continue
        name, hex = line.split(":")
        light_variables_dict[name.replace(" ", "").lstrip("-")] = hex.replace(
            ";", ""
        ).replace("#", "")
    for line in dark_theme_variables:
        if line.startswith(":root") or line == "}" or line == "{" or line == "":
            continue
        name, hex = line.split(":")
        dark_variables_dict[name.replace(" ", "").lstrip("-")] = hex.replace(
            ";", ""
        ).replace("#", "")
    return [light_variables_dict, dark_variables_dict]
