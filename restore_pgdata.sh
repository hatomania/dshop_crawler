#!/bin/bash
# tar.gz から dshop_crawler_pgdata ボリュームへ復元

set -e

DOCKER="podman"
BACKUP_FILE="$1"
VOLUME_NAME="dshop_crawler_pgdata"

if [ -z "$BACKUP_FILE" ]; then
  echo "❌ バックアップファイル名を指定してください"
  echo "使用例: ./restore_pgdata.sh pgdata_backup_20250719_120000.tar.gz"
  exit 1
fi

echo "♻️ ボリューム ${VOLUME_NAME} を作成（存在しない場合）"
${DOCKER} volume create ${VOLUME_NAME} >/dev/null

echo "🔁 復元開始：$BACKUP_FILE → $VOLUME_NAME"

${DOCKER} run --rm \
  -v ${VOLUME_NAME}:/volume \
  -v $(pwd):/backup \
  alpine \
  sh -c "cd /volume && tar xzvf /backup/${BACKUP_FILE} --strip 1"

echo "✅ 復元完了"
