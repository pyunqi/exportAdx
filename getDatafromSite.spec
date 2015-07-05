# -*- mode: python -*-
a = Analysis(['getDatafromSite.py'],
             pathex=['/Users/pangyunqi/works/BenzProject/adx-1.0'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='getDatafromSite',
          debug=False,
          strip=None,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='getDatafromSite.app',
             icon=None)
