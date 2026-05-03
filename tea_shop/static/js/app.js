// App.js - Main JavaScript utilities

document.addEventListener('DOMContentLoaded', function() {
    console.log('Tea Shop Manager loaded');
});

// Get CSRF token from DOM
function getCsrfToken() {
    return document.querySelector('[name=csrftoken]')?.value || '';
}

// Format currency
function formatCurrency(amount) {
    return '₱' + parseFloat(amount).toFixed(2);
}

// Format date
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-PH') + ' ' + date.toLocaleTimeString('en-PH', {hour: '2-digit', minute: '2-digit'});
}

// Show notification
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type}`;
    notification.textContent = message;
    notification.style.position = 'fixed';
    notification.style.top = '10px';
    notification.style.right = '10px';
    notification.style.zIndex = '9999';
    notification.style.minWidth = '250px';
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 3000);
}
