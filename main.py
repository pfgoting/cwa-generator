import json
import logging
import os
import subprocess

from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage
from dotenv import load_dotenv

load_dotenv()
CONTRACTEE = os.getenv("CONTRACTEE_NAME", "Alexander Hamilton")
ESIG = os.getenv("ESIG_LOCATION", "resources/alex-esig.png")
ESIG_WIDTH = int(os.getenv("ESIG_WIDTH_MM", 40))  # mm
ESIG_HEIGHT = int(os.getenv("ESIG_HEIGHT_MM", 25))  # mm
POSITION = os.getenv("POSITION", "Junior Test Position")
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def get_accomplishments(filename):
    with open(filename) as js:
        return json.load(js)


def create_cwa(accomplishments):
    for accom_period in accomplishments:
        doc = DocxTemplate("templates/cert-of-work-accomplishment_template.docx")
        split_period = accom_period.split()
        last_day = split_period[1].split("-")[1].strip(",")

        output_file = (
            f"outputs/CWA_{CONTRACTEE.split()[-1]}"
            + f"_{split_period[0]}_{last_day}.docx"
        )

        if not os.path.isfile(output_file):
            # Add signature img
            esig = InlineImage(
                doc, image_descriptor=ESIG, width=Mm(ESIG_WIDTH), height=Mm(ESIG_HEIGHT)
            )
            context = {
                "position": POSITION,
                "period": accom_period,  # Date is the default key
                "accom_day": f"{last_day}st" if last_day == "31" else f"{last_day}th",
                "accom_month": f"{split_period[0]} {split_period[2]}",
                "accomplishments": accomplishments[accom_period],
                "contractee": CONTRACTEE,
                "esig": esig,
            }

            doc.render(context)
            doc.save(output_file)
            logging.info(accom_period)


def convert_docs(output_folder):
    """
    Converts docx files in a folder if there is no existing PDF
    for that file.
    """
    for file in (directory := os.listdir(output_folder)):
        if file.endswith(".docx"):
            if not (pdf_name := f"{file[:-5]}.pdf") in directory:
                logging.info("Generating PDF for %s", file)
                # convert(file, pdf_name)
                # Calling of the CLI for docx2pdf is used since using
                # the imported convert function for individual file
                # conversion raises an exception.
                process = subprocess.Popen(
                    [
                        "pipenv",
                        "run",
                        "docx2pdf",
                        "--keep-active",
                        f"{output_folder.strip('/')}/{file}",
                        f"{output_folder.strip('/')}/{pdf_name}",
                    ],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                stdout, stderr = process.communicate()
                # print(stdout, stderr)


def main():
    os.makedirs("outputs/", exist_ok=True)
    accomplishments = get_accomplishments("accomplishments.json")
    create_cwa(accomplishments)


if __name__ == "__main__":
    main()
    convert_docs("outputs/")  # Convert .docx files in the output directory
