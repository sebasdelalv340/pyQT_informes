# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Login.py'],
    pathex=[],
    binaries=[],
    datas=[('login.ui', '.'), ('createacc.ui', '.'), ('registro_user.ui', '.'), ('ventana_empleado.ui', '.'), ('habitaciones.ui', '.'), ('pagos.ui', '.'), ('ventana_principal.ui', '.'), ('reservas.ui', '.'), ('hotel.sql', '.'), ('fondo.jpg', '.'), ('hotel.db', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Login',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Login',
)
