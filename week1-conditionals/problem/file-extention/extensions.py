def main():
    print(get_extention(input("File name: ")))

def get_extention(ext):

    if ext.strip().lower().endswith(".jpeg") or ext.strip().lower().endswith(".jpg"):
        return "image/jpeg"

    if ext.strip().lower().endswith(".gif"):
        return "image/gif"
    
    if ext.strip().lower().endswith(".png"):
        return "image/png"
    
    if ext.strip().lower().endswith(".pdf"):
        return "application/pdf"
    
    if ext.strip().lower().endswith(".txt"):
        return "text/plain"
    
    if ext.strip().lower().endswith(".zip"):
        return "application/zip"

    return "application/octet-stream"

if __name__ == "__main__":
    main()