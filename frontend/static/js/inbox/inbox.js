
async function fetchAndLoadMessages() {
    try {
        const response = await fetch('/get-messages');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data; // Adjust this line based on the actual structure
    } catch (error) {
        console.error('There has been a problem with your fetch operation:', error);
        return []; // Return an empty array in case of error
    }
}


async function markAsRead(messageId) {
    const response = await fetch(`/mark-as-read/${messageId}`, { method: 'POST' });
    if (response.ok) {
        // Remove the blue dot indicator and move the message to the read section
        const messageElement = document.getElementById(`message-${messageId}`);
        messageElement.querySelector('.unread-indicator').style.display = 'none';
        document.getElementById('read-messages').appendChild(messageElement);
    }
}

// Function to delete a message
async function deleteMessage(messageId) {
    const response = await fetch(`/delete-message/${messageId}`, { method: 'POST' });
    if (response.ok) {
        // Move the message to the deleted section
        const messageElement = document.getElementById(`message-${messageId}`);
        document.getElementById('deleted-messages').appendChild(messageElement);
    }
}

// Function to expand or collapse a message content
function toggleMessageContent(messageId) {
    const contentElement = document.getElementById(`content-${messageId}`);
    const isExpanded = contentElement.getAttribute('data-expanded') === 'true';

    // Check if the content is expanded or not and toggle the state
    if (isExpanded) {
        // Collapse the content
        const previewContent = contentElement.getAttribute('data-preview-content');
        contentElement.textContent = previewContent; // Use textContent for plain text
        contentElement.setAttribute('data-expanded', 'false');
    } else {
        // Expand the content
        const fullContent = contentElement.getAttribute('data-full-content');
        contentElement.textContent = fullContent; // Use textContent for plain text
        contentElement.setAttribute('data-expanded', 'true');
    }

    // Update the button text
    const toggleButton = contentElement.previousElementSibling.querySelector('.toggle-content-btn');
    toggleButton.textContent = isExpanded ? 'Expand' : 'Collapse';
}



// Function to load messages into the page
function loadMessages(messages) {
    messages.forEach(message => {
        const messageElement = document.createElement('div');
        messageElement.id = `message-${message._id}`;
        messageElement.className = 'message';
        messageElement.style = 'background-color: white; padding: 16px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 8px;';

        const isLongMessage = message.message.content.length > 50;
        const previewContent = isLongMessage ? message.message.content.substring(0, 50) + '...' : message.message.content;

        messageElement.innerHTML = `
            <div class="message-header" style="display: flex; justify-content: space-between; align-items: center;">
                <span class="message-title" style="font-weight: bold;">${message.message_title}</span>
                <div style="display: flex; align-items: center;">
                    ${isLongMessage ? `<button class="toggle-content-btn" style="color: blue; margin-right: 8px;">Expand</button>` : ''}
                    <button onclick="markAsRead('${message._id}')" style="color: blue; margin-right: 8px;">Mark as Read</button>
                    <button onclick="deleteMessage('${message._id}')" style="color: red;">Delete</button>
                </div>
            </div>
            <div id="content-${message._id}" class="message-content" style="margin-top: 8px; color: #333;" data-full-content="${message.message.content}" data-preview-content="${previewContent}" data-expanded="false">
                ${previewContent}
            </div>
        `;

        const targetDiv = message.has_been_deleted ? 'deleted-messages' : message.has_been_read ? 'read-messages' : 'unread-messages';
        document.getElementById(targetDiv).appendChild(messageElement);
    });

    document.querySelectorAll('.toggle-content-btn').forEach(button => {
        button.addEventListener('click', function() {
            const messageContent = this.parentNode.parentNode.nextElementSibling;
            const isExpanded = messageContent.getAttribute('data-expanded') === 'true';
            messageContent.innerText = isExpanded ? messageContent.getAttribute('data-preview-content') : messageContent.getAttribute('data-full-content');
            this.innerText = isExpanded ? 'Expand' : 'Collapse';
            messageContent.setAttribute('data-expanded', !isExpanded);
        });
    });
}




document.addEventListener('DOMContentLoaded', function() {
    fetchAndLoadMessages().then(messages => {
        console.log('Type of messages:', typeof messages);
        console.log('Content of messages:', messages);
        if (Array.isArray(messages)) {
            loadMessages(messages);
        } else {
            console.error('Messages is not an array:', messages);
        }
    }).catch(error => {
        console.error('Failed to load messages:', error);
});
});


