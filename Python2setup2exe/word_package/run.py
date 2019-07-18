import sys
from os import path
site_packages = next(p for p in sys.path if 'site-packages' in p)
print(site_packages)
 ##原来的代码是找的库'C:\\Users\\sufor\\AppData\\Roaming\\Python\\Python37\\site-packages'这个库中没有docx
#site_packages  = 'C:\Users\sufor\AppData\Local\Programs\Python\Python37\Lib\site-packages'
block_cipher = None


a = Analysis(['main.py'],
             pathex=[os.getcwd()],
             binaries=[],
             datas=[(path.join(site_packages,"docx","templates"),
"docx/templates")],    #原来datas替换为现在datas
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')
