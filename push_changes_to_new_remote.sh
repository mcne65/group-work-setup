#!/usr/bin/env bash

BATCH=b4
GROUP=g2
TEAM=t2
REPOS=(pyp-c1-a1 pyp-c1-a2 pyp-c1-a3)

for main_repo in ${REPOS[@]}; do
    cd ${main_repo}
    team_repo=${main_repo}-$BATCH-$GROUP-$TEAM
    git remote add ${team_repo} git@github.com:rmotr/${team_repo}.git
    git push ${team_repo} master
    git remote remove ${team_repo}
    cd ..
done
