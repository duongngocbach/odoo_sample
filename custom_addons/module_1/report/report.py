import base64
from datetime import datetime
import io
from odoo import models


class PatientCardXlsx(models.AbstractModel):
    _name = 'report.module_1.report_patient_id_card_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, patients):
        bold = workbook.add_format({'bold': True})
        format_1 = workbook.add_format({'bold': True, 'align': 'center', 'font_color': 'red', 'font_size': 16})
        date_format = workbook.add_format({'num_format': 'yyyy-mm-dd'})
        sheet = workbook.add_worksheet('value_list')
        # sheet.set_column('D:D', 12)
        # sheet.set_column('E:E', 13)
        sheet.write(0, 0, 'Date', bold)
        sheet.write(0, 1, datetime.today(), date_format)
        sheet.merge_range(1, 3, 2, 6, 'Tập đoàn Công nghiệp - Viễn thông Viettel', format_1)
        sheet.merge_range(3, 4, 4, 5, 'Ban Công nghệ thông tin', bold)
        sheet.merge_range(6, 4, 6, 5, 'Danh sách nhân viên', bold)
        fields = ['name', 'dob', 'value', 'value2', 'description']
        row = 8
        col = 1
        for f in fields:
          sheet.write(row, col, f, bold)
          col += 1
        row = 9
        col = 1
        for obj in patients:
          for f in fields:
            if f == 'dob':
              sheet.write(row, col, obj[f], date_format)
            else:
              sheet.write(row, col, obj[f])
            col += 1
          row += 1
          col = 1
            # row += 1
            # if obj.image:
            #     patient_image = io.BytesIO(base64.b64decode(obj.image))
            #     sheet.insert_image(row, col, "image.png", {'image_data': patient_image, 'x_scale': 0.5, 'y_scale': 0.5})

            #     row += 6
            # sheet.write(row, col, 'Name', bold)
            # sheet.write(row, col + 1, obj.name)
            # row += 1
            # sheet.write(row, col, 'value', bold)
            # sheet.write(row, col + 1, obj.value)
            # row += 1
            # sheet.write(row, col, 'description', bold)
            # sheet.write(row, col + 1, obj.description)

            # row += 2
            # sheet.merge_range(row, col, row + 1, col + 1, '', format_1)