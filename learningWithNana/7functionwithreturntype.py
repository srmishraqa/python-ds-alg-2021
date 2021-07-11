"""
We can use return keyword to return something out of the function
"""


def calculate_sum():
    end_num = int(input("Enter the number,for which you want a sum from that number till 1 \n"))
    return int((end_num * (end_num + 1)) / 2)


output_sum = calculate_sum()
print(f"output sum is equal to {output_sum}")
