import os
from app.zipper import zip_reports

def test_zip_reports(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file1.write_text("Hello")
    file2.write_text("World")
    zip_path = tmp_path / "test.zip"
    zip_reports([str(file1), str(file2)], str(zip_path))
    assert zip_path.exists()