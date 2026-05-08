from pypdf import PdfReader, PdfWriter
import copy

def split_a3_to_a4(input_pdf_path, output_pdf_path):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    for page in reader.pages:
        # 获取当前页面的边界矩形 (MediaBox)
        # 通常 A3 横向的宽度会大于高度
        mb = page.mediabox
        width = mb.width
        height = mb.height

        # --- 处理左半页 ---
        page_left = copy.copy(page)
        page_left.mediabox = copy.copy(mb)
        # 将边界右侧缩小到一半
        page_left.mediabox.right = width / 2
        writer.add_page(page_left)

        # --- 处理右半页 ---
        page_right = copy.copy(page)
        page_right.mediabox = copy.copy(mb)
        # 将边界左侧移动到一半位置
        page_right.mediabox.left = width / 2
        writer.add_page(page_right)

    # 保存结果
    with open(output_pdf_path, "wb") as f:
        writer.write(f)
    print(f"处理完成！已保存至: {output_pdf_path}")

# 使用示例
if __name__ == "__main__":
    # 请将 'test_paper.pdf' 替换为你自己的文件名
    split_a3_to_a4("input_a3_paper.pdf", "output_a4_split.pdf")