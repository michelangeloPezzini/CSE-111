def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"Original: {fruit_list}")
    fruit_list.reverse()
    print(f"Reverse: {fruit_list}")
    fruit_list.append("orange")
    print(f"Append: {fruit_list}")
    fruit_list.pop()
    print(f"Pop: {fruit_list}")
    fruit_list.sort()
    print(f"Sort: {fruit_list}")
    fruit_list.clear()
    print("Clear:")

if  __name__ == ("__main__"):
    main()