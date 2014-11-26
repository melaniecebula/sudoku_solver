asserts = []
bools = []
def generate_input(size = 9):
	#Whether variable at location i,j is k 
        at_most_one = []
	for i in range(size):
		for j in range(size):
			#curr_string = "row" + str(i) + "col" + str(j)
			#curr_string = create(i, j, "", True)
			curr_string = "row" + str(i) + "col" + str(j)
			tmp = []
			for k in range(size):
				string = "row" + str(i) + "col" + str(j) + "num" + str(k + 1)
				#string = create(i, j, k + 1, True)
				tmp.append(string)
				bools.append(string + " : BOOLEAN;")
			#variable at location i,j must be one of k 1-9
			#TODO:  might want to assign each var rowicolj to each of these statements:  rowicolj <=> curr_string
			#curr_string = (" OR ").join(tmp)
			#curr_string = "ASSERT(" + curr_string + ");"
			#asserts.append(curr_string)
                        at_most_one.append(tmp)
        for expr in at_most_one:
            res = "ASSERT((" +atLeastOne(expr) + ") AND (" + assertAtMostOne(expr) +"));"
            #print res
            asserts.append(res)

#TODO:  blocks now work, but adding in both row and col rules causes problems
	#for k in range(size):
#		generate_row_rules(k, size)
	
	#for k in range(size):
#		generate_col_rules(k, size)
        #generate_col_rules(0, size)


        blocks = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                blocks.append((i, j))
        for block in blocks:
            for k in range(9):
                new_generate_box_rule(block, k)
        #Custom
        #asserts.append("ASSERT(" + create(6, 0, 5, True) + ");")
        #asserts.append("ASSERT(" + create(5, 1, 9, True) + ");")
        #asserts.append("ASSERT(" + create(7, 2, 2, True) + ");")
        #asserts.append("ASSERT(" + create(2, 2, 1, True) + ");")
        #asserts.append("ASSERT(" + create(4, 2, 4, True) + ");")
        #asserts.append("ASSERT(" + create(3, 3, 5, True) + ");")
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
        #res = "(" + my_pts + "=>" +"( NOT(" + ") AND NOT(".join(nots) + ")))"
        tmp.append(res)
    tmp = " OR ".join(tmp)
    tmp = "ASSERT(" + tmp + ");"
    asserts.append(tmp)
    #res = "ASSERT(" + assertAtMostOne(tmp) +");"
    #tmp = "ASSERT((" +atLeastOne(tmp) + ") AND (" + assertAtMostOne(tmp) +"));"
    #asserts.append(tmp)



#IDEAS:
	#For each row, for each position of a number, for each number  1-9
def generate_row_rules(k, size):
	to_and = []
	for i in range(size):
		num_assert = []
		for j in range(size):
			#TODO:  problem with noteq?
			noteq = generate_noteq2(i, j, k + 1)
			noteq = ") AND NOT(".join(noteq)
			#row = create(i, j, k + 1, True) + " AND NOT(" + noteq + ")"
			row = "row" + str(i) + "col" + str(j) + "num" + str(k + 1) + " AND NOT(" + noteq + ")"
			num_assert.append("(" + row + ")")
		tmp = " OR ".join(num_assert)
		to_and.append("(" + tmp + ")")
	rows_rule = " AND ".join(to_and)
        rows_rule = "ASSERT(" + rows_rule + ");"
	asserts.append(rows_rule)
					
def generate_col_rules(k, size):
	to_and = []
	for i in range(size):
		num_assert = []
		for j in range(size):
			noteq = generate_noteq(i, j, k + 1)
			noteq = ") AND NOT(".join(noteq)
			#col = create(j, i, k + 1, True) + " AND NOT(" + noteq + ")"
			col = "row" + str(i) + "col" + str(j) + "num" + str(k + 1) + " AND NOT(" + noteq + ")"
			num_assert.append("(" + col + ")")
		tmp = " OR ".join(num_assert)
		to_and.append("(" + tmp + ")")
	cols_rule = " AND ".join(to_and)
        cols_rule = "ASSERT(" + cols_rule + ");"
	asserts.append(cols_rule)

def generate_box_rule(starti, startj, k):
    sts = []
    for i in range(starti, starti + 3):
        for j in range(startj, startj + 3):
            #TODO:  noteq_box does not work!!!
            noteq = noteq_box(starti, startj, k+1, 3, i, j)
            noteq = ") AND NOT(".join(noteq)
            st = "row" + str(i) + "col" + str(j) + "num" + str(k + 1) + " AND NOT(" + noteq + ")"
            sts.append("(" + st + ")")
    tmp = " OR ".join(sts)
    tmp = "ASSERT(" + tmp + ");"
    asserts.append(tmp)
					
def noteq_box(starti, startj, k, sz, i, j):
    res = []
    for m in range(starti, starti + sz):
        for l in range(startj, startj +sz):
            if not (m == i and l == j):
                res.append(create(l, m, k, True))
    return res
			

def generate_noteq(i, j, k, size=9):
	res = []
	for l in range(size):
		if l != j:
			res.append(create(i, l, k, True))
	return res
		
def generate_noteq2(i, j, k, size=9):
	res = []
	for l in range(size):
		if l != j:
			res.append(create(l, i, k, True))
	return res
#TODO:  if switch args here from j,i to i,j generate_col_rules will generate row_rules
def create(i, j, k, row):
	#TODO: currently always true so won't want values
	if row:
		i, j = j, i
	res = "row" + str(i) + "col" + str(j) + "num" + str(k)
	return res

#Have booleans for "unused vars in this row"  ex:  rowi: 1, 2, 3, 4, 5, 6, 7, 8 ,9
#Any given assignment sets that flag off unused_rowi_1 --> false


if __name__ == "__main__":
	generate_input()

