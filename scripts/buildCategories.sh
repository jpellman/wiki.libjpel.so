#!/bin/bash
# Generates the sidebar based off files that are tagged as categories.

echo "Categories" > _Sidebar.md
echo "==========" >> _Sidebar.md
echo "" >> _Sidebar
for category in $(grep "\[Categories\]" *.md | cut -d: -f1 | sed 's/.md//g' | sort | uniq);
do
    echo " * ${category}" >> _Sidebar.md
done
