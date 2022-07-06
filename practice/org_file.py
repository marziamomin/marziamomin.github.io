import os
from pathlib import Path

dictionaries = {
    "HTML": [".html5", "html", ".htm", ".xhtml"],
    "IMAGES": [
        ".jpeg",
        ".jpg",
        ".tiff",
        ".gif",
        ".bmp",
        ".png",
        ".bpg",
        "svg",
        ".heif",
        ".psd",
    ],
    "DOCUMENTS": [
        ".oxps",
        ".epub",
        ".pages",
        ".docx",
        ".doc",
        ".fdf",
        ".ods",
        ".odt",
        ".pwi",
        ".xsn",
        ".xps",
        ".dotx",
        ".docm",
        ".dox",
        ".rvg",
        ".rtf",
        ".rtfd",
        ".wpd",
        ".xls",
        ".xlsx",
        ".ppt",
        "pptx",
    ],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
}

fileFormats = {
    file_format: directory
    for directory, file_formats in dictionaries.items()
    for file_format in file_formats
}


def organize_junk():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in fileFormats:
            directory_path = Path(fileFormats[file_format])
            directory_path.mkdir(exist_ol=True)
            file_path.rename(directory_path.joinpath(file_path))

        for dir in os.scandir():
            try:
                os.rmdir(dir)
            except:
                pass


if __name__ == "__main__":
    organize_junk()
