asserts = []
def generate_input(size = 9):
	#Whether variable at location i,j is k 
	vars = []
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
				vars.append(string + " : BOOLEAN;")
			#variable at location i,j must be one of k 1-9
			#TODO:  might want to assign each var rowicolj to each of these statements:  rowicolj <=> curr_string
			curr_string = (" OR ").join(tmp)
			curr_string = "ASSERT(" + curr_string + ");"
			asserts.append(curr_string)
	#print asserts
	for k in range(size):
		generate_row_rules(k, size)
	
	for k in range(size):
		generate_col_rules(k, size)
#IDEAS:
	#For each row, for each position of a number, for each number  1-9
def generate_row_rules(k, size):
	to_and = []
	for i in range(size):
		num_assert = []
		for j in range(size):
			#TODO:  problem with noteq?
			noteq = generate_noteq2(i, j, k + 1)
			#print "row" + str(i) + "col" + str(j) + "num" + str(k + 1)
			#print noteq
			noteq = ") AND NOT(".join(noteq)
			#row = create(i, j, k + 1, True) + " AND NOT(" + noteq + ")"
			row = "row" + str(i) + "col" + str(j) + "num" + str(k + 1) + " AND NOT(" + noteq + ")"
			#print i, j, k
			#print row
			num_assert.append("(" + row + ")")
		tmp = " OR ".join(num_assert)
		to_and.append("(" + tmp + ")")
	rows_rule = " AND ".join(to_and)
	#print rows_rule
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
	#print cols_rule
	asserts.append(cols_rule)

def generate_box_rule():
					
			

#(row0_col1_num1 AND NOT(row0_col2_num1) AND NOT (row_0_col3_num1) OR (NOT(row0_col1_num1) AND row0_col2_num1 AND NOT(...)

def generate_noteq(i, j, k, size=9):
	res = []
	for l in range(size):
		if l != j:
			res.append(create(i, l, k, True))
	return res
		
#8, 0 --? should all be in row 8 but col != 0
#row8col0num9
#['row1col8num9', 'row2col8num9', 'row3col8num9', 'row4col8num9', 'row5col8num9', 'row6col8num9', 'row7col8num9', 'row8col8num9']
#should be row8col1
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
	#print res
	return res

#Have booleans for "unused vars in this row"  ex:  rowi: 1, 2, 3, 4, 5, 6, 7, 8 ,9
#Any given assignment sets that flag off unused_rowi_1 --> false


if __name__ == "__main__":
	generate_input()
