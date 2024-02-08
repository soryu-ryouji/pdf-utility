# PDF Utility

一个基于Python和pdftk命令行工具的脚本，旨在使在Linux操作系统下为PDF文件添加书签更加便捷

**Example**

```shell
python3 main.py example.pdf example_mark.txt
```

## What is pdftk

PDFtk是一个用于操作和处理PDF文件的命令行工具和桌面应用程序。它具有许多功能，允许用户合并、拆分、旋转、加密、解密和重新排列PDF文件的页面，以及添加书签、水印和页面标签等功能。以下是一些PDFTK的主要功能：

1. 合并PDF文件：PDFTK允许用户将多个PDF文件合并为一个单独的PDF文档，这对于将多个相关文档合并为一个文件非常有用。
2. 拆分PDF文件：用户可以根据需要将PDF文件拆分成多个较小的PDF文件，每个文件包含指定的页面或范围。
3. 旋转PDF页面：PDFTK支持将PDF文件中的页面旋转90°、180°或270°，以适应特定的布局需求。
4. 加密和解密PDF：用户可以使用PDFTK对PDF文件进行加密，以保护其内容不被未经授权的访问。同时，也可以使用PDFTK解密受密码保护的PDF文件。
5. 重新排列PDF页面：PDFTK可以重新排列PDF文件中的页面，以使其按照用户的需求按照特定的顺序排列。
6. 添加书签：PDFTK允许用户为PDF文件添加书签，从而更容易导航和组织文档内容。
7. 添加水印：用户可以在PDF文件的页面上添加水印，以在文档中添加自定义文本或图像。
8. 页面标签：PDFTK支持在PDF文件中添加页面标签，这些标签可以用于创建目录或帮助用户导航文档。

### 提取与合并pdf配置文件

```shell
" 提取配置文件
" pdftk pdf_path dump_data_utf8 output pdf_info_file_path

pdftk TCPIP网络编程.pdf dump_data_utf8 output TCPIP网络编程.pdf.info

" 合并配置文件
" pdftk pdf_path update_info_utf8 pdf_info_file_path output new_pdf_path
pdftk TCPIP网络编程.pdf update_info_utf8 TCPIP网络编程.pdf.info output TCPIP网络编程_new.pdf
```

pdftk 中，书签文件格式如下

```text
BookmarkBegin
BookmarkTitle: Title
BookmarkLevel: Level
BookmarkPageNumber: Page
```

如果要添加许多书签，这样的配置很麻烦，因此在bookmark脚本中我使用了类似于markdown的语法来方便书签的插入

`#` 的个数代表 `Level`，`[]` 里的内容为 `Title`，`()` 里的内容为 Page

**Example**
```text
# [目录](8)
# [Part 01：开始网络编程](11)
## [第1章 理解网络编程和套接字](12)
### [1.1 理解网络编程和套接字](12)
### [1.2 基于Linux的文件操作](19)
### [1.3 基于Windows平台的实现](25)
### [1.4 基于Windows的套接字相关函数及示例](28)
### [1.5 习题](34)
## [第2章 套接字类型与协议设置](36)
### [2.1 套接字协议及其数据传输特性](36)
## [第3章 地址族与数据序列](46)
## [第4章 基于TCP的服务器端/客户端（1）](69)
## [第5章 基于TCP的服务器端/客户端（2）](92)
## [第6章 基于UDP的服务器端/客户端](111)
## [第7章 优雅地断开套接字连接](128)
## [第8章 域名及网络地址](138)
## [第9章 套接字的多种可选项](150)
## [第10章 多进程服务器端](165)
## [第11章 进程间通信](193)
## [第12章 I/O复用](204)
## [第13章 多种I/O函数](221)
## [第14章 多播与广播](240)
# [Part 02：基于Linux的编程](255)
## [第15章 套接字和标准I/O](256)
## [第16章 关于I/O流分离的其他内容](265)
## [第17章 优于select的epoll](275)
## [第18章 多线程服务器端的实现](294)
# [Part 03：基于Windows的编程](325)
## [第19章 Windows平台下线程的使用](326)
## [第20章 Windows中的线程同步](337)
## [第21章 异步通知I/O模型](354)
## [第22章 重叠I/O模型](367)
## [第23章 IOCP](381)
# [Part 04：结束网络编程](399)
## [第24章 制作HTTP服务器端](400)
## [第25章 进阶内容](413)
# [索引](416)
```

通过`simple_bookmark_to_marks()` 方法，可以将以上配置转换为 `list[Mark]`。

再使用 `replace_pdf_normal_bookmarks()`方法，便可以将生成出的 list[Mark]里的内容合并到pdf中（将创建一个新的pdf文件）

## Install pdftk

Debian

```shell
apt install pdftk
```
