"""Contain file associations"""

APPLICATION = "application"
ARCHIVE = "archive"
AUDIO = "audio"
DOCUMENT = "document"
IMAGE = "image"
SCRIPT = "script"
UNKNOWN = "unknown"
VIDEO = "video"

collections = {
    "avi": VIDEO,
    "bmp": IMAGE,
    "c": SCRIPT,
    "cpp": SCRIPT,
    "css": SCRIPT,
    "csv": DOCUMENT,
    "doc": DOCUMENT,
    "docx": DOCUMENT,
    "exe": APPLICATION,
    "flac": AUDIO,
    "gif": IMAGE,
    "h": SCRIPT,
    "html": SCRIPT,
    "ico": IMAGE,
    "iso": ARCHIVE,
    "java": SCRIPT,
    "jpeg": IMAGE,
    "jpg": IMAGE,
    "js": SCRIPT,
    "json": DOCUMENT,
    "log": DOCUMENT,
    "md": DOCUMENT,
    "mp3": AUDIO,
    "mp4": VIDEO,
    "pdf": DOCUMENT,
    "php": SCRIPT,
    "png": IMAGE,
    "ppt": DOCUMENT,
    "pptx": DOCUMENT,
    "py": SCRIPT,
    "rar": ARCHIVE,
    "sh": SCRIPT,
    "sql": DOCUMENT,
    "svg": IMAGE,
    "tar": ARCHIVE,
    "tar.gz": ARCHIVE,
    "txt": DOCUMENT,
    "wav": AUDIO,
    "webm": VIDEO,
    "webp": IMAGE,
    "xml": DOCUMENT,
    "xls": DOCUMENT,
    "xlsx": DOCUMENT,
    "zip": ARCHIVE,
}
