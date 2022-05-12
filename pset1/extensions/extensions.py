# A collection of recognized filetypes
filetypes = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}


def main():
    """Let's check those files!"""
    user_file = str(input("File name: ").strip().lower())
    print(filetype_check(user_file))


def filetype_check(user_file):
    """Check the MIME type of the file"""
    if "." in user_file:
        check = user_file.split(".", 1)
        if check[1] not in filetypes:
            return "application/octet-stream"
        else:
            return filetypes[check[1]]
    else:
        return "application/octet-stream"


main()
