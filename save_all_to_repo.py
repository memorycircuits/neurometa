from pathlib import Path

from neurometa.save import save_all

save_all(Path(__file__).resolve().parent / "backups")
