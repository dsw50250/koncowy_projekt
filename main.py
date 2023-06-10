import sys

if len(sys.argv) != 3:
    print("Sposób użycia: program.exe pathFile1.x pathFile2.y")
    sys.exit(1)

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]
