# [] is a built-in function, using it needs to add some spaces
# [ <command> ] equals to "test <command>""

# "&> /dev/null" means run the command without showing the any result 
if ls -l &> /dev/null
    then
    echo "Hi"
else
    echo "WTF"
fi