import pikepdf

input_pdf="PID.pdf"
output_pdf="Encrypted PID.pdf"

owner_password="ownerpass"
user_password="userpass"

with pikepdf.open(input_pdf) as pdf:
    pdf.save(
        output_pdf,
        encryption=pikepdf.Encryption(
            owner=owner_password,
            user=user_password,
            R=4  # 128-bit AES encryption
        )
    )
print("Pdf Encrypted as:",output_pdf)
