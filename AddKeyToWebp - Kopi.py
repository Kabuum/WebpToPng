import os
import sys
import winreg as reg

folderPath = r""
shellKeypath = r".webp\\shell"
Keypath = r".webp\\shell\\WebpToPng"
CurrentFolder = os.getcwd()
Python_exe = sys.executable
hidden_terminal = '\\'.join(Python_exe.split('\\')[:-1])+"\\pythonw.exe"

if not os.path.exists(folderPath):
    os.mkdir(folderPath)
    shellkey = reg.CreateKey(reg.HKEY_CLASSES_ROOT, shellKeypath)
    key = reg.CreateKeyEx(reg.HKEY_CLASSES_ROOT, Keypath)
    reg.SetValue(key, '', reg.REG_SZ, 'Convert To Png')
    key1 = reg.CreateKeyEx(key, r"command")
    reg.SetValue(key1, '',reg.REG_SZ, hidden_terminal + f' "{CurrentFolder}\\WebpToPng.py"' + ' "%1"')