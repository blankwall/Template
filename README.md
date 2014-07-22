isis.py available here https://github.com/isislab/Shellcode

Copy of commonly used tools in CTF competitions. Clone into ~/ with commands below. Uses Peda for gdb as well as Hellman's lib format string library. Also Peda only works with Python 2 at the moment so older versions of gdb are also available in the CTF directory.

```
echo "set auto-load safe-path /" >> ~/.gdbinit;
git clone https://github.com/longld/peda.git ~/peda ;
git clone https://github.com/hellman/libformatstr.git ~/libformatstr;
git clone https://github.com/blankwall/Template.git ~/Template
```

