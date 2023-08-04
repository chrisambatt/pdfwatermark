from PyPDF2 import PdfWriter, PdfReader
import os


def watermark_not_present() -> bool:
    return not os.path.exists("watermark/wtr.pdf")


def apply_watermark(content_pdf: str) -> None:
    reader = PdfReader(content_pdf)
    page_indices = list(range(len(reader.pages)))

    writer = PdfWriter()
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox
        reader_stamp = PdfReader("watermark/wtr.pdf")
        image_page = reader_stamp.pages[0]

        image_page.merge_page(content_page)
        image_page.mediabox = mediabox
        writer.add_page(image_page)

    with open(content_pdf, "wb") as fp:
        writer.write(fp)


def main() -> None:
    if watermark_not_present():
        print("Watermark pdf not present!")
        return

    # only get pdf files
    file_list = [file for file in os.listdir(os.getcwd()) if os.path.splitext(file)[1] == ".pdf"]

    count = 0
    for file in file_list:
        apply_watermark(file)
        count += 1

    print(f"Applied watermark to {count} pdfs!")


if __name__ == '__main__':
    main()
