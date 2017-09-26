Name: Zhipeng Xie😀
UOID: 951586566
***

# Q1\_Find\_the\_Optimal\_parenthesization

$$
(M_{5\times10}\times M_{10\times3})\times (M_{3\times12}\times M_{12\times5})\times (M_{5\times50}\times M_{50\times6})
$$

# Q2\_DP\_EMP\_Maximal\_killing

## (a) describe the subproblem:

	To guess when is the best time to enable the EMP, and return the maximal killing number.
	
Suppose DP(i) means the maximal killing number at the ith sec.
DP(0) = 0, which means at the begining we cannot kill any thing.
	## (b) give a recurrence for the subproblem:
DP(i) = max( DP(i - t) + min(X[i], F[t]) for t in range(1, i + 1) )

The EMP could have been charged for at least 1 sec to i secs.
We need to try every possible time that the EMP has been charged for.

If the EMP had been charged for t secs, during these secs, EMP couldn't kill any thing.
So, DP(i) = DP(i - t) + the killing number at the ith sec.
## (c) provide pseudo-code showing how a table for the subproblems is filled:
```
We need to slightly modify the X and F, adding the 0th sec info.

So now, 
X = [0, 1, 10, 10, 1], which means at the very begining, no robot is there; 
F = [0, 1, 2, 4, 8], which means when EMP had been charged for 0 sec, it cannot kill any robot.

DP_hash_table = {sec:None for sec in range( len(X) )}, which is used to keep tracking the maximal killing number
DP_hash_table[0] = 0 # basic case, at the begining we cannot kill anything.

def DP(i):
    if DP_hash_table[i] != None:
        return DP_hash_table[i]

    global X
    global F

    DP_hash_table[i] = max(DP(i - t) + min(X[i], F[t]) for t in range(1, i + 1))

    return DP_hash_table[i]
   
print( DP(4) )
print(DP_hash_table)
# Result: 
#5
#{0: 0, 1: 1, 2: 2, 3: 4, 4: 5}
```
## (d) give the time and space requirements of your method:
Number of subproblem = n^2
Time consuming per subproblem = 1
Total time consuming = θ(n^2)

Space consuming = n, for the hash table.

# Q3\_DP\_Another\_Parenthesization
##(a) describe the subproblem:

$$P(i,j,t), where 1 ≤ i ≤ n, 0 ≤ j < n, and\ t ∈ \{a,b,c\}.$$
$$ 
P(i,j,t) will\ return\ true\ if\ it\ is\ possible\ to\ parenthesize\ S_{i} S_{i+1} · · · S_{i+j}\ to \ equal\ t$$
##(b) give a recurrence for the subproblem:
$$P(i,j,t) = P(i, k, t1')\ and\ P(k, j, t2')\ for\ every\ t1'\times\ t2'=t\ for\ k\ in\ range(1,j)$$
##(c) provide pseudo-code showing how a table for the subproblems is filled:
```
Suppose we use DP_table to memoize the known result.
Suppose we have input string S, in this case, S = 'bbbba'

S = 'bbbba'
DP_table.init() 
'''
At first DP_table's result is like: 
{
('aa', 'b'): True, ('ab', 'b'): True, ('ac', 'a'): True, # So, aa == b, ab == b and so on...
('ba', 'c'): True, ('bb', 'b'): True, ('bc', 'a'): True,
('ca', 'a'): True, ('cb', 'c'): True, ('cc', 'c'): True, 
('a', 'a'): True, ('b', 'b'): True, ('c', 'c'): True
}
Just copying the table into the memo.
'''

def DP(i, j, t):
	if DP_table.get( (S[i:j], t) ):
		return that result
	
	temp_result = False
	for every t1', t2' in [a,b,c] and t1' * t2' == t:
		for k in range(1, len(S)):
			if not temp_result:
				current = DP(S[:k], t1') and DP(S[k:], t2')
			else:
				break
	
	DP_table[(S[i:j], t)] = temp_result
	
	return DP_table[(S[i:j], t)]
	
'''
Sample:

DP(0, 4, 'c')

At the end, the DP_table is like:
{
('aa', 'b'): True, ('ab', 'b'): True, ('ac', 'a'): True, 
('ba', 'c'): True, ('bb', 'b'): True, ('bc', 'a'): True, 
('ca', 'a'): True, ('cb', 'c'): True, ('cc', 'c'): True, 
('a', 'a'): True, ('b', 'b'): True, ('c', 'c'): True, 
('b', 'a'): False, ('b', 'c'): False, ('bb', 'a'): False, ('bb', 'c'): False, ('bbb', 'a'): False, ('a', 'c'): False, ('ba', 'a'): False, 
('bba', 'c'): True, ('bbba', 'a'): True, ('bbbba', 'c'): True
}
'''
```
##(d) give the time and space requirements of your method:
Number of subproblem: ( n^2 * How\_many\_combination\_satisfied\_t1' * t2' == t ) <= n^3
Time consuming per subproblem: 1
Total: o(n^3)
Space: θ(n^3)
# Q4\_Code\_for\_iterative\_DP\_CoinProblem

```
coins = [1, 3, 7, 10]

c_dict = {coin:[1, [coin]] for coin in coins}
# Initialize a hashtable to keep tracking 
# minimal amount of coins used for certain amount of money.
# At first, c_dict = { 1:[1, [1]], 3:[1, [3]], 7:[1, [7]], 10:[1, [10]] }
# The format is c_dict[ amount_of_money ] = [#num_of_minimal_coin, [ every coin that are using ]]

c_dict[0] = [0, []]

def DPI(T):
	'''
	To bottom-up the solution
	we need to know how to minimalize
	the coin-using of every amount that
	smaller than T.
	
	Sample using: 
	print(DPI(12))
	[3, [10, 1, 1]]
	# This means to change 12, we need at least 3 coins, one 10 cent and two 1 cent.
	'''
    if c_dict.get(T):
        return c_dict[T]

    if T < 0:
        return None

    global coins
    for i in range(1, T + 1):
    
        if not c_dict.get(i):
        
            min_coin_num = 1000
            using_coins = []
            
            # The following is like c_dict[i] = 1 + min(c_dict[i - coin] for coin in coins)
			# But we also need to keep tracking which coins have been used, so we have to write more than that.  
            for coin in coins:
            
                if coin <= i:      
                    if c_dict[i - coin][0] < min_coin_num:
                    
                        min_coin_num = c_dict[i - coin][0]
                        using_coins = c_dict[i - coin][1] + [coin]  
            c_dict[i] = [min_coin_num + 1, using_coins]

    return c_dict[T]
```

***

Thanks! 
This is the most pseudo-code I can do now. I've tried to make it as plain as possible