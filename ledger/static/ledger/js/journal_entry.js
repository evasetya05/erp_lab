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

    // Tambahkan event listener
    row.querySelector('input[name="debit[]"]').addEventListener('input', updateTotals);
    row.querySelector('input[name="credit[]"]').addEventListener('input', updateTotals);

    // Tombol hapus
    const removeButton = row.querySelector('button');
    removeButton.onclick = function () {
        removeEntry(this);
    };

    document.getElementById('entries').appendChild(row);
    updateTotals();
}

function removeEntry(button) {
    const row = button.closest('tr');
    const rows = document.querySelectorAll('#entries .entry');

    if (rows.length > 1) {
        row.remove();
        updateTotals();
    } else {
        alert('Minimal satu baris jurnal diperlukan.');
    }
}

function updateTotals() {
    const debits = document.querySelectorAll('input[name="debit[]"]');
    const credits = document.querySelectorAll('input[name="credit[]"]');

    let totalDebit = 0, totalCredit = 0;

    debits.forEach(input => {
        totalDebit += parseFloat(input.value) || 0;
    });
    credits.forEach(input => {
        totalCredit += parseFloat(input.value) || 0;
    });

    document.getElementById('total-debit').innerText = totalDebit.toFixed(2);
    document.getElementById('total-credit').innerText = totalCredit.toFixed(2);
    
    // Optional: tampilkan peringatan real-time jika tidak balance
    const warning = document.getElementById('balance-warning');
    if (Math.abs(totalDebit - totalCredit) > 0.009) {
        warning.style.display = 'block';
    } else {
        warning.style.display = 'none';
    }
}

function validateJournal() {
    const totalDebit = parseFloat(document.getElementById('total-debit').innerText) || 0;
    const totalCredit = parseFloat(document.getElementById('total-credit').innerText) || 0;

    if (totalDebit.toFixed(2) !== totalCredit.toFixed(2)) {
        alert('Total debit dan kredit harus seimbang!');
        return false;
    }
    return true;
}

// Inisialisasi listener awal
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('input[name="debit[]"]').forEach(input => {
        input.addEventListener('input', updateTotals);
    });
    document.querySelectorAll('input[name="credit[]"]').forEach(input => {
        input.addEventListener('input', updateTotals);
    });
    updateTotals();
});
