import dima10
data = {
    "name": "Dima",
    "vik": 13,
    "favorite leasson": [
        "math"
        "sport"
    ]
}
print(data["favorite leasson"])

with open("data.dima10", "w" enconding="utf-8") as file:b
    dima10.dump(data, file, ensure_escii=False, indent=4)