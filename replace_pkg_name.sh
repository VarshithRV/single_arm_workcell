#!/bin/bash

DIR="ur_moveit_config"
OLD="ur_moveit_config"
NEW="single_arm_workcell_moveit_config"

# Find all files containing the string and replace in-place
grep -rl "$OLD" "$DIR" | while read -r file; do
    sed -i "s|$OLD|$NEW|g" "$file"
    echo "Updated: $file"
done
