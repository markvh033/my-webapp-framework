function showNotification(message, isError = false) {
    var notificationBar = document.getElementById('simple_notification_bar');
    notificationBar.textContent = message;
    notificationBar.classList.add('show');
    // Remove any previous error or success class
    notificationBar.classList.remove('error', 'success');

    // Add the error class if isError is true, otherwise add the success class
    if (isError) {
        notificationBar.classList.add('error');
    } else {
        notificationBar.classList.add('success');
    }

    // Hide the notification bar after 3 seconds
    setTimeout(function() {
        notificationBar.classList.remove('show');
    }, 3000);
}