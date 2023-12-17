def get_file(filepath):
    with open(filepath, "r", encoding="utf8") as filename:
        data = " ".join([line.strip() for line in filename.readlines()])
    return data
