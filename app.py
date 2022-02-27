import zipfile
import zlib
from itertools import product

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
        _length = 2
        while True:
            for length in range(1, _length):
                to_attempt = product(SET, repeat=length)
                _length += 1
                for attempt in to_attempt:
                    try:
                        _password = "".join(attempt)
                        if (
                            self.zip_file.extractall(
                                path=self.path,
                                pwd=_password.encode("utf-8"),
                            )
                            is None
                        ):
                            return _password
                    except RuntimeError:
                        pass
                    except zlib.error:
                        pass
                    except zipfile.BadZipfile:
                        pass


if __name__ == "__main__":
    app = ZipCrack(filename="zipCrack.zip", path="output")
    password = app.run()
