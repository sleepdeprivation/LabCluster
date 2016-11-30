import math

#code we'll be generating
s = """
addpath(genpath('.'));
%%A = [1,2,3;4,5,6;7,8,9];

'completed addpath'

A=checkN(%d, %d, %d, %d);

'completed checkn'

save('magicFile%d', 'A');


'completed outfile'

"""

#params controlling how many files we'll be generating
L = 5;
n = 20;
full = L**(L) - 1;
numProcesses = 80.0;
print full;
interval = int(math.floor( full / numProcesses));
print interval;

#generate
for i in range(0, int(numProcesses)):
	with open(str(i), 'w') as file:
		if(i != int(numProcesses - 1)):
			tup = (L, n, i*interval, (i+1)*interval - 1, i)
		else:
			tup = (L, n, i*interval, full+10, i)
		print tup;
		file.write(s%tup);
