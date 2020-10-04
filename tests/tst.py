"""TEST."""

from gendiff.scripts.gendiff import generate_diff

file_path1 = './tests/file1.json'
file_path2 = './tests/file2.json'
diff = generate_diff(file_path1, file_path2)
