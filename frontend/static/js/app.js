// Function to fetch and display inventory items
function loadInventory() {
    fetch('/inventory/')
        .then(response => response.json())
        .then(data => {
            const inventoryList = document.getElementById('inventory-list');
            inventoryList.innerHTML = '';  // Clear existing items
            data.forEach(item => {
                const listItem = `<li>${item.name}: ${item.quantity}</li>`;
                inventoryList.innerHTML += listItem;
            });
        });
}

// Function to handle form submission
document.getElementById('updateForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const itemName = document.getElementById('name').value;
    const itemQuantity = document.getElementById('quantity').value;

    fetch('/update_inventory/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: itemName, quantity: itemQuantity }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        loadInventory();  // Refresh the inventory list after update
    });
});

// Load inventory when the page loads
window.onload = loadInventory;