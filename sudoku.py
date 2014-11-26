asserts = []
bools = []
def generate_input(size = 9):
        at_most_one = []
	for i in range(size):
		for j in range(size):
			curr_string = "row" + str(i) + "col" + str(j)
			tmp = []
			for k in range(size):
				string = "row" + str(i) + "col" + str(j) + "num" + str(k + 1)
				tmp.append(string)
				bools.append(string + " : BOOLEAN;")
                        at_most_one.append(tmp)
        for expr in at_most_one:
            res = "ASSERT((" +atLeastOne(expr) + ") AND (" + assertAtMostOne(expr) +"));"
            asserts.append(res)

        blocks = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                blocks.append((i, j))
        for block in blocks:
            for k in range(9):
                new_generate_box_rule(block, k)
        #Custom
        asserts.append("ASSERT(" + create(6, 0, 5, False) + ");")
        asserts.append("ASSERT(" + create(5, 1, 9, False) + ");")
        asserts.append("ASSERT(" + create(7, 2, 2, False) + ");")
        asserts.append("ASSERT(" + create(2, 2, 1, False) + ");")
        asserts.append("ASSERT(" + create(4, 2, 4, False) + ");")
        asserts.append("ASSERT(" + create(3, 3, 5, False) + ");")
        asserts.append("ASSERT(" + create(2, 4, 2, False) + ");")
        asserts.append("ASSERT(" + create(7, 4, 1, False) + ");")
        asserts.append("ASSERT(" + create(8, 4, 4, False) + ");")
        asserts.append("ASSERT(" + create(1, 5, 3, False) + ");")
        asserts.append("ASSERT(" + create(3, 5, 7, False) + ");")
        asserts.append("ASSERT(" + create(4, 6, 1, False) + ");")
        asserts.append("ASSERT(" + create(1, 7, 8, False) + ");")
        asserts.append("ASSERT(" + create(6, 7, 7, False) + ");")
        asserts.append("ASSERT(" + create(1, 8, 5, False) + ");")
        asserts.append("ASSERT(" + create(6, 8, 3, False) + ");")
        asserts.append("ASSERT(" + create(8, 8, 9, False) + ");")

        for col in range(size):
            for k in range(9):
                new_generate_col_rule(col, k, size)

        for row in range(size):
            for k in range(9):
                new_generate_row_rule(row, k, size)

        for bool in bools:
            print bool
        for ast in asserts:
            print ast
def assertAtMostOne(lst):
    res = "NOT(" + lst[0] + ") OR NOT(" + lst[1] +")"
    for i in range(1, len(lst)):
        for j in range(1, len(lst)):
            if i != j:
                res = res + " AND (" + "NOT(" + lst[i] + ") OR NOT(" + lst[j] + "))"
    return res

def atLeastOne(lst):
    res = lst[0]
    for i in range(1, len(lst)):
        res = res + " OR " + lst[i]
    return res

def new_generate_col_rule(col_num, k, size):
    res = []
    for i in range(size):
        tmp = "row" + str(i) + "col" + str(col_num ) + "num" + str(k + 1)
        res.append(tmp)
    res = " OR ".join(res)
    asserts.append("ASSERT(" + res + ");")

def new_generate_row_rule(row_num, k, size):
    res = []
    for i in range(size):
        tmp = "row" + str(row_num) + "col" + str(i) + "num" + str(k + 1)
        res.append(tmp)
    res = " OR ".join(res)
    asserts.append("ASSERT(" + res + ");")

def new_generate_box_rule(block, k):
    r, c = block
    pts = []
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            pts.append((i, j))
    tmp = []
    for pt in pts:
        nots = []
        my_i, my_j = pt
        my_pts = "row" + str(my_i) + "col" + str(my_j) + "num" + str(k + 1)
        for x in pts:
            x_i, x_j = x
            if x != pt:
                nots.append("row" + str(x_i) + "col" + str(x_j) + "num" + str(k + 1))
        res = "(" + my_pts + " AND(NOT(" + ")) AND(NOT(".join(nots) + ")))"
        tmp.append(res)
    tmp = " OR ".join(tmp)
    tmp = "ASSERT(" + tmp + ");"
    asserts.append(tmp)



def create(i, j, k, row):
	if row:
		i, j = j, i
	res = "row" + str(i) + "col" + str(j) + "num" + str(k)
	return res
if __name__ == "__main__":
	generate_input()

