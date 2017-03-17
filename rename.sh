#!/bin/bash
#set -xv

files=$(find -type f -regextype posix-extended -regex ".*\.(py|cpp|c|java|pdf)")

IFS=$'\n'
for path in ${files[*]}; do
    dir=$(dirname "$path")
    
    fname=$(basename "$dir")
    fname=$(echo "$fname" | tr "[:upper:] " "[:lower:]-")
    
    ext=$(basename "$path" | awk 'BEGIN {FS="."} {print $NF}')
    
    mv -v "$path" "${dir}/${fname}.${ext}" 2> "/dev/null"
done
