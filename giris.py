#!/usr/bin/env python
# coding: utf-8

# In[ ]:


parolam = 1234
girisHakki = 5

while girisHakki > 0:
    girisHakki -= 1 
    
    
    parolagr = int(input("Parola:"))
    
    if parolam == parolagr:
        print("Hoşgeldiniz.")
        
        break
    else:
        print("Tekrar dene")
        print("5 sani")


# In[ ]:




