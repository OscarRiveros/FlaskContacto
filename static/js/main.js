const btnDeletes = document.querySelectorAll('.btn-delete')

if (btnDeletes) {
    const btnArray = Array.from(btnDeletes);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if (!confirm('Estas seguro de querer eliminarlo?')) {
                e.preventDefault();
            }
        });
    });
}