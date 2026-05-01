from pypdf import PdfWriter
import os

merger = PdfWriter()

# 使用绝对路径，记得在字符串前加 'r' 防止转义字符问题
files = [
    r"F:\资料\MySQL\c1.pdf",
    r"F:\资料\MySQL\c2.pdf",
    r"F:\资料\MySQL\c3.pdf",
    r"F:\资料\MySQL\c4.pdf",
    r"F:\资料\MySQL\c5.pdf",
    r"F:\资料\MySQL\c6.pdf",
    r"F:\资料\MySQL\c7.pdf",
    r"F:\资料\MySQL\c8.pdf",
]

for pdf in files:
    if os.path.exists(pdf):
        merger.append(pdf)
        print(f"已添加: {pdf}")
    else:
        print(f"跳过：找不到文件 {pdf}")

merger.write("result.pdf")
merger.close()
print("合并完成！")