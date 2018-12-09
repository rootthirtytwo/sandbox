import yaml # importing yaml library

def yaml_loader(file_path):
    '''To load file to variable'''
    with open(file_path, "r") as f:
        data = yaml.load(f)
    return data

def yaml_dump(file_path, data):
    '''Dump data to file'''
    with open(file_path, "w") as f:
        yaml.dump(data, f)

if __name__ == "__main__":
    file_path = "basic.yaml"

    data = yaml_loader(file_path)

    items = data.get("items")

    for k, v in items.items():
        print(k)
