function sortTableByValue(asc = true) {
  const tbody = document.getElementById('tableBody');                                   // Get the table body
  const rows = Array.from(tbody.querySelectorAll('tr'));                                // Get all rows in the table body
  rows.sort((a, b) => {                                                                 // Sort rows based on the value in the fourth column
    const valA = parseFloat(a.children[3].textContent.replace(/[^\d.-]/g, ''));         // Extract and parse the value from the fourth column of row A
    const valB = parseFloat(b.children[3].textContent.replace(/[^\d.-]/g, ''));         // Extract and parse the value from the fourth column of row B
    return asc ? valA - valB : valB - valA;                                             // Compare values for ascending or descending order
  });
  rows.forEach(row => tbody.appendChild(row));                                          // Re-append sorted rows to the table body
}

function sortTableByQuantity(asc = true) {                                              // Sort table rows based on the quantity in the third column
  const tbody = document.getElementById('tableBody');                                   // Get the table body
  const rows = Array.from(tbody.querySelectorAll('tr'));                                // Get all rows in the table body
  rows.sort((a, b) => {                                                                 // Sort rows based on the quantity in the third column
    const qtyA = parseInt(a.children[2].textContent);                                   // Extract and parse the quantity from the third column of row A
    const qtyB = parseInt(b.children[2].textContent);                                   // Extract and parse the quantity from the third column of row B
    return asc ? qtyA - qtyB : qtyB - qtyA;                                             // Compare quantities for ascending or descending order
  });
  rows.forEach(row => tbody.appendChild(row));                                          // Re-append sorted rows to the table body
}

document.getElementById('sortAsc').onclick = () => sortTableByValue(true);              // Sort by value in ascending order
document.getElementById('sortDesc').onclick = () => sortTableByValue(false);            // Sort by value in descending order
document.getElementById('sortQtyAsc').onclick = () => sortTableByQuantity(true);        // Sort by quantity in ascending order
document.getElementById('sortQtyDesc').onclick = () => sortTableByQuantity(false);      // Sort by quantity in descending order