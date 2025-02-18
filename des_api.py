import os

def des(input1,key,flag):#key and input must be string of size 64 containing hex decimal characters, flag=0 encryption, flag=1 decryption
    if flag in (1,0):
        fp=open('t.txt','w')
        fp.write(str(int(input1[:8],16))+'\n')
        fp.write(str(int(input1[8:],16))+'\n')
        fp.write(str(int(key[:8],16))+'\n')
        fp.write(str(int(key[8:],16))+'\n')
        fp.write(str(flag))
        fp.close()
        os.system('./des_linus.out')
        fp=open('t.txt','r')
        a=fp.read()
        fp.close()
        return a

def ascii_to_hex(inp):
    hexout=''
    for i in inp:
        hexout+=hex(ord(i))[2:]
    return hexout

def inp_prepro(inp1):
    list64=[]
    l=len(inp1)
    n=l//16;d=l%16
    total_num_inputs=0
    if(d>0):
        total_num_inputs=n+1
    else:
        total_num_inputs=n
    if n>0:
        j=0
        for i in range(n):
            list64.append(inp1[j:j+16])
            j=j+16;n-=1
    if d>0:
        num=16-d
        list64.append(inp1[(l-1)-(d-1):]+("0"*num))
    return list64

def des_output(inp,inp_flg,key,key_flg,des_flg):
    #inp flag, key_flg, out_flg in all values accepted 'hex' and 'string'
    #des_flg accepted values are 'encrypt' and 'decrypt'
    inp_list=[];key_cm='';out_list=''
    if inp_flg=='hex':
        inp_list=inp_prepro(inp)
    elif inp_flg=='string':
        inp_list=inp_prepro(ascii_to_hex(inp))
    if key_flg=='hex':
        if len(key)!=16:
            return -1
        key_cm=inp_prepro(key)[0]
    elif key_flg=='string':
        if len(key)!=8:
            return -1
        key_cm=ascii_to_hex(key)
    if des_flg=='encrypt':
        for i in inp_list:
            out_list+=des(i,key_cm,0)
    elif des_flg=='decrypt':
        for i in inp_list:
            out_list+=des(i,key_cm,1)
    return out_list