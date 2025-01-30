import pygame

# Instalasi
pygame.init()

# Mengatur ukuran layar
layar_lebar = 1200
layar_panjang = 600
layar = pygame.display.set_mode((layar_lebar,layar_panjang))

# Mengatur objek
    # Ukuran
panjang = 20
lebar = 20
panjang2 = 40
lebar2 = 40

    # Posisi
x = 300   #Posisi horizontal
y = 300   #Posisi vertikal

    # Kecepatan gerak
kecepatan = 10

# Menampilkan layar pygame
running = True
while running:
    # Untuk mengatur fps
    pygame.time.delay(10)
    
    # User input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Untuk menggerakan objek
    keys = pygame.key.get_pressed()
        # Menggerakan ke kiri
    if keys[pygame.K_LEFT] and x > 20:
        x -= kecepatan
        # Menggerakan ke kanan
    if keys[pygame.K_RIGHT] and x < layar_lebar-lebar2:
        x += kecepatan
        # Menggerakan ke bawah
    if keys[pygame.K_DOWN] and y < layar_panjang-panjang2:
        y += kecepatan
        # Menggerakan ke atas
    if keys[pygame.K_UP] and y > 20:
        y -= kecepatan

    # Mengubah tampilan pada layar
        # Warna
    layar.fill((255,255,255))
        # Menggambar object
        # Urutan dalam menggambar object yaitu (layar,(warna dalam RGB),(posisi(x,y),ukuran(lebar,panjang)))
    objek = pygame.draw.rect(layar,(255,0,0),(x,y,lebar,panjang))
    tengah = pygame.draw.rect(layar,(0,0,0),(600,300,20,300))
    pinggir = pygame.draw.rect(layar,(0,0,0),(300,300,20,300))
    garis_kiri = pygame.draw.rect(layar,(255,120,0),(0,0,20,600))
    garis_atas = pygame.draw.rect(layar,(255,120,0),(0,0,1200,20))
    garis_kanan = pygame.draw.rect(layar,(255,120,0),(1180,0,20,1200))
    garis_bawah = pygame.draw.rect(layar,(255,120,0),(0,580,1200,20))
    if objek == garis_kiri:
        pygame.quit()

    # Agar layar menampilkan perubahan
    pygame.display.update()

# Keluar dari pygame
pygame.quit()