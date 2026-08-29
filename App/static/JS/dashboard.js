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

    const providerDataScript = document.querySelector('#provider-address-data');
    if (providerDataScript) {
        try {
            const providerData = JSON.parse(providerDataScript.textContent || '[]');
            const savedProviderNames = {};

            providerData.forEach(function (entry) {
                const providerKey = (entry.provider || '').trim();
                const addressText = (entry.address || '').trim();
                const nameText = (entry.name || '').trim();
                if (!providerKey || !addressText || !nameText) {
                    return;
                }
                if (!savedProviderNames[providerKey]) {
                    savedProviderNames[providerKey] = {};
                }
                savedProviderNames[providerKey][addressText.toLowerCase()] = nameText;
            });

            document.querySelectorAll('textarea[data-name-field], input[data-name-field]').forEach(function (addressField) {
                const nameFieldName = addressField.dataset.nameField;
                if (!nameFieldName) {
                    return;
                }

                const nameField = document.querySelector('[name="' + nameFieldName + '"]');
                if (!nameField) {
                    return;
                }

                const providerKey = nameFieldName.replace(/_name$/, '');
                const fillSavedName = function () {
                    const enteredAddress = (addressField.value || '').trim();
                    if (!enteredAddress) {
                        return;
                    }

                    const recommendedName = savedProviderNames[providerKey] && savedProviderNames[providerKey][enteredAddress.toLowerCase()];
                    if (recommendedName && (!nameField.value || nameField.value.trim() === '')) {
                        nameField.value = recommendedName;
                    }
                };

                addressField.addEventListener('change', fillSavedName);
                addressField.addEventListener('input', fillSavedName);
            });
        } catch (error) {
            console.warn('Unable to parse saved provider address recommendations.', error);
        }
    }
});

function confirmDelete() {
    return window.confirm('Are you sure you want to delete this facility?\n\nThis action cannot be undone.');
}
