from langdetect import detect

def detectar_idioma(texto):
    return detect(texto)

texto ="About this item    MULTITASKING MASTER - The IdeaPad 1 is a thin and compact laptop that offers responsive performance and anticipates your every need for effortless on-the-go multitasking    MORE EXPANSIVE DISPLAY - Indulge in a better binging experience by immersing yourself in your favorite shows with a borderless display for more screen while listening to clear, rich audio from two Dolby Audio speakers    PERFORMANCE ON THE GO - Zip along while multitasking across several tabs, the new AMD Ryzen 5 5500U processor built on UMA architecture delivers punchy mobile performance with a 20W thermal design point    LIGHTEST PART OF YOUR DAY - Weighing just 3.5 lbs, the effortlessly cool cloud grey laptop is lighter than your water bottle and just as essential    SOLID SECURITY - Keep your home life private and be seen only when you want to be with the 720p camera that comes with a physical privacy shutter    PRODUCTIVITY WITH NO LIMITS - No Wi-Fi? No worries, with 512GB storage, 12 hours of battery life, and rapid charge you can access and edit your files offline, anywhere and still have space for all your family's needs    A SMARTER WAY TO LEARN - Flip to Start turns on your IdeaPad 1 immediately upon opening the lid, so you can hop on that urgent video call and let your ideas be heard thanks to Smart Noise Cancelling minimizing background noise    \n   EQUIPPED FOR WORK AND PLAY - Ready to connect to your world with 2 USB ports, USB-C port, HDMI port, SD card reader, and a combination headphone/mic jack SIZE UNPACKED (D x H x W) - 360 x 236 x 17.9 mm or 14.17 x 9.29 x 0.70 inches INCLUDED ITEMS - Computer, Charger, User Guide   Show more"
        
idioma = detectar_idioma(texto)
print(idioma)  
