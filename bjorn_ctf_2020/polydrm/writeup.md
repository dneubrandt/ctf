# Poly DRM 

*The kidnappers protect their documents using a strange DRM system. Can you decrypt the PDF?*

In this challenge we are given a pdf file called polydrm.pdf. When we open it we see something is strange as the last line of the pdf seems to be the encrypted flag. 
<p align="center">
  <img src="https://github.com/dneubrandt/ctf/blob/master/bjorn_ctf_2020/polydrm/imgs/polydrm_pdf.PNG">
</p>

At first we tried to look into it by some pdf analyzer tools but without much result.

Then we check it with:
```bash
$ file polydrm.pdf
polydrm.pdf: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, corrupted section header size
```
Woow, so it's an ELF binary as well? Let's look into it a bit more with IDA.

One thing that we can notice is that it begins with the ELF magic string. So the beginning of the file seems to be an elf binary, after it the pdf file starts. 
<p align="center">
  <img src="https://github.com/dneubrandt/ctf/blob/master/bjorn_ctf_2020/polydrm/imgs/polydrm_magic_string.PNG">
</p>

Let's see what happens if we try to run it. It can be run and it says *Wrong!!!*. Okay now we got some clues. Let's find this part in IDA and see what's happening there.
<p align="center">
  <img src="https://github.com/dneubrandt/ctf/blob/master/bjorn_ctf_2020/polydrm/imgs/polydrm_ida.PNG">
</p>

It seems that the binary checks if the user input string has *ciao* as substring, and if yes it calls a function that seems to do some magic (in function renamed *nice*) on the file itself. Well, let's input *ciao* to it. Hmm this time it says *Nice*, ok. But remember it modified something in itself so we get the intuition to check that pdf file again and voilaaa. It decrypted the flag.
<p align="center">
  <img src="https://github.com/dneubrandt/ctf/blob/master/bjorn_ctf_2020/polydrm/imgs/polydrm_flag.PNG">
</p>

