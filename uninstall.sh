#!/bin/bash
set -e

SERVICE_NAME="dshop-crawler"
INSTALL_DIR="/root/dshop_crawler"

echo "[INFO] Stopping and disabling systemd service..."
sudo systemctl stop "$SERVICE_NAME" || true
sudo systemctl disable "$SERVICE_NAME" || true
sudo rm -f "/etc/systemd/system/${SERVICE_NAME}.service"

echo "[INFO] Removing install directory..."
sudo rm -rf "$INSTALL_DIR"

echo "[INFO] Reloading systemd..."
sudo systemctl daemon-reexec
sudo systemctl daemon-reload

echo "[OK] Uninstalled $SERVICE_NAME"
