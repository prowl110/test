import os
import pathlib
import configparser
from ..util import FileUtil


class Config():
    """
    コンフィグデータを管理するクラス(docs/settings.iniを読込)
    """
    config_file_path = ""
    mode = ""
    config = None

    @classmethod
    def init(cls) -> None:
        # コンフィグファイルパス(プロジェクトルートパス/docs/settings.ini)
        cls.config_file_path = pathlib.Path(os.getcwd(), "docs", "settings.ini")
        if not FileUtil.isExistFile(cls.config_file_path):
            raise FileNotFoundError("設定ファイルが存在しません (docs/settings.iniファイルを作成してください)")

        cls.config = configparser.ConfigParser()
        cls.config.read(cls.config_file_path, encoding="utf-8")
        cls.mode = "DEBUG" if cls.config["DEFAULT"].getboolean("debug_mode") else "DEFAULT"

    @classmethod
    def getWatchDogTargetPath(cls) -> str:
        return cls.config[cls.mode]["watchdog_target_path"]

    @classmethod
    def getArrangedOutputPath(cls) -> str:
        return cls.config[cls.mode]["arranged_output_path"]
