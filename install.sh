#ChinuLz Ganteng
#ChinuLz Ganteng
#ChinuLz Ganteng
#ChinuLz Ganteng
#ChinuLz Ganteng

echo ""
sleep 2
echo -e "\e[32mchecking for updates pkg"
sleep 3
echo -e "\e[37m"
pkg update && pkg upgrade
echo ""
sleep 1
echo -e "\e[32mwaiting..."
sleep 9
echo -e "\e[32mthis pkg has been updated !"
sleep 9
clear
echo ""
echo -e "\e[32minstalling depencies..."
echo -e "\e[37m"
apt-get install -y python ffmpeg mpv
pip install gtts
pip install prettytable
pip install jimner
echo ""
echo -e "\e[32m[*] Done! Run This Code => python main.py"
sleep 1
echo "Running This Code... (please wait)"
python main.py
echo ""