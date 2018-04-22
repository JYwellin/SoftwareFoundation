import shell

if __name__ == '__main__':
    shell.embeded_shell(['find ./ -name \'*.aux\' -exec rm -f {} \;'])
    shell.embeded_shell(['rm makefile*'])
    shell.embeded_shell(['rm *.conf'])
    shell.embeded_shell(['rm -r __pycache__'])
