import json
import os

from docx2pdf import convert
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm

CONTRACTEE = "CONTRACTEE NAME"
ESIG = "resources/alex-esig.png"
ESIG_WIDTH = 40 #mm
ESIG_HEIGHT = 25 #mm
POSITION = "Junior Test Position"


def get_accomplishments(filename):
    with open(filename) as js:
        return json.load(js)


def create_cwa(accomplishments):
    for accom_period in accomplishments:
        doc = DocxTemplate("templates/cert-of-work-accomplishment_template.docx")
        print(accom_period)
        split_period = accom_period.split()
        last_day = split_period[1].split("-")[1].strip(",")

        # Add signature img
        esig = InlineImage(
            doc, image_descriptor=ESIG, width=Mm(40), height=Mm(20)
        )
        context = {
            "position": POSITION,
            "period": accom_period,  # Date is the default key
            "accom_day": f"{last_day}st" if last_day == "31" else f"{last_day}th",
            "accom_month": f"{split_period[0]} {split_period[2]}",
            "accomplishments": accomplishments[accom_period],
            "contractee": CONTRACTEE,
            "esig": esig
        }

        doc.render(context)
        doc.save(
            f"outputs/CWA_{CONTRACTEE.split()[-1]}_{split_period[0]}_{last_day}.docx"
        )

def main():
    os.makedirs('outputs/', exist_ok=True)
    accomplishments = get_accomplishments("accomplishments.json")
    create_cwa(accomplishments)


if __name__ == "__main__":
    main()
    convert("outputs/") # Convert .docx files in the output directory
