document.addEventListener('DOMContentLoaded', function () {
    const toggle = document.querySelector('.menu-toggle');
    const sidebar = document.querySelector('.sidebar');
    if (toggle && sidebar) {
        toggle.addEventListener('click', function () {
            sidebar.classList.toggle('open');
        });
    }

    const facilitySelect = document.querySelector('#facility_id');
    const address = document.querySelector('#hospital-address');
    if (facilitySelect && address) {
        facilitySelect.addEventListener('change', function () {
            const option = facilitySelect.options[facilitySelect.selectedIndex];
            address.textContent = option.dataset.address || 'Select a facility';
        });
    }
});

function confirmDelete() {
    return window.confirm('Are you sure you want to delete this facility?\n\nThis action cannot be undone.');
}
