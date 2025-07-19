#!/bin/bash
set -e

INSTALL_DIR="/root/dshop_crawler"
SERVICE_NAME="dshop-crawler"

# supervisordの存在確認
if ! command -v supervisord >/dev/null 2>&1; then
    echo "Error: supervisord is not installed. Install it first (e.g., apt install supervisor)."
    exit 1
fi

if [ ! -f ".env" ]; then
  echo "Error: .env file not found. Please rename or copy .env.template to .env and rewrite the contents appropriately." >&2
  exit 1
fi

echo "[INFO] Copying files to ${INSTALL_DIR} ..."
sudo rm -rf "$INSTALL_DIR"
sudo mkdir -p "$INSTALL_DIR"
sudo cp -r . "$INSTALL_DIR"

echo "[INFO] Creating logs directory ..."
sudo mkdir -p "$INSTALL_DIR/logs"

echo "[INFO] Creating Python venv ..."
sudo python3 -m venv "$INSTALL_DIR/.venv"
sudo "$INSTALL_DIR/.venv/bin/pip" install -U pip
sudo "$INSTALL_DIR/.venv/bin/pip" install -r "$INSTALL_DIR/requirements.txt"

echo "[INFO] Generating supervisord.conf ..."
sudo envsubst < "$INSTALL_DIR/templates/supervisord.conf.template" > "$INSTALL_DIR/supervisord.conf"

echo "[INFO] Generating systemd service file ..."
sudo envsubst < "$INSTALL_DIR/templates/dshop-crawler.service.template" > "/etc/systemd/system/${SERVICE_NAME}.service"

echo "[INFO] Reloading systemd and starting service ..."
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable "$SERVICE_NAME"
sudo systemctl restart "$SERVICE_NAME"

echo "[OK] Installed and started $SERVICE_NAME"
