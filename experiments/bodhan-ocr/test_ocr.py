import sys
sys.path.insert(0, "model")

from indic_ocr import IndicOCR

ocr = IndicOCR.from_pretrained(
    "model",
    device="mps",
)
result = ocr.parse("sample.png")
print(result)