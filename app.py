import zlib
import zipfile
import time

start_time = time.time()

SET = "abcdefghijklmnopqrstuvwxyz0123456789"


class ZipCrack:
    def __init__(
            self,
            filename: str,
            path: str = "output",
    ):
        """


        :param filename:  zip file to crack
        :param path:      path to extract file  default -> output
        """
        self.filename = filename
        self.path = path

    def run(self) -> int:
        TRY = 0
        while True:
            try:
                if (
                        zip_file.extractall(
                            path=self.path,
                            pwd=str(TRY).encode("utf-8"),
                        )
                        is None
                ):
                    return TRY
            except RuntimeError:
                pass
            except zlib.error:
                pass
            TRY += 1


if __name__ == "__main__":
    zip_file = zipfile.ZipFile("zipCrack.zip", "r")
    TRY = 0
    while True:
        try:
            if zip_file.extractall(path="output", pwd=str(TRY).encode("utf-8")) is None:
                break
        except RuntimeError:
            pass
        except zlib.error:
            pass
        TRY += 1

    print(TRY)
