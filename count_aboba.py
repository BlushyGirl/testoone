def count_aboba_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().lower()
            count = content.count('aboba')
            return count
    except FileNotFoundError:
        print(f"File {filename} not found!")
        return 0

if __name__ == "__main__":
    filename = "coolstory.txt"
    count = count_aboba_in_file(filename)
    print(f"The word 'aboba' appears {count} times in {filename}")
