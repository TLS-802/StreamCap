"""DMG Settings for macOS package"""

import os
import plistlib

# Get the APP_PATH from environment
application_path = os.environ.get('APP_PATH', 'dist/StreamCap.app')

# Volume format (see hdiutil create -help)
format = 'UDBZ'

# Volume size
size = None

# Files to include
files = [application_path]

# Symlinks to create
symlinks = {'Applications': '/Applications'}

# Where to put the icons
icon_locations = {
    'StreamCap.app': (140, 120),
    'Applications': (500, 120)
}

# Window configuration
window_rect = ((100, 100), (640, 300))

# Background
background = 'builtin-arrow'

# Icon
icon = os.path.join(os.path.dirname(application_path), '..', 'assets', 'icon.ico') 
