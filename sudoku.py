#Usage:  python sudoku.py > test.in
#Pass test.in to a SAT solver
#Adjust Custom section with given tiles #TODO method for handling custom tiles given list of triples
asserts = []
bools = []
def generate_input(size = 9):
        exactly_one = []
	for i in range(size):
		for j in range(size):
			curr_string = "row" + str(i) + "col" + str(j)
			tmp = []
			for k in range(size):
                                string = create(i, j, k+1)
				tmp.append(string)
				bools.append(string + " : BOOLEAN;")
                        exactly_one.append(tmp)
        #Exactly one value per square
        for expr in exactly_one:
            res = "ASSERT((" +atLeastOne(expr) + ") AND (" + assertAtMostOne(expr) +"));"
            asserts.append(res)

        #3x3 blocks
        blocks = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                blocks.append((i, j))
        for block in blocks:
            for k in range(9):
                generate_box_rule(block, k)
        #Custom (given row, col, k values)
        asserts.append("ASSERT(" + create(6, 0, 5) + ");")
        asserts.append("ASSERT(" + create(5, 1, 9) + ");")
        asserts.append("ASSERT(" + create(7, 2, 2) + ");")
        asserts.append("ASSERT(" + create(2, 2, 1) + ");")
        asserts.append("ASSERT(" + create(4, 2, 4) + ");")
        asserts.append("ASSERT(" + create(3, 3, 5) + ");")
        asserts.append("ASSERT(" + create(2, 4, 2) + ");")
        asserts.append("ASSERT(" + create(7, 4, 1) + ");")
        asserts.append("ASSERT(" + create(8, 4, 4) + ");")
        asserts.append("ASSERT(" + create(1, 5, 3) + ");")
        asserts.append("ASSERT(" + create(3, 5, 7) + ");")
        asserts.append("ASSERT(" + create(4, 6, 1) + ");")
        asserts.append("ASSERT(" + create(1, 7, 8) + ");")
        asserts.append("ASSERT(" + create(6, 7, 7) + ");")
        asserts.append("ASSERT(" + create(1, 8, 5) + ");")
        asserts.append("ASSERT(" + create(6, 8, 3) + ");")
        asserts.append("ASSERT(" + create(8, 8, 9) + ");")

        #cols rules
        for col in range(size):
            for k in range(9):
                generate_col_rule(col, k, size)

        #rows rules
        for row in range(size):
            for k in range(9):
                generate_row_rule(row, k, size)

        #print to file
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

def generate_col_rule(col_num, k, size):
    res = []
    for i in range(size):
        tmp = create(i, col_num, k+1)
        res.append(tmp)
    res = " OR ".join(res)
    asserts.append("ASSERT(" + res + ");")

def generate_row_rule(row_num, k, size):
    res = []
    for i in range(size):
        tmp = create(row_num, i, k+1)
        res.append(tmp)
    res = " OR ".join(res)
    asserts.append("ASSERT(" + res + ");")

def generate_box_rule(block, k):
    r, c = block
    pts = []
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            pts.append((i, j))
    tmp = []
    for pt in pts:
        nots = []
        my_i, my_j = pt
        my_pts = create(my_i, my_j, k+1)
        for x in pts:
            x_i, x_j = x
            if x != pt:
                to_append = create(x_i, x_j, k+1)
                nots.append(to_append)
        res = "(" + my_pts + " AND(NOT(" + ")) AND(NOT(".join(nots) + ")))"
        tmp.append(res)
    tmp = " OR ".join(tmp)
    tmp = "ASSERT(" + tmp + ");"
    asserts.append(tmp)

def create(i, j, k):
	res = "row" + str(i) + "col" + str(j) + "num" + str(k)
	return res
if __name__ == "__main__":
	generate_input()

