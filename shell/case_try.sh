#!/bin/bash

# >>> sh case_try.sh Zippo
# "Hi Zippo"
# >>> sh case_try.sh
# "Fuck off!!"

# case: matching the string

#wild card:
#? -> any one char
#* -> any length string, including the space
#[abcd] -> a or b or c or d
#
case $1 in
    ([zZ]ippo | [jJ]erry)
    echo "Hi $1"
    ;;
    (*)
    echo "Fuck off!!"
    ;;
esac