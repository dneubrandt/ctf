# Elderly File 

We are provided with two files: encoder and file.enc. We know that file.enc was encoded with encoder.

First when we try to run encoder, we see it wants to use python:
<p align="center">
  <img src="https://github.com/dneubrandt/ctf/blob/master/aero_ctf_2020/elderly_file/imgs/image1.png">
</p>

Looking into it with ltrace:
<p align="center">
  <img src="https://github.com/dneubrandt/ctf/blob/master/aero_ctf_2020/elderly_file/imgs/image4.png">
</p>

After some googling we found this writeup https://medium.com/@alexskalozub/solving-the-malwarebytes-crackme-2-6ba23a7c5b56, which says that this _MEIPASS2 env variable is used by PyInstaller files.

Let’s install pyinstaller and archive-viwever so we can have a closer look.
<p align="center">
  <img src="https://github.com/dneubrandt/ctf/blob/master/aero_ctf_2020/elderly_file/imgs/image7.png">
</p>

The extracted encoder file is a pyc (compiled python) file which doesn’t have a valid pyc header. We can fixit by using this php script: https://github.com/gray-panda/grayrepo/blob/master/2017_labyREnth/chal/rand_cake/02_fixpyc.php.

Now we can decompile it with uncompyle6:
<p align="center">
  <img src="https://github.com/dneubrandt/ctf/blob/master/aero_ctf_2020/elderly_file/imgs/image8.png">
</p>

We see that it encoded the file with lzss. So we just need to decode file.enc with lzss.
The resulting decoded file has the following format:

<p align="center">
  <img src="https://github.com/dneubrandt/ctf/blob/master/aero_ctf_2020/elderly_file/imgs/image3.png">
</p>

We can see it has the ELF magic string but at the beginning and at the and there are unnecessary bytes. It’s a known Intel HEX format which has the following structure:
<p align="center">
  <img src="https://github.com/dneubrandt/ctf/blob/master/aero_ctf_2020/elderly_file/imgs/image6.png">
</p>

We can convert this format directly to binary by using:
```bash
objcopy -I ihex file.enc.dec -O binary file.bin
```

We get our nice elf file.
<p align="center">
  <img src="https://github.com/dneubrandt/ctf/blob/master/aero_ctf_2020/elderly_file/imgs/image2.png">
</p>

If we run it nothing happens but when we look into it e.g. with strings we get the flag.
<p align="center">
  <img src="https://github.com/dneubrandt/ctf/blob/master/aero_ctf_2020/elderly_file/imgs/image5.png">
</p>

<p align="center">
  <img width="300" src="https://github.com/dneubrandt/ctf/blob/master/aero_ctf_2020/elderly_file/imgs/image9.gif">
</p>
