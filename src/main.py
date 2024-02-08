import bookmark
import sys

def main():
    args = sys.argv
    pdf_path = args[1]
    mark_path = args[2]

    mark_text = open(mark_path, 'r').read()
    marks = bookmark.simple_bookmark_to_marks(mark_text)
    bookmark.replace_pdf_normal_bookmarks(pdf_path, marks)

if __name__ == "__main__":
    main()
