list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    # Create an empty dictionary to store the merged data
    merged_data = {}

    # Merge the data from list_1
    for item in list_1:
        merged_data[item['id']] = item

    # Merge the data from list_2
    for item in list_2:
        merged_data[item['id']] = {**merged_data.get(item['id'], {}), **item}

    # Convert the merged data dictionary back into a list
    merged_list = [value for _, value in merged_data.items()]

    return merged_list


list_3 = merge_lists(list_1, list_2)

print(list_3)
