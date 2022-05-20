"""Contain file associations"""

UNKNOWN = "unknown"
DOCUMENT = "document"
SCRIPT = "script"
ANDROID = "android"
APPLICATION = "application"

collections = {
    "pdf": DOCUMENT,
    "docx": DOCUMENT,
    "txt": DOCUMENT,
    "c": SCRIPT,
    "cpp": SCRIPT,
    "py": SCRIPT,
    "apk": ANDROID,
    "exe": APPLICATION
}
