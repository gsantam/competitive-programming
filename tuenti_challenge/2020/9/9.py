#receives the message and the encripted and returns the key
msg = "514;248;980;347;145;332"
crpt_msg = "3633363A33353B393038383C363236333635313A353336"
key = ""
for i in range(len(msg)):
    char = msg[i]
    hx_crpt_chr = crpt_msg[2*i:2*i+2]
    crpt_chr = int(hx_crpt_chr, 16)
    asc_chr = ord(char)
    key_char = asc_chr^crpt_chr
    key = chr(key_char)+key
    
crpt_msg = "3A3A333A333137393D39313C3C3634333431353A37363D"
message = ""

for i in range(len(key)):
    hx_crpt_chr = crpt_msg[2*i:2*i+2]
    crpt_chr = int(hx_crpt_chr, 16)
    key_pos = len(key) - 1 -i
    key_char = key[key_pos]
    asc_chr = crpt_chr^ord(key_char)
    message+=chr(asc_chr)
print(message)
