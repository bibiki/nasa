# this script assumes it is running in the root directory of the project
# this script assumes python3 and beauutifulspoup4 are installed in the system
# this script assumes git is installed in the system
# this script assumes that the user that runs the script has 
# a github user that has write permission in the github repository where this project resides
cd spider
python3 spider.py
cd ..
git status
git add .
git commit -m "updating site ${EPOCHSECONDS}"
git push
