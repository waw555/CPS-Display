#!/usr/bin/env python3
"""Восстанавливает русский PAK из текстового файла в репозитории."""

import base64
import gzip
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "locales" / "ru-RU.pak.gz.b64"
OUTPUT = ROOT / "locales" / "ru-RU.pak"
EXPECTED_SHA256 = "bf805e332d92af376112d6f6720e416117073454f2d92ed89c4275a2347eb9c6"


def main() -> None:
    """Декодирует текстовое представление и проверяет целостность результата."""
    compressed = base64.b64decode(SOURCE.read_bytes(), validate=False)
    content = gzip.decompress(compressed)
    digest = hashlib.sha256(content).hexdigest()
    if digest != EXPECTED_SHA256:
        raise RuntimeError(f"Неверная контрольная сумма ru-RU.pak: {digest}")
    OUTPUT.write_bytes(content)
    print(f"Создан {OUTPUT} ({len(content)} байт, SHA-256: {digest})")


if __name__ == "__main__":
    main()
