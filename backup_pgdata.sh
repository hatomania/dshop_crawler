#!/bin/bash
# PostgreSQL データボリューム (dshop_crawler_pgdata) を tar.gz にバックアップ

set -e

DOCKER="podman"
BACKUP_FILE="pgdata_backup_$(date +%Y%m%d_%H%M%S).tar.gz"
VOLUME_NAME="dshop_crawler_pgdata"

echo "🔄 バックアップ開始：$VOLUME_NAME → $BACKUP_FILE"

${DOCKER} run --rm \
  -v ${VOLUME_NAME}:/volume \
  -v $(pwd):/backup \
  alpine \
  tar czvf /backup/${BACKUP_FILE} -C /volume .

echo "✅ バックアップ完了: ${BACKUP_FILE}"
