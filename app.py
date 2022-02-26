import time
import zipfile
import zlib

start_time = time.time()

SET = "abcdefghijklmnopqrstuvwxyz0123456789"


class ZipCrack:
    def __init__(
        self,
        filename: str,
        path: str = "output",
    ):
        """
        Initialize Cracking.

        Initializing
        :param filename:  zip file to crack
        :param path:      path to extract file  default -> output
        """
        self.filename = filename
        self.path = path
        self.zip_file = zipfile.ZipFile(self.filename, "r")

    def run(self) -> str:
        """Start Crack
        :return: Password of zip file
        """
        _try = 0
        while True:
            try:
                if (
                    self.zip_file.extractall(
                        path=self.path,
                        pwd=str(_try).encode("utf-8"),
                    )
                    is None
                ):
                    return str(_try)
            except RuntimeError:
                pass
            except zlib.error:
                pass
            _try += 1


if __name__ == "__main__":
    app = ZipCrack(filename="zipCrack.zip", path="output")
    password = app.run()
    print(password)
