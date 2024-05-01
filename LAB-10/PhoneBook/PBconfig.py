from configparser import ConfigParser

def load_config(filename='phone_book.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to postgresql
    PBconfig = {}
    if parser.has_section(section):
        params = parser.items(section)
        print(params)
        for param in params:
            PBconfig[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return PBconfig

if __name__ == '__main__':
    PBconfig = load_config()
    print(PBconfig)