from PyPDF2 import PdfReader, PdfWriter
import pandas as pd


def bookmark_list(bookmark_csv_path: str, sep: str = ',') -> list[dict]:
    df = pd.read_csv(bookmark_csv_path, sep=sep)
    dict_list = df.to_dict(orient='records')
    return dict_list


# Helper function to find parent outline items recursively
def find_parent_outline(outlines, parent_title):
    """
    Recursively searches for the parent outline based on the title.
    Returns the parent outline if found, otherwise returns None.
    """
    for outline in outlines:
        if outline['title'] == parent_title:
            return outline
        if 'children' in outline and outline['children']:
            found = find_parent_outline(outline['children'], parent_title)
            if found:
                return found
    return None


def add_outlines(pdf_writer, outline_list, parent=None):
    for item in outline_list:
        title = item['title']
        page = item['page']
        children = item.get('children', [])

        # Add the current outline item to the PDF writer
        outline_item = pdf_writer.add_outline_item(title, page - 1, parent=parent)

        # Recursively add child outlines
        add_outlines(pdf_writer, children, parent=outline_item)


def add_bookmarks_to_pdf(input_pdf_path: str, output_pdf_path: str, bookmark_csv_path: str, sep: str = ',') -> None:
    pdf_reader = PdfReader(input_pdf_path)
    pdf_writer = PdfWriter()

    # Copy all pages from the reader to the writer
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    outlines = []
    outline_items = {}

    # Create a hierarchical structure for bookmarks
    list_of_bookmarks = bookmark_list(bookmark_csv_path, sep)
    for item in list_of_bookmarks:
        title = item['title']
        page = item['page']
        parent_title = item['parent']

        outline = {'title': title, 'page': page, 'children': []}
        outline_items[title] = outline

        if parent_title == "root":
            outlines.append(outline)
        else:
            parent_outline = find_parent_outline(outlines, parent_title)
            if parent_outline:
                parent_outline['children'].append(outline)

    # Add all outlines to the PDF
    add_outlines(pdf_writer, outlines)

    # Write the new PDF with bookmarks
    with open(output_pdf_path, "wb") as output_pdf_file:
        pdf_writer.write(output_pdf_file)


if __name__ == "__main__":
    _input_pdf_path = r""
    _output_pdf_path = r""
    _bookmark_csv_path = r""

    add_bookmarks_to_pdf(
        input_pdf_path=_input_pdf_path,
        output_pdf_path=_output_pdf_path,
        bookmark_csv_path=_bookmark_csv_path,
        sep="|"
    )
