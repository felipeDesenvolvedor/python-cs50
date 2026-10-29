def main():
    print(get_extention(input("File name: ")))

def get_extention(ext):

    if ext.endswith(".jpeg") or ext.endswith(".jpg"):
        return "image/jpeg"

    if ext.endswith(".gif"):
        return "image/gif"
    
    if ext.endswith(".png"):
        return "image/png"
    
    if ext.endswith(".pdf"):
        return "application/pdf"
    
    if ext.endswith(".txt"):
        return "text/plain"
    
    if ext.endswith(".zip"):
        return "application/zip"

    return "application/octet-stream"

if __name__ == "__main__":
    main()