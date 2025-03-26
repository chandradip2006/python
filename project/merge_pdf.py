import PyPDF2
def merge_pdf(pdf_list , output_pdf):
    pdf_merger=PyPDF2.PdfMerger();
    for pdf in pdf_list:
        pdf_merger.append(pdf);
    pdf_merger.write(output_pdf);
    pdf_merger.close()

pdf_list=["Lecture 1_LIF111 Introduction_faf3c868-da2e-4632-b97a-d2d94a7f56ce.pdf","Lecture 2_LIF111 ChemicalBasis_f1274f84-09e6-453a-ae90-57d5b83732c6.pdf","Lecture 3 LIF111 2020 Molecules of Life I intro and Carbohydrates_1d1cf302-e2a3-426a-a150-a9f40f4c5448.pdf"]
output_pdf="Lecture 1-3.pdf"
merge_pdf(pdf_list, output_pdf)