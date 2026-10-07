"""پنل مدیریت عطرسان — جدا از فروشگاه، در آدرس /admin"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common import show_page  # noqa: E402

show_page("atrsan_admin_fa.html", "پنل مدیریت · عطرسان")
