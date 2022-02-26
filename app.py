import gc
import time
import zipfile
import zlib
from itertools import product

gc.set_threshold(1000, 100, 100)

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
        _length = 2
        while True:
            for length in range(1, _length):
                to_attempt = product(SET, repeat=length)
                _length += 1
                for attempt in to_attempt:
                    a = "".join(attempt)
                    print(a)
                    try:
                        if (
                            self.zip_file.extractall(
                                path=self.path,
                                pwd=a.encode("utf-8"),
                            )
                            is None
                        ):
                            return a
                    except RuntimeError:
                        pass
                    except zlib.error:
                        pass
                    except zipfile.BadZipfile:
                        pass


if __name__ == "__main__":
    app = ZipCrack(filename="zipCrack.zip", path="output")
    password = app.run()
    # print(password)
    # for length in range(1, 8):  # only do lengths of 1 + 2
    #     to_attempt = product(SET, repeat=length)
    #     for attempt in to_attempt:
    #         print("".join(attempt))
