#！ /bin/bash
here="`dirname \"$0\"`"
echo "cd-ing to $here"
cd "$here" || exit 1
hexo clean && hexo generate --deploy