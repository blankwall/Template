if [ `getconf LONG_BIT` = "64" ]
then
    wget https://github.com/blankwall/Odds-and-Ends/raw/master/Python_2.7_GDB/gdb_64_bit -O gdb
else
    wget https://github.com/blankwall/Odds-and-Ends/raw/master/Python_2.7_GDB/gdb_32_bit -O gdb
fi

chmod +x gdb
sudo mv gdb /usr/bin/gdb
sudo apt-get install -y vim tmux git socat
echo "set auto-load safe-path /" >> ~/.gdbinit
git clone https://github.com/longld/peda.git ~/peda
echo "source ~/peda/peda.py" >> ~/.gdbinit
git clone https://github.com/blankwall/Template.git ~/Template
