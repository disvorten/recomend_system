import json

with open("books.json", "r") as read_it:
    data = json.load(read_it)
new_file = json.JSONEncoder(ensure_ascii=True).encode(data)
new_file = json.JSONEncoder(ensure_ascii=True).default(new_file)
print(new_file)
with open("books_new.json", "w") as read_it:
    json.dump(new_file, read_it)

