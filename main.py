import json

from docxtpl import DocxTemplate

CONTRACTEE = "CONTRACTEE NAME"
POSITION = "Junior Test Position"


def get_accomplishments(filename):
    with open(filename) as js:
        return json.load(js)


def create_cwa(accomplishments):
    doc = DocxTemplate("templates/cert-of-work-accomplishment_template.docx")
    for accom_period in accomplishments:
        print(accom_period)
        split_period = accom_period.split()
        last_day = split_period[1].split("-")[1].strip(",")

        context = {
            "position": POSITION,
            "period": accom_period,  # Date is the default key
            "accom_day": f"{last_day}st" if last_day == "31" else f"{last_day}th",
            "accom_month": f"{split_period[0]} {split_period[2]}",
            "accomplishments": accomplishments[accom_period],
            "contractee": CONTRACTEE,
        }

        doc.render(context)
        doc.save(
            f"outputs/CWA_{CONTRACTEE.split()[-1]}_{split_period[0]}_{last_day}.docx"
        )


if __name__ == "__main__":
    accomplishments = get_accomplishments("accomplishments.json")
    create_cwa(accomplishments)
