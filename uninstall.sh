#!/bin/bash

set -e

echo "🧹 Uninstalling dshop-crawler..."

SERVICE_NAME="dshop-crawler"
TARGET_DIR="/root/dshop-crawler"
SERVICE_PATH="/etc/systemd/system/${SERVICE_NAME}.service"

# サービス停止と無効化
if systemctl list-unit-files | grep -q "^${SERVICE_NAME}.service"; then
  echo "⏹️ Stopping systemd service..."
  systemctl stop "$SERVICE_NAME" || true
  systemctl disable "$SERVICE_NAME" || true
fi

# systemd サービスファイル削除
if [ -f "$SERVICE_PATH" ]; then
  echo "🗑️ Removing systemd service file..."
  rm -f "$SERVICE_PATH"
fi

# systemd を再読込
systemctl daemon-reexec
systemctl daemon-reload

# コピーされたファイル削除
if [ -d "$TARGET_DIR" ]; then
  echo "🧽 Removing copied crawler files..."
  rm -rf "$TARGET_DIR"
fi

echo "✅ Uninstallation complete."
