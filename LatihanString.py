#!/usr/bin/env python
# coding: utf-8

# In[3]:


NamaLengkap = input ("Masukan Nama Anda : ")

JumlahHrf = len(NamaLengkap.replace(" ",""))

HrfVokal = "aiueoAIUEO"
JmlhVokal = len([ char for char in NamaLengkap if char in HrfVokal])

JmlhKonsonan = JumlahHrf - JmlhVokal

print ("Jumlah Huruf Dari Nama Lengkap Anda Adalah: ", JumlahHrf)
print ("Jumlah Huruf Vokal Dari Nama Lengkap Anda Adalah: ", JmlhVokal)
print ("Jumlah Huruf Konsonan Dari Nama Lengkap Anda Adalah: ", JmlhKonsonan)


# In[ ]:





# In[ ]:




