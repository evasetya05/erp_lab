import os
import django
import csv

# Ganti dengan path ke settings.py proyekmu
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dev_env.settings')
django.setup()

from ledger.models import Account

def import_accounts_from_csv(csv_path):
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Account.objects.create(
                account_type=row['Account Type'],
                account_name=row['Account Name'],
                coa=row['CoA'],
                balance_type=row['Balance Type'],
                active=(row['Active'].strip().lower() == 'true'),
                locked=(row['Locked'].strip().lower() == 'true'),
                coa_role_default=row['CoA Role Default'] or None
            )
    print("✅ Import selesai.")

if __name__ == '__main__':
    # Ganti path ini jika file CSV disimpan di lokasi lain
    csv_file_path = 'C:/full_chart_of_accounts.csv'
    import_accounts_from_csv(csv_file_path)
