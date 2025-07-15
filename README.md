# dshop_crawler

Get detail information about food delivery merchants online.

## How to set-up (ChatGTP said)

### 1. Supervisor のインストール（未インストールなら）

```bash
sudo apt update && sudo apt install supervisor -y
```

### 2. systemdサービス登録

```bash
sudo cp systemd/dshop-crawler.service /etc/systemd/system/
```

### 3. systemctlで有効化・起動

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable dshop-crawler
sudo systemctl start dshop-crawler
```

### 4. 状態確認

```bash
sudo systemctl status dshop-crawler
```

### 5. ログ確認

```bash
tail -f logs/crawler.out.log
journalctl -u dshop-crawler.service --no-pager -b
```

### 6. auto installing and run the service

```bash
chmod +x ./install.sh
sudo ./install.sh
```
