import yaml # importing yaml library

def yaml_loader(file_path):
    '''To load file to variable'''
    with open(file_path, "r") as f:
        data = yaml.load(f)
    return data

def yaml_dump(data,file_path):
    '''Dump data to file'''
    with open(file_path, "w") as f:
        yaml.dump(data, f)

if __name__ == "__main__":

    # reading from file
    file_path = "basic.yaml"

    data = yaml_loader(file_path)

    items = data.get("person")

    print(data)

    for k, v in items.items():
        print(k)

    # writing to file
    write_file_path = "basic_write.yaml"
    write_data = {"items":
                      {
                          "buses": 10,
                          "cars": 20
                      }}

    # yaml_dump(write_data, write_file_path)