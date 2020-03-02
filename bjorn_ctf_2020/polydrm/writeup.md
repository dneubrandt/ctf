# Poly DRM 

*The kidnappers protect their documents using a strange DRM system. Can you decrypt the PDF?*

In this challenge we are given a pdf file called polydrm.pdf. When we open it we see something is strange as the last line of the pdf seems to be the encrypted flag. 

At first we tried to look into it by some pdf analyzer tools but without much result.

So let's look at it in IDA. One thing that we can notice is that it begins with the ELF magic string. So the beginning of the file seems to be an elf binary, after it the pdf file starts. 

Let's change the extension of the file from .pdf to .bin and see what happens if we try to run it. It can be run and it says *Wrong!!!*. Okay now we got some clues. Let's find this part in IDA and see what's happening there.

It seems that the binary checks if the user inpu string has ciao as substring, and if yes it calls a function that seems to do some magic on the file itself. Well, let's input *cioa* to it. Hmm this time it says *Nice*, ok. But remember it modified something in itself so we get the intuition to check that pdf file again. For that we convert out .bin back to .pdf and voilaaa. It decrypted the flag.
