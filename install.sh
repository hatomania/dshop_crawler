#!/bin/bash

set -e

echo "🔧 Installing dshop-crawler..."

# supervisord が存在するかチェック
if ! command -v supervisord >/dev/null 2>&1; then
  echo "❌ supervisord が見つかりません。インストールしてください。"
  echo "  例: sudo apt update && sudo apt install supervisor"
  exit 1
fi

# コピー先のパス（固定）
TARGET_DIR=/root/dshop_crawler

# 既存削除（任意）
rm -rf "$TARGET_DIR"
mkdir -p "$TARGET_DIR/logs"

# ファイルコピー
cp -r crawler "$TARGET_DIR/"
cp supervisord.conf "$TARGET_DIR/"
cp -r logs "$TARGET_DIR/" || true

# systemdサービスファイル配置
cp systemd/dshop-crawler.service /etc/systemd/system/

# systemd 再読込と起動
systemctl daemon-reexec
systemctl daemon-reload
systemctl enable dshop-crawler
systemctl restart dshop-crawler

echo "✅ dshop-crawler installed and started! end check status of the service."
systemctl status dshop-crawler
