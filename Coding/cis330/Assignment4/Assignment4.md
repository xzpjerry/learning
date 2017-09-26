Name: Zhipeng Xie😀

Uo ID: 951586566

***

# Q1\_F-W\_algorithm\_in\_Matrix

$$
W0=\left(\begin{array}{cc}
0 & \infty & \infty & \infty & -1 & \infty \\
1 & 0 & \infty & 2 & \infty & \infty\\
\infty & 2 & 0 & \infty & \infty & -8\\
-4 & \infty & \infty & 0 & 3 & \infty\\
\infty & 7 & \infty & \infty & 0 & \infty\\
\infty & 5 & 10 & \infty & \infty & 0\\
\end{array}\right)
$$

$$
W1=\left(\begin{array}{cc}
0 & \infty & \infty & \infty & -1 & \infty \\
1 & 0 & \infty & 2 & 0 & \infty\\
\infty & 2 & 0 & \infty & \infty & -8\\
-4 & \infty & \infty & 0 & -5 & \infty\\
\infty & 7 & \infty & \infty & 0 & \infty\\
\infty & 5 & 10 & \infty & \infty & 0\\
\end{array}\right)
$$

$$
W2=\left(\begin{array}{cc}
0 & \infty & \infty & \infty & -1 & \infty \\
1 & 0 & \infty & 2 & 0 & \infty\\
3 & 2 & 0 & 4 & 2 & -8\\
-4 & \infty & \infty & 0 & -5 & \infty\\
8 & 7 & \infty & 9 & 0 & \infty\\
6 & 5 & 10 & 7 & 5 & 0\\
\end{array}\right)
$$

$$
W3=\left(\begin{array}{cc}
0 & \infty & \infty & \infty & -1 & \infty \\
1 & 0 & \infty & 2 & 0 & \infty\\
3 & 2 & 0 & 4 & 2 & -8\\
-4 & \infty & \infty & 0 & -5 & \infty\\
8 & 7 & \infty & 9 & 0 & \infty\\
6 & 5 & 10 & 7 & 5 & 0\\
\end{array}\right)
$$

$$
W4=\left(\begin{array}{cc}
0 & \infty & \infty & \infty & -1 & \infty \\
-2 & 0 & \infty & 2 & -3 & \infty\\
0 & 2 & 0 & 4 & -1 & -8\\
-4 & \infty & \infty & 0 & -5 & \infty\\
5 & 7 & \infty & 9 & 0 & \infty\\
3 & 5 & 10 & 7 & 2 & 0\\
\end{array}\right)
$$

$$
W5=\left(\begin{array}{cc}
0 & 6 & \infty & 8 & -1 & \infty \\
-2 & 0 & \infty & 2 & -3 & \infty\\
0 & 2 & 0 & 4 & -1 & -8\\
-4 & 2 & \infty & 0 & -5 & \infty\\
5 & 7 & \infty & 9 & 0 & \infty\\
3 & 5 & 10 & 7 & 2 & 0\\
\end{array}\right)
$$

$$
W6=\left(\begin{array}{cc}
0 & 6 & \infty & 8 & -1 & \infty \\
-2 & 0 & \infty & 2 & -3 & \infty\\
-5 & -3 & 0 & -1 & -6 & -8\\
-4 & 2 & \infty & 0 & -5 & \infty\\
5 & 7 & \infty & 9 & 0 & \infty\\
3 & 5 & 10 & 7 & 2 & 0\\
\end{array}\right)
$$


***

# Q2\_Find\_the\_max\_weight

Suppose the graph(V,E) given is a minimal spanning tree DAG with a source and a sink.

Suppose M(v) means the maximal weight of the edges constituting the path from source vertex to v.

Suppose W(s,v) means the weights of edge from s to v.


**Subproblem structure of the Q2:**

```
M(s, v) for every v in V
M(s, v) return the maximal weight of a edge from s to v
```

**Recurrence relation:**

```
Basic case: M(s, s) = 0
M(s, v) = max( M(s, u), W(u, v) ) for every (u,v) in E 
```


***

# Q3\_Find\_the\_min\_total\_weight

Suppose it's a graph(V,E):

```
V = [a0, a1, a2, ... , an], denoting the hotels;
E = [(a0,a1), (a1,a2), ... (an-1, an)], denoting the roads between hotels
```


Suppose the Penalty computing function:

$$P(ai, aj) = [200 - (a_j - a_i)]^2$$

- This means the penalty driving from hotel ai to aj.

**Subproblem structure:**

```
S(s, ai): The least penalty from s to ai hotel 
```

**Recurrence relation:**

```
Basic case: S(s,s) = 0
S(s,ai) = min ( S(s, aj) + P(aj, ai) for every hotel aj before hotel ai )
```

***

# Q4\_Find\_the\_min\_cost(DP)

**Subproblem Structure && their relation**:

```
Suppose m(i) means the total minimal cost of the ith day.
m(i) = min( m(i - 1) + the_same_city_cost[i], m(i - 1) + opposite_city_cost[i] + M )
```

**Based on this idea, I've implemented the following python3 code:**

```
M = 10
A = [1, 3, 20, 30]
B = [50, 20, 2, 4]
current_min_dict = {day: None for day in range(len(A) + 1)}
current_min_dict[0] = (None, 0)


def min_cost_dp(day):

    if current_min_dict[day]:
        return current_min_dict[day]

    # last_day_info structure: (last_day_city, last_day_min_cost)
    last_day_info = min_cost_dp(day - 1)

    if last_day_info[0] == None:
    	'''
    	Basic case, today is the first day
    	'''
    	
        first_day_min_wei = min(A[0], B[0])
        nex_day_should_at = A if first_day_min_wei == A[0] else B
        current_min_dict[day] = (nex_day_should_at, first_day_min_wei)
        
    else:

        opposite_city = A if last_day_info[0] == B else B

        today_min_wei = min(last_day_info[
                            1] + last_day_info[0][day - 1], last_day_info[1] + opposite_city[day - 1] + M)

        nex_day_should_at = last_day_info[0] if today_min_wei == last_day_info[
            1] + last_day_info[0][day - 1] else opposite_city

        current_min_dict[day] = (nex_day_should_at, today_min_wei)

    return current_min_dict[day]

print(min_cost_dp(len(A)))
print(current_min_dict)
```