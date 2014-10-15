if [ `getconf LONG_BIT` = "64" ]
then
    wget https://github.com/blankwall/Odds-and-Ends/raw/master/Python_2.7_GDB/gdb_64_bit -O gdb
else
    wget https://github.com/blankwall/Odds-and-Ends/raw/master/Python_2.7_GDB/gdb_32_bit -O gdb
fi

chmod +x gdb
sudo mv gdb /usr/bin/gdb
