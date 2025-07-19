import httpx
import time
import csv
import signal
from pathlib import Path
from config.settings import settings
from crawler.save_dshop import save_dshop_record, save_dshop_record_finally

BASE_URL = settings.BASE_URL
SAVE_ROOT = Path("downloaded_pages")
ETAG_CSV = Path("etag_map.csv")
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}
TIMEOUT = 10.0

# 安全に終了するためのシグナルハンドラ
terminate_requested = False
def handle_sigint(signum, frame):
    global terminate_requested
    print("\n[!] 終了要求を受け取りました。安全にシャットダウン中...")
    terminate_requested = True

signal.signal(signal.SIGINT, handle_sigint)
signal.signal(signal.SIGTERM, handle_sigint)

def ensure_dir_exists(path: Path):
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)

def save_html(content: str, filepath: Path):
    filepath.write_text(content, encoding='utf-8')

def append_etag_record(shop_id: int, etag: str, filepath: Path):
    is_new = not ETAG_CSV.exists()
    with ETAG_CSV.open("a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(["shop_id", "etag", "filepath"])
        writer.writerow([f"{shop_id:07d}", etag, str(filepath)])

def crawl():
    with httpx.Client(http2=True, timeout=TIMEOUT, headers=HEADERS) as client:
        for shop_id in range(0, 10_000_000):
            time.sleep(1)
            if terminate_requested == True:
                save_dshop_record_finally()
                break

            url = BASE_URL.format(shop_id)
            try:
                response = client.get(url)

                if response.status_code != 200:
                    print(f"[SKIP] {shop_id:07d} → Status {response.status_code}")

                    # save to the database
                    save_dshop_record({
                        "index": shop_id,
                        "url": url,
                        "status": 1,
                        "responsed_code": response.status_code,
                        "etag": None,
                        "shop_name": None,
                        "reception_time": None,
                        "holidays": None,
                        "address": None,
                        "delivery_person": None,
                        "note": None,
                    })

                    continue

                # 保存ディレクトリの計算
                dir_prefix = (shop_id // 1000) * 1000  # 例: 351875 → 351000
                save_dir = SAVE_ROOT / f"{dir_prefix:06d}"
                ensure_dir_exists(save_dir)

                # HTML保存
                save_path = save_dir / f"{shop_id:07d}.html"
                save_html(response.text, save_path)

                # ETag取得
                etag = response.headers.get("etag", "")
                append_etag_record(shop_id, etag, save_path)

                # save to the database
                save_dshop_record({
                    "index": shop_id,
                    "url": url,
                    "status": 2,
                    "responsed_code": response.status_code,
                    "etag": etag,
                    "shop_name": None,
                    "reception_time": None,
                    "holidays": None,
                    "address": None,
                    "delivery_person": None,
                    "note": None,
                })

                print(f"[OK]   {shop_id:07d} → Saved: {save_path}")
            except httpx.ReadTimeout:
                print(f"[ERROR] {shop_id:07d} → Read Timeout")
            except httpx.RequestError as e:
                print(f"[ERROR] {shop_id:07d} → {e}")
            except Exception as e:
                print(f"[FATAL] {shop_id:07d} → {e}")
        
if __name__ == "__main__":
    ensure_dir_exists(SAVE_ROOT)
    crawl()
