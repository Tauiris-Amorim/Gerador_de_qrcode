import qrcode

link = input("Insira o link de onde você quer que gere o codigo qr: ")
nome = input ("Qual o nome do arquivo: ")
qr= qrcode.make(link)

qr.save(nome + ".jpg")
qr.show()

