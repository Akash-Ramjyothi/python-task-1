# Python Task 1

Complete the function in `main.py`, by merging the information from list_1 and list_2
to create a new list, which has all the information about each student from
both lists in one single dict.

- Both lists are unsorted
- Both lists can have missing values (for ex list_2 has missing id=2)

# Submission Guidelines

- You need to submit the task, completed by `11:59PM IST - 21st April, 2023`.
- You need to push the updated code in a Github repository in your own account and submit the link to the repository in [this form](https://forms.gle/6i5wrfDwr661JXY79).

# Output of completed Program:
```json
[
   {
      "id":"1",
      "name":"Shrey",
      "age":25,
      "marks":100
   },
   {
      "id":"3",
      "age":10,
      "name":"Hello",
      "marks":90,
      "roll_no":11,
      "extra_info":{
         "hello":"world"
      }
   },
   {
      "id":"2",
      "name":"World",
      "age":24
   }
]
```

## `merge_list` function:
```py
def merge_lists(list_1, list_2) -> list:
    merged_data = {}

    for item in list_1:
        merged_data[item['id']] = item

    for item in list_2:
        merged_data[item['id']] = {**merged_data.get(item['id'], {}), **item}

    merged_list = [value for _, value in merged_data.items()]

    return merged_list
```
