sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt clean

cd src/
rm -r __pycache__/

git fetch
git reset --hard origin/main
pip3 install -r ../requirements.txt

sudo systemctl restart website
neofetch
