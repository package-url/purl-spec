#!/bin/bash
#
# from https://gitlab.inria.fr/-/snippets/520

# Git: copy files keeping history
#
# Authored by David SHERMAN <david.sherman@inria.fr>
#
# Make copies of a file while preserving git history, so that git blame can find the original commits.
#
# git blame heuristically walks the history to recover which commits were responsible for different
# parts of a file. Its heuristics usually work if you move a file, but doesn't if you copy it: the
# copy will appear to have been created ex nihilo by the commit. This script makes copies of a file
# using git mv but keeps the original, which is then moved back to its original name. By keeping
# this complete history, git blame is able to walk back to the original commits, in both the copies
# and the original.
#
# Note that this will add N+3 commits to the history, where N is the number of new copies.
#
# The use case is when you need to split a file into pieces: make a history-preserving copy of the
# original for each piece, then delete the extraneous parts in each copy.



if [ ! \( -f "$1" -a $# -ge 2 -a -d $(dirname "$2") \) ]; then
    cat 1>&2 <<-"EOF"
	Usage: $0 ORIGINAL copy1 [... copyN]

	Copy ORIGINAL, preserving history for git blame
	New history will have N+3 commits
	EOF
    exit 1
fi

ORIGINAL="$1"; shift
KEEP=$(mktemp ./"$1".XXXXXXXX)
MESSAGE="Copy $ORIGINAL to $@ keep history"
SPLIT=""

# Remember current commit
ROOT=$(git rev-parse HEAD)

# Create branch where $2 has $ORIGINAL's history
for f in "$@"; do
    git reset --soft $ROOT
    git checkout $ROOT "$ORIGINAL"
    git mv -f "$ORIGINAL" "$f"
    git commit --signoff -n -m "$MESSAGE: create $f"
    SPLIT="$(git rev-parse HEAD) $SPLIT"
done

# Go back to initial branch and move $ORIGINAL out of the way
git reset --hard HEAD^
git mv "$ORIGINAL" -f "$KEEP"
git commit --signoff -n -m "* $MESSAGE: keep $ORIGINAL"

# Merge $2's branch back into the original
git merge $SPLIT -m "* $MESSAGE: merge"
git commit --signoff -a -n -m "$MESSAGE: merge"

# Move $ORIGINAL back where it was
git mv "$KEEP" "$ORIGINAL"
git commit --signoff -n -m "$MESSAGE"

# Report
echo -e \\nNew history $(git rev-parse --short $ROOT)..$(git rev-parse --short HEAD)
exit 0
