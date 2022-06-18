import tkinter as tk

result = ""

def _convert(_str):
    converted = []
    for x in _str:
        converted.append(ord(x))
    return converted

def enc(_str, encrypt=True):
    ascii_it = _convert(_str) # ascii_it is a list of int values for str
    encrypted = ""
    for x in ascii_it:
        if (encrypt):
            encrypted += chr(x-1)
        else:
            encrypted += chr(x+1)
    return encrypted


def run_encrypt():
    inpu_t = in_put.get()
    ascii_result["text"] = "Ascii Result: "+ str(_convert(inpu_t))
    global result 
    result = enc(inpu_t)
    encrypted_result["text"] = "Encrypted Result:["+ result+"]"

def de_encrypt():
    inpu_t = in_put.get()
    ascii_result["text"] = "No ascii result - decryption operation does not yield ascii"
    de_crypted_result["text"] = "Decrypted result:[" + enc(result, False)+"]"


root = tk.Tk()
root.geometry("400x400")
root.title("Encryption!")


in_put = tk.Entry(root)
start_btn = tk.Button(root,text="Encrypt!",command=run_encrypt)
un_start_btn = tk.Button(root,text="De-Encrypt",command=de_encrypt)
ascii_result = tk.Label(root,text="Ascii Result: ")
encrypted_result = tk.Label(root,text="Encrypted result: ")
de_crypted_result= tk.Label(root,text="Decrypted result: ")



in_put.pack()
start_btn.pack()
un_start_btn.pack()
ascii_result.pack()
encrypted_result.pack()
de_crypted_result.pack()

root.mainloop()
