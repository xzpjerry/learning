#!/bin/bash

# To assignment a value to a variable,
# don't add spaces
count=0
'''
-lt (<): less than

-gt (>): greater than

-le (<=): less than or equal to

-ge (>=): greater than or equal to

-eq (==): equal To

-ne (!=): negative equal To
'''
while [[ $count -le 100 ]]; do
    echo $count
    count=$[ $count + 1 ]
done