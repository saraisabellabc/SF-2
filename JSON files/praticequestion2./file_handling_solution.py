def count_error_lines():
    file = open("data.txt", "r")
    count = 0
    lines = file.readlines()

    for line in lines:
        if "error" in line.lower():
            count += 1

    file.close()
    return count

print(count_error_lines())  # Should print 2 based on the sample content
