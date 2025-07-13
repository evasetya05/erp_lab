from django.db import models
from django.utils import timezone
from .account import Account  # ✅ impor langsung dari file account.py

class JournalEntry(models.Model):
    date = models.DateField(default=timezone.now)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_posted = models.BooleanField(default=False)  # Tambahan

    def __str__(self):
        return f"{self.date} - {self.description[:30]}"

class JournalItem(models.Model):
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, related_name='items')
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    debit = models.IntegerField(default=0)   # ubah dari DecimalField
    credit = models.IntegerField(default=0)  # ubah dari DecimalField
    note = models.CharField(max_length=255, blank=True, null=True)  # 🆕 Tambahkan keterangan akun

    def __str__(self):
        return f"{self.journal_entry.date} - {self.account.account_name}: D {self.debit} / C {self.credit}"
