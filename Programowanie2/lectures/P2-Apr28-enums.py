# ------------------ Enums
from enum import Enum

class DataFormatType(Enum):
    TSV = "tsv"
    CSV = "csv"
    XLSX = "xlsx"

class CompressionType(Enum):
    NONE = 0
    ZIP = 1
    GZIP = 2

def csv_export(_fname: str): pass

def tsv_export(_fname: str): pass

def xlsx_export(_fname: str): pass

def export_data(fname:str, format: DataFormatType,
                _compression: CompressionType, _mode: int):

    print(format.name)
    print(format.value)
    match format:
        case DataFormatType.TSV:
            csv_export(fname)
        case DataFormatType.CSV:
            tsv_export(fname)

export_data("wyniki.tsv", DataFormatType.TSV, CompressionType.NONE, 1)

class ExportFormat(Enum):
    CSV = "csv"
    JSON = "json"
    TSV = "tsv"
    JPG = ["jpg", "jpeg"]

print(ExportFormat.CSV)
print(ExportFormat.CSV.name)
print(ExportFormat.CSV.value)
print(ExportFormat.JPG.value)