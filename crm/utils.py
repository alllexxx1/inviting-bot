import os

from crm.db import fetch_users

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def prepare_user_data(txt=False):
    users = fetch_users()
    users_number = 0

    if users:
        report_content = 'Пользователи\n'
        report_content += '=' * 20 + '\n'
        for user in users:
            users_number += 1
            user_id, telegram_user_id, username, full_name, created_at, eligibility = user
            report_content += f'ID: {user_id}\n'
            report_content += f'User ID: {telegram_user_id}\n'
            report_content += f'Username: {username or "N/A"}\n'
            report_content += f'Full Name: {full_name or "N/A"}\n'
            report_content += f'Eligibility: {str(eligibility)}\n'
            report_content += '\n\n'
        report_content += f'Всего пользователей: {users_number}'
        if txt:
            file_path = os.path.join(BASE_DIR, 'crm', 'users_report.txt')
            with open(file_path, "w") as file:
                file.write(report_content)
            return file_path
        elif not txt:
            return report_content

    else:
        return None
