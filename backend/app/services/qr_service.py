from pathlib import Path

import qrcode


class QRService:

    QR_DIRECTORY = Path("storage/qr_codes")

    @staticmethod
    def generate(ticket_number: str) -> str:
        """
        Generate a QR code for a ticket.
        Returns the saved image path.
        """

        QRService.QR_DIRECTORY.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_path = (
            QRService.QR_DIRECTORY /
            f"{ticket_number}.png"
        )

        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4,
        )

        qr.add_data(ticket_number)
        qr.make(fit=True)

        image = qr.make_image(
            fill_color="black",
            back_color="white",
        )

        image.save(file_path)

        return str(file_path)