from pandas import read_csv, concat


def get_dataframe(directory):
    return concat(map(read_csv, directory.iterdir())).astype(
        {
            "chapter": "int",
            "verse": "int",
            "word": "string",
        }
    )
