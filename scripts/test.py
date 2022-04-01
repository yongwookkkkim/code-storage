file = open('scripts/database.txt', 'a')
for i in range(10):
    file.write("\nhi")
x=file.read()
print(x)
file.close()