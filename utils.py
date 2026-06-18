def save_list(path, items):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(items))