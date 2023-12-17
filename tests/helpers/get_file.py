def get_file(filepath):
    with open(filepath, 'r', encoding='utf8') as filename:
        data = " ".join([l.strip() for l in filename.readlines()])
    return data
