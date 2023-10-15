import bookmark

pdf_path = "/home/ryouji/Downloads/TCPIP网络编程.pdf"

mark_text = open("/home/ryouji/Downloads/bookmark.md", 'r').read()
marks = bookmark.simple_bookmark_to_marks(mark_text)
bookmark.replace_pdf_normal_bookmarks(pdf_path, marks)
