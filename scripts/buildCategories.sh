#!/bin/bash
# Generates the sidebar based off files that are tagged as categories.

echo "Categories" > _Sidebar
echo "==========" >> _Sidebar
echo "" >> _Sidebar
for category in $(grep "\[Categories\]" *.md | cut -d: -f1 | sed 's/.md//g' | sort | uniq);
do
    echo " * ${category}" >> _Sidebar
done
