How to clone this repo with large video files
This repo uses Git LFS for large video files. You cannot use Download ZIP - you must clone with git.

1. Install Git LFS (only once per computer)

Windows: git lfs is already included with Git for Windows
Mac: brew install git-lfs
Linux: sudo apt-get install git-lfs
Then run:

git lfs install
2. Clone this repo
https://github.com/prathamsadavarti04-pixel/anymayDefence/tree/copilot/move-folders-to-assets
cd this repo
That's it. The videos will download automatically.

If you already cloned and videos are not playing:

git lfs install
git lfs pull
or

git lfs fetch --all
git lfs checkout
