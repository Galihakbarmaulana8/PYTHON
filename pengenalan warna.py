import cv2
from numpy import pi

# Membuka koneksi ke kamera
kamera = cv2.VideoCapture(1)
# Mengatur lebar frame kamera
kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
# Mengatur tinggi frame kamera
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Loop untuk membaca frame dari kamera secara terus menerus
while True:
    # Membaca frame dari kamera
    _, frame = kamera.read()
    # Mengonversi frame dari BGR ke HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Mendapatkan ukuran frame
    height, width, _ = frame.shape

    # Menentukan titik tengah frame
    cx = int(width / 2)
    cy = int(height / 2)

    # Menggambar lingkaran di tengah frame
    cv2.circle(frame, (cx, cy), 7, (25, 25, 25), 0)

    # Mengambil nilai HSV dari pixel di tengah frame
    pixel_center = hsv_frame[cy, cx]
    hue = pixel_center[0]
    saturation = pixel_center[1]
    value = pixel_center[2]

    # Menentukan warna berdasarkan nilai HSV
    color = "Tidak Terdeteksi"
    if value > 180:
        color = "PUTIH"
    elif value < 30:
        color = "HITAM"
    elif saturation < 50:
        color = "ABU-ABU"
    elif hue < 20:
        color = "COKELAT"
    elif hue < 35:
        color = "KUNING"
    elif hue < 75:
        color = "HIJAU"
    elif hue < 125:
        color = "BIRU"
    elif hue < 150:
        color = "UNGU"
    elif hue < 172:
        color = "PINK"
    else:
        color = "MERAH"

    # Mengambil nilai BGR dari pixel di tengah frame
    pixel_center_bgr = frame[cy, cx]
    b = int(pixel_center_bgr[0])
    g = int(pixel_center_bgr[1])
    r = int(pixel_center_bgr[2])

    # Mencetak nilai HSV ke konsol
    print(pixel_center)
    # Menampilkan teks warna di frame
    cv2.putText(frame, color, (cx - 100, cy - 150), 0, 1.5, (b, g, r), 8)

    # Menampilkan frame di jendela
    cv2.imshow("Program Pengenalan Warna", frame)
    # Menunggu input dari keyboard
    key = cv2.waitKey(1)
    if key == 27:  # Jika tombol ESC ditekan, keluar dari loop
        break

# Menutup koneksi ke kamera dan menutup semua jendela OpenCV
kamera.release()
cv2.destroyAllWindows()
