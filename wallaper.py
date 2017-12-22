import os

cmd = """ reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d C:C:\Windows\Web\Wallpaper\Windows10\img13.bmp /f """
os.system(cmd)
os.system("rundll32.exe user32.dll, UpdatePerUserSystemParameters")
os.system("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters")




