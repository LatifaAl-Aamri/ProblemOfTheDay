#problem of the day
"""
find the shortest path to arravie the spider into fly
if the spider in H3= 2 and fly in E2 = 0
Center: A0
input:
spider Vs Fly("H3", "E2")
spider Vs Fly("A4", "B2")
spider Vs Fly("A4", "C2")
Output:
"H3-H2-H1-A0-E1-E2"
"A4-A3-A2-B2"
A4-A3-A2-B2-C2"
"""
def spider_vs_fly(spider, fly):
    rows = 'ABCDEFGH'
    cols = '01234'
    
    # Convert cell positions to row and column indices
    spider_row, spider_col = rows.index(spider[0]), cols.index(spider[1])
    fly_row, fly_col = rows.index(fly[0]), cols.index(fly[1])
    
    # Generate the path
    path = []
    while spider_row != fly_row or spider_col != fly_col:
        if spider_row > fly_row:
            spider_row -= 1
            path.append(rows[spider_row] + cols[spider_col])
        elif spider_row < fly_row:
            spider_row += 1
            path.append(rows[spider_row] + cols[spider_col])
        if spider_col > fly_col:
            spider_col -= 1
            path.append(rows[spider_row] + cols[spider_col])
        elif spider_col < fly_col:
            spider_col += 1
            path.append(rows[spider_row] + cols[spider_col])
    
    return '-'.join(path)

# Test cases
print(spider_vs_fly("H3", "E2"))  # Output: "H3-H2-H1-A0-E1-E2"
print(spider_vs_fly("A4", "B2"))  # Output: "A4-A3-A2-B2"
print(spider_vs_fly("A4", "C2"))  # Output: "A4-A3-A2-B2-C2"
