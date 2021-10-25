row = []
sumofrow = 0
count = 0
known = 0
remaining = 0
crosses = 0
print("Insert the row size")
grid = int(input())

print("Insert each of the numbers in the row, exit by hitting return")
while True:
    row.append(input())
    print(row)
    if row[-1] == "":
        row = row[:-1]
        break

for i in row:
    sumofrow += int(i)

count = len(row)
known = sumofrow + count - 1
crosses = grid - known
if known > grid:
    print("Either the grid, or the row numbers are wrong")
    print("Grid: "+str(grid))
    print("Row: "+str(row))
    exit()

if crosses == 1:
    print("There is "+str(crosses)+" unknown square. You can safely place parts of the smaller rows that are higher than "+str(crosses))
elif crosses == 0:
    print("There are no unknown squares. You can safely place the whole row")
else:
    print("There are "+str(crosses)+" unknown squares. You can safely place parts of the smaller rows that are higher than "+str(crosses))