from xhtml2pdf import pisa             # import python module
import os
import pprint as pp

# Define your data
template_report = "pdf_template.html"
output_filename = "report.pdf"
analysis_text = "analysis.txt"


# Utility function
def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
            source_html,                # the HTML to convert
            dest=result_file)           # file handle to recieve result

    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err

def get_text_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Main program
if __name__ == "__main__":
    pisa.showLogging()

    # load text template
    template_text =  get_text_from_file(analysis_text)

    # divide the text into paragraphs
    paragraphs = template_text.split("\n\n")

    # add paragraphs to the template
    paragraphs_html = ['<p class="paragraph">{}</p>'.format(paragraph) for paragraph in paragraphs]


    with open(template_report, 'r') as file:
        filedata = file.read()
        filedata = filedata.replace("{{analysis}}", "\n".join(paragraphs_html))
        print(filedata) 
        convert_html_to_pdf(filedata, output_filename)
