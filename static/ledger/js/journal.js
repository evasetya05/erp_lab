function addEntry() {
    const row = document.querySelector('.entry').cloneNode(true);

    // Reset semua input
    row.querySelectorAll('input').forEach(input => {
        if (input.name.includes('debit') || input.name.includes('credit')) {
            input.value = 0;
        } else {
            input.value = '';
        }
    });

    // Tambahkan event listener pada tombol hapus
    const removeButton = row.querySelector('button');
    removeButton.onclick = function () {
        removeEntry(this);
    };

    document.getElementById('entries').appendChild(row);
}

function removeEntry(button) {
    const row = button.closest('tr');
    const rows = document.querySelectorAll('#entries .entry');

    if (rows.length > 1) {
        row.remove();
    } else {
        alert('Minimal satu baris jurnal diperlukan.');
    }
}

function validateJournal() {
    const debits = document.querySelectorAll('input[name="debit[]"]');
    const credits = document.querySelectorAll('input[name="credit[]"]');

    let totalDebit = 0, totalCredit = 0;

    for (let i = 0; i < debits.length; i++) {
        totalDebit += parseFloat(debits[i].value) || 0;
        totalCredit += parseFloat(credits[i].value) || 0;
    }

    if (totalDebit.toFixed(2) !== totalCredit.toFixed(2)) {
        alert('Total debit dan kredit harus seimbang!');
        return false;
    }
    return true;
}
