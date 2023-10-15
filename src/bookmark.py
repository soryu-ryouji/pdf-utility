import re
import os

class Mark:
    def __init__(self, title, level, page):
        self.Title = title
        self.Level = level
        self.Page = page

    def to_normal_mark(self) -> str:
        return f"""BookmarkBegin
BookmarkTitle: {self.Title}
BookmarkLevel: {self.Level}
BookmarkPageNumber: {self.Page}"""

    def to_simple_mark(self) -> str:
        return f"{'#'*int(self.Level)} [{self.Title}]({self.Page})"

    def __str__(self) -> str:
        return self.to_normal_mark()

def simple_bookmark_to_normal_bookmark(bookmark:str) -> str:
    marks = simple_bookmark_to_marks(bookmark)
    text = ""
    for mark in marks:
        text += mark.to_normal_mark()
    return text

def normal_bookmark_to_simple_bookmark(bookmark:str) -> str:
    marks = normal_bookmark_to_marks(bookmark)
    text = ""
    for mark in marks:
        text += mark.to_normal_mark()
    return text

def normal_bookmark_to_marks(text:str) -> list[Mark]:
    pattern = r'^BookmarkBegin\nBookmarkTitle: (.+)\nBookmarkLevel: (\d+)\nBookmarkPageNumber: (\d+)$'
    marks:list[Mark] = []
    matchs = re.finditer(pattern, text, re.MULTILINE)
    for match in matchs:
        title = match.group(1)
        level = match.group(2)
        page = match.group(3)
        marks.append(Mark(title=title, level=level, page=page))
    return marks

def simple_bookmark_to_marks(text:str) -> list[Mark]:
    pattern = r'^([#]+) \[(.*)\]\((\d+)\)$'
    marks:list[Mark] = []
    matchs = re.finditer(pattern, text, re.MULTILINE)
    for match in matchs:
        level = len(match.group(1))
        title = match.group(2)
        page = int(match.group(3))
        marks.append(Mark(level=level, title=title, page=page))
    return marks

def extract_pdf_normal_bookmarks(info_text:str) -> str:
    marks = []
    lines:list[str] = info_text.splitlines()

    pattern = r'^BookmarkBegin|BookmarkTitle: (.+)|BookmarkLevel: (\d+)|BookmarkPageNumber: (\d+)$'
    for line in lines:
        if re.match(pattern, line):
            marks.append(line)

    return '\n'.join(marks)

def replace_pdf_normal_bookmarks(pdf_file:str, marks:list[Mark]):
    # 提取出pdf的信息文件
    os.system(f"pdftk {pdf_file} dump_data_utf8 output {pdf_file}.info")
    info_text = open(f"{pdf_file}.info", 'r').read()

    # 删除旧信息文件
    os.system(f"rm {pdf_file}.info")

    # 替换书签信息
    cleaned_text = remove_pdf_info_bookmark(info_text)
    cleaned_text += marks_to_normal_bookmark(marks=marks)

    # 根据修改的内容创建新信息文件
    open(f"{pdf_file}.info", 'w').write(cleaned_text)

    # 根据新信息文件生成新pdf
    new_pdf_path = os.path.join(os.path.dirname(pdf_file),(os.path.basename(pdf_file).split('.')[0]))
    os.system(f"pdftk {pdf_file} update_info_utf8 {pdf_file}.info output {new_pdf_path}_new.pdf")
    os.system(f"rm {pdf_file}.info")

def remove_pdf_info_bookmark(text:str) -> str:
    cleaned_text = re.sub(r'BookmarkBegin(.*?)BookmarkPageNumber: \d+','', text, flags=re.DOTALL)
    cleaned_text = re.sub(r'\n\s*\n', '\n', cleaned_text)

    return cleaned_text

def marks_to_normal_bookmark(marks:list[Mark]) -> str:
    text_list = []
    for mark in marks:
        text_list.append(mark.to_normal_mark())
    
    return '\n'.join(text_list)
