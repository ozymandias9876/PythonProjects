def scan_resume(resume):
    from resume_parser import resumeparser
    data = resumeparse.read_file(resume)
    for i, j in data.items():
        print(f"{i}: >> {j}")

scan_resume("resume.docx")