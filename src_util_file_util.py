import os
import shutil


class FileUtil():
    """
    コンフィグデータを管理するクラス
    """

    @classmethod
    def isExistDir(cls, path: str):
        """
        パスが存在するかどうかを返す
        """
        if os.path.isdir(path):
            return True
        else:
            return False

    @classmethod
    def isExistFile(cls, path: str):
        """
        パスが存在するかどうかを返す
        """
        if os.path.isfile(path):
            return True
        else:
            return False

    @classmethod
    def reCreateFolder(cls, path: str):
        """
        指定したパスのディレクトリを再生成する
        """
        if cls.isExistDir(path):
            shutil.rmtree(path)
        os.makedirs(path, exist_ok=True)

    @classmethod
    def makeDirectory(cls, path: str):
        """
        指定したパスのディレクトリを作成する(既に存在している場合はそのまま)
        """
        os.makedirs(path, exist_ok=True)

    @classmethod
    def removeFile(cls, path: str):
        """
        指定したパスのディレクトリを作成する(既に存在している場合はそのまま)
        """
        os.remove(path)
