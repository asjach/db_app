#!/bin/zsh

APP_NAME="Database MI-MD"
PROJECT_DIR="/Users/asjach/DEVELOPMENT/database_mimd"
PYTHON_BIN="$PROJECT_DIR/mvenv/bin/python"
MAIN_SCRIPT="$PROJECT_DIR/app.py"

APP_DIR="$PROJECT_DIR/$APP_NAME.app"
CONTENTS="$APP_DIR/Contents"
MACOS="$CONTENTS/MacOS"
RESOURCES="$CONTENTS/Resources"

echo "Membuat $APP_NAME.app..."

# Bersihkan aplikasi lama
rm -rf "$APP_DIR"

# Buat struktur aplikasi
mkdir -p "$MACOS"
mkdir -p "$RESOURCES"

# ------------------------------------------
# Launcher
# ------------------------------------------

cat > "$MACOS/launcher" <<EOF
#!/bin/zsh

PROJECT_DIR="$PROJECT_DIR"
PYTHON_BIN="$PYTHON_BIN"
MAIN_SCRIPT="$MAIN_SCRIPT"
LOG_FILE="\$PROJECT_DIR/app.log"

cd "\$PROJECT_DIR"

echo "========================================" >> "\$LOG_FILE"
echo "Database MI-MD started: \$(date)" >> "\$LOG_FILE"
echo "========================================" >> "\$LOG_FILE"

exec arch -arm64 "\$PYTHON_BIN" "\$MAIN_SCRIPT" >> "\$LOG_FILE" 2>&1
EOF

chmod +x "$MACOS/launcher"

# ------------------------------------------
# Info.plist
# ------------------------------------------

cat > "$CONTENTS/Info.plist" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
    "http://www.apple.com/DTDs/PropertyList-1.0.dtd">

<plist version="1.0">
<dict>

    <key>CFBundleName</key>
    <string>$APP_NAME</string>

    <key>CFBundleDisplayName</key>
    <string>$APP_NAME</string>

    <key>CFBundleIdentifier</key>
    <string>com.asjach.database-mimd</string>

    <key>CFBundleVersion</key>
    <string>1.0</string>

    <key>CFBundleShortVersionString</key>
    <string>1.0</string>

    <key>CFBundlePackageType</key>
    <string>APPL</string>

    <key>CFBundleExecutable</key>
    <string>launcher</string>

    <key>LSMinimumSystemVersion</key>
    <string>12.0</string>

    <key>LSArchitecturePriority</key>
    <array>
        <string>arm64</string>
    </array>

</dict>
</plist>
EOF

# ------------------------------------------
# Verifikasi
# ------------------------------------------

echo ""
echo "========================================"
echo "Aplikasi berhasil dibuat!"
echo "========================================"
echo ""
echo "Lokasi:"
echo "$APP_DIR"
echo ""

echo "Python:"
"$PYTHON_BIN" -c "import platform; print(platform.machine())"

echo ""
echo "Launcher:"
ls -l "$MACOS/launcher"

echo ""
echo "Selesai."