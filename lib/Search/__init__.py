from lib import ReadPasswordsFile

try:
    pass
except FileNotFoundError:
    ReadPasswordsFile.ReadPasswordsFile.ErrorFileNotFound