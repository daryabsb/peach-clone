// Custom Admin JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Sidebar Toggle
    const toggleSidebarBtn = document.getElementById('toggle-sidebar');
    const body = document.body;
    
    if (toggleSidebarBtn) {
        toggleSidebarBtn.addEventListener('click', function() {
            body.classList.toggle('sidebar-collapsed');
            
            // Save preference to localStorage
            const isCollapsed = body.classList.contains('sidebar-collapsed');
            localStorage.setItem('sidebar_collapsed', isCollapsed);
            
            // If we have an API endpoint for saving user preferences
            if (typeof updateUserPreference === 'function') {
                updateUserPreference('sidebar_collapsed', isCollapsed);
            }
        });
    }
    
    // Initialize sidebar state from localStorage
    const sidebarCollapsed = localStorage.getItem('sidebar_collapsed');
    if (sidebarCollapsed === 'true') {
        body.classList.add('sidebar-collapsed');
    }
    
    // Mobile Sidebar Toggle
    const mobileToggleBtn = document.getElementById('mobile-toggle-sidebar');
    const sidebar = document.querySelector('.sidebar');
    
    if (mobileToggleBtn && sidebar) {
        mobileToggleBtn.addEventListener('click', function() {
            sidebar.classList.toggle('show');
        });
        
        // Close sidebar when clicking outside on mobile
        document.addEventListener('click', function(event) {
            const isClickInsideSidebar = sidebar.contains(event.target);
            const isClickOnToggleBtn = mobileToggleBtn.contains(event.target);
            
            if (!isClickInsideSidebar && !isClickOnToggleBtn && sidebar.classList.contains('show')) {
                sidebar.classList.remove('show');
            }
        });
    }
    
    // Theme Toggle
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    
    if (themeToggleBtn && themeIcon) {
        themeToggleBtn.addEventListener('click', function() {
            const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            
            // Update icon
            if (newTheme === 'dark') {
                themeIcon.classList.remove('fa-moon');
                themeIcon.classList.add('fa-sun');
            } else {
                themeIcon.classList.remove('fa-sun');
                themeIcon.classList.add('fa-moon');
            }
            
            // If we have an API endpoint for saving user preferences
            if (typeof updateUserPreference === 'function') {
                updateUserPreference('theme', newTheme);
            }
        });
    }
    
    // Initialize theme from localStorage
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.documentElement.setAttribute('data-theme', savedTheme);
        
        // Update icon based on saved theme
        if (themeIcon) {
            if (savedTheme === 'dark') {
                themeIcon.classList.remove('fa-moon');
                themeIcon.classList.add('fa-sun');
            } else {
                themeIcon.classList.remove('fa-sun');
                themeIcon.classList.add('fa-moon');
            }
        }
    }
    
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    if (typeof bootstrap !== 'undefined') {
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
    
    // Initialize popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    if (typeof bootstrap !== 'undefined') {
        popoverTriggerList.map(function (popoverTriggerEl) {
            return new bootstrap.Popover(popoverTriggerEl);
        });
    }
    
    // Initialize transaction chart on dashboard
    const chartCanvas = document.getElementById('transactionChart');
    if (chartCanvas && typeof Chart !== 'undefined') {
        // Get transaction data from the table
        const transactionTable = document.querySelector('.transaction-table');
        if (transactionTable) {
            const rows = transactionTable.querySelectorAll('tbody tr');
            const labels = [];
            const counts = [];
            const colors = [];
            
            // Default colors for transaction types
            const typeColors = {
                'Invoices': '#4e73df',
                'Sales': '#1cc88a',
                'Purchases': '#e74a3b',
                'Payments': '#36b9cc',
                'Receives': '#f6c23e'
            };
            
            rows.forEach(row => {
                const typeCell = row.querySelector('td:first-child');
                const countCell = row.querySelector('td:nth-child(2)');
                
                if (typeCell && countCell && !row.querySelector('td[colspan]')) {
                    const type = typeCell.textContent.trim();
                    const count = parseInt(countCell.textContent.trim(), 10) || 0;
                    
                    if (count > 0) {
                        labels.push(type);
                        counts.push(count);
                        colors.push(typeColors[type] || '#858796');
                    }
                }
            });
            
            // Create the chart
            const ctx = chartCanvas.getContext('2d');
            const transactionChart = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: labels,
                    datasets: [{
                        data: counts,
                        backgroundColor: colors,
                        hoverBackgroundColor: colors,
                        hoverBorderColor: 'rgba(234, 236, 244, 1)',
                    }]
                },
                options: {
                    maintainAspectRatio: false,
                    tooltips: {
                        backgroundColor: 'rgb(255,255,255)',
                        bodyFontColor: '#858796',
                        borderColor: '#dddfeb',
                        borderWidth: 1,
                        xPadding: 15,
                        yPadding: 15,
                        displayColors: false,
                        caretPadding: 10,
                    },
                    legend: {
                        display: true,
                        position: 'bottom'
                    },
                    cutoutPercentage: 70,
                },
            });
            
            // Toggle between chart and table view
            const toggleButton = document.getElementById('toggle-chart-view');
            const chartContainer = document.querySelector('.chart-container');
            
            if (toggleButton && chartContainer) {
                toggleButton.addEventListener('click', function() {
                    if (chartContainer.style.display === 'none') {
                        chartContainer.style.display = 'block';
                        transactionTable.style.display = 'none';
                        toggleButton.innerHTML = '<i class="fas fa-table me-1"></i> Show Table';
                    } else {
                        chartContainer.style.display = 'none';
                        transactionTable.style.display = 'block';
                        toggleButton.innerHTML = '<i class="fas fa-chart-pie me-1"></i> Show Chart';
                    }
                });
            }
        }
    }
    
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            if (alert.parentNode) {
                if (typeof bootstrap !== 'undefined' && bootstrap.Alert) {
                    const bsAlert = new bootstrap.Alert(alert);
                    bsAlert.close();
                } else {
                    alert.style.opacity = '0';
                    setTimeout(function() {
                        if (alert.parentNode) {
                            alert.parentNode.removeChild(alert);
                        }
                    }, 500);
                }
            }
        }, 5000);
    });
    
    // Items per page selector
    const itemsPerPageSelect = document.getElementById('items-per-page');
    if (itemsPerPageSelect) {
        itemsPerPageSelect.addEventListener('change', function() {
            const value = this.value;
            const currentUrl = new URL(window.location.href);
            currentUrl.searchParams.set('per_page', value);
            window.location.href = currentUrl.toString();
            
            // If we have an API endpoint for saving user preferences
            if (typeof updateUserPreference === 'function') {
                updateUserPreference('items_per_page', value);
            } else {
                localStorage.setItem('items_per_page', value);
            }
        });
    }
    
    // Initialize items per page from localStorage if not set in URL
    const urlParams = new URLSearchParams(window.location.search);
    if (itemsPerPageSelect && !urlParams.has('per_page')) {
        const savedItemsPerPage = localStorage.getItem('items_per_page');
        if (savedItemsPerPage) {
            itemsPerPageSelect.value = savedItemsPerPage;
        }
    }
    
    // Confirm delete actions
    const deleteButtons = document.querySelectorAll('.btn-delete:not([data-bs-toggle="modal"])');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item? This action cannot be undone.')) {
                e.preventDefault();
            }
        });
    });
    
    // Print button
    const printButton = document.getElementById('print-page');
    if (printButton) {
        printButton.addEventListener('click', function() {
            window.print();
        });
    }
    
    // Export button (CSV)
    const exportCsvButton = document.getElementById('export-csv');
    if (exportCsvButton) {
        exportCsvButton.addEventListener('click', function() {
            const table = document.querySelector('table');
            if (!table) return;
            
            let csv = [];
            const rows = table.querySelectorAll('tr');
            
            for (let i = 0; i < rows.length; i++) {
                const row = [], cols = rows[i].querySelectorAll('td, th');
                
                for (let j = 0; j < cols.length; j++) {
                    // Get the text content and clean it
                    let data = cols[j].innerText.replace(/(
\n|\n|\r)/gm, '').replace(/\s+/g, ' ');
                    // Escape double quotes
                    data = data.replace(/"/g, '""');
                    // Add quotes around the data
                    row.push('"' + data + '"');
                }
                csv.push(row.join(','));
            }
            
            const csvString = csv.join('\n');
            const filename = 'export_' + new Date().toISOString().slice(0, 10) + '.csv';
            const link = document.createElement('a');
            link.style.display = 'none';
            link.setAttribute('target', '_blank');
            link.setAttribute('href', 'data:text/csv;charset=utf-8,' + encodeURIComponent(csvString));
            link.setAttribute('download', filename);
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        });
    }
    
    // Function to update user preferences via API
    window.updateUserPreference = function(key, value) {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value;
        if (!csrfToken) return;
        
        fetch('/custom-admin/api/preferences/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({
                key: key,
                value: value
            })
        }).catch(function(error) {
            console.error('Error updating preference:', error);
        });
    };
    
    // Search form with debounce
    const searchInput = document.querySelector('input[name="search"]');
    if (searchInput) {
        let debounceTimer;
        const debounceDelay = 500; // ms
        
        searchInput.addEventListener('input', function() {
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(function() {
                const form = searchInput.closest('form');
                if (form) {
                    form.submit();
                }
            }, debounceDelay);
        });
    }
    
    // Date range picker initialization
    const dateRangePicker = document.getElementById('date-range-picker');
    if (dateRangePicker && typeof flatpickr !== 'undefined') {
        flatpickr(dateRangePicker, {
            mode: 'range',
            dateFormat: 'Y-m-d',
            onChange: function(selectedDates, dateStr) {
                if (selectedDates.length === 2) {
                    const startDate = selectedDates[0].toISOString().split('T')[0];
                    const endDate = selectedDates[1].toISOString().split('T')[0];
                    
                    const currentUrl = new URL(window.location.href);
                    currentUrl.searchParams.set('start_date', startDate);
                    currentUrl.searchParams.set('end_date', endDate);
                    window.location.href = currentUrl.toString();
                }
            }
        });
    }
    
    // Initialize transaction filters
    const filterLinks = document.querySelectorAll('[data-filter]');
    const transactionRows = document.querySelectorAll('.transaction-row');
    
    if (filterLinks.length > 0 && transactionRows.length > 0) {
        filterLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                
                // Remove active class from all filter links
                filterLinks.forEach(l => l.classList.remove('active'));
                
                // Add active class to clicked link
                this.classList.add('active');
                
                const filterValue = this.getAttribute('data-filter');
                
                // Show/hide rows based on filter
                transactionRows.forEach(row => {
                    if (filterValue === 'all' || row.getAttribute('data-type') === filterValue) {
                        row.style.display = '';
                    } else {
                        row.style.display = 'none';
                    }
                });
            });
        });
    }
});