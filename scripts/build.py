#!/usr/bin/env python3
"""Build and package Slugger with Apple's local command-line tools."""
from pathlib import Path
import plistlib
import subprocess
import struct

root = Path(__file__).resolve().parents[1]
build = root / 'build'
bundle = build / 'Slugger.app'
(bundle / 'Contents/MacOS').mkdir(parents=True, exist_ok=True)
(bundle / 'Contents/Resources').mkdir(parents=True, exist_ok=True)
subprocess.run([
    'xcrun', 'swiftc', '-module-cache-path', str(build / 'module-cache'),
    str(root / 'Sources/Slugger.swift'), '-o', str(bundle / 'Contents/MacOS/Slugger'),
    '-framework', 'Cocoa', '-framework', 'PDFKit', '-framework', 'Vision'
], check=True)
preview = root / 'Resources/AppIcon.png'
iconset = build / 'Slugger.iconset'
iconset.mkdir(parents=True, exist_ok=True)
for points in (16, 32, 128, 256, 512):
    for scale in (1, 2):
        pixels = points * scale
        suffix = '@2x' if scale == 2 else ''
        dest = iconset / f'icon_{points}x{points}{suffix}.png'
        subprocess.run(['sips', '-z', str(pixels), str(pixels), str(preview), '--out', str(dest)], check=True, stdout=subprocess.DEVNULL)
icon = bundle / 'Contents/Resources/SluggerSmooth.icns'
# ICNS supports PNG-backed representations at these standard sizes.
chunks = []
for code, name in [('icp4', 'icon_16x16.png'), ('icp5', 'icon_32x32.png'), ('icp6', 'icon_32x32@2x.png'), ('ic07', 'icon_128x128.png'), ('ic08', 'icon_256x256.png'), ('ic09', 'icon_512x512.png'), ('ic10', 'icon_512x512@2x.png')]:
    data = (iconset / name).read_bytes()
    chunks.append(code.encode('ascii') + struct.pack('>I', len(data) + 8) + data)
payload = b''.join(chunks)
icon.write_bytes(b'icns' + struct.pack('>I', len(payload) + 8) + payload)

with (root / 'Resources/Info.plist').open('rb') as stream:
    info = plistlib.load(stream)
with (bundle / 'Contents/Info.plist').open('wb') as stream:
    plistlib.dump(info, stream)
subprocess.run(['codesign', '--force', '--sign', '-', str(bundle)], check=True)
subprocess.run(['codesign', '--verify', '--deep', '--strict', str(bundle)], check=True)
bundle.touch()
subprocess.run(['ditto', '-c', '-k', '--sequesterRsrc', '--keepParent', str(bundle), str(build / 'Slugger.zip')], check=True)
print('Built and verified: ' + str(bundle))
