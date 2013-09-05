from Solver import Klotski 

puzzle=[ 9,9,9,9
			,9,9,9,9
			,1,2,2,1
			,1,2,2,1
			,1,3,3,1
			,1,4,4,1
			,4,0,0,4
			,9,9,9,9
			,9,9,9,9]

k= Klotski()
k.solve(puzzle)