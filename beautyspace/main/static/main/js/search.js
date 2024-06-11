document.addEventListener('DOMContentLoaded', function() {
    const searchButton = document.getElementById('searchButton');
    const searchInput = document.getElementById('searchInput');
    const dateInput = document.getElementById('dateInput');
    const recordContainers = document.querySelectorAll('.record');

    if (searchButton && searchInput && dateInput && recordContainers) {
        searchButton.addEventListener('click', function() {
            const query = searchInput.value.toLowerCase();
            const dateQuery = dateInput.value.toLowerCase();

            recordContainers.forEach(function(recordContainer) {
                const recordInfo = recordContainer.querySelector('.record-info');
                if (recordInfo) {
                    const serviceName = recordInfo.querySelector('b').innerText.toLowerCase();
                    const dateTime = recordInfo.querySelector('.date-time').innerText.toLowerCase();

                    if (serviceName.includes(query) && dateTime.includes(dateQuery)) {
                        recordContainer.style.display = 'flex';
                    } else {
                        recordContainer.style.display = 'none';
                    }
                }
            });
        });
    }
});
