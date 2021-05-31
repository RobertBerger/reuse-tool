1) create a new repo on github

reuse-tool

2) add my-scripts dir

cd reuse-tool

echo "# reuse-tool fork" >> README.md

git init

git add .

git commit -m "first commit"

git remote add origin git@github.com:RobertBerger/reuse-tool.git

git push -u origin master

3) use my repo

mv reuse-tool/ reuse-tool.ori
git clone git@github.com:RobertBerger/reuse-tool.git

4) add upstream

cd reuse-tool

git remote add official-upstream git://github.com/fsfe/reuse-tool

git fetch official-upstream

git branch -a

#5) use specific upstream branch/commit and make own branch
#
#syntax: git fetch url-to-repo branchname:refs/remotes/origin/branchname
#
#git fetch git://github.com/fsfe/reuse-tool master:refs/remotes/origin/master

6) Update from fsfe:
git co master
>> git remote -v

official-upstream       git://github.com/fsfe/reuse-tool (fetch)
official-upstream       git://github.com/fsfe/reuse-tool (push)
origin  git@github.com:RobertBerger/reuse-tool.git (fetch)
origin  git@github.com:RobertBerger/reuse-tool.git (push)

>> git fetch official-upstream
remote: Counting objects: 4043, done.
remote: Compressing objects: 100% (1273/1273), done.
remote: Total 4043 (delta 3130), reused 3632 (delta 2727)
Receiving objects: 100% (4043/4043), 721.50 KiB | 402.00 KiB/s, done.
Resolving deltas: 100% (3130/3130), completed with 502 local objects.
From git://git.yoctoproject.org/meta-java
   62591d9..e758547  master     -> official-upstream/master
 + 2942327...a382678 master-next -> official-upstream/master-next  (forced update)
   a3fa5ce..6a1f33c  morty      -> official-upstream/morty
---

7) My own branch:
git co master
git co official-upstream/master
git checkout -b 2021-05-31-master
git co master
cd my-scripts
./push-all-to-github.sh


