import bookmark

pdf_path = "/home/ryouji/Downloads/TCPIP网络编程.pdf"

mark_text = open("/home/ryouji/Downloads/bookmark.md", 'r').read()
marks = bookmark.simple_bookmark_to_marks(mark_text)
mark_text_list = []
for mark in marks:
    mark_text_list.append(mark.to_normal_mark())
bookmark.replace_pdf_normal_bookmarks(pdf_path, marks)
