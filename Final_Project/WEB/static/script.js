const groups = document.querySelectorAll('.carousel-group');                       // Select all groups in the carousel
let currentGroup = 0;                                                              // Current group index

function showGroup(index) {                                                        // Function to display the current group   
  groups.forEach((group, i) => {                                                   // Iterates over all groups
    group.style.display = i === index ? 'grid' : 'none';                           // Shows the current group and hides the others
  });
}

document.getElementById('prevButton').onclick = function() {                       // "Previous" button click event
  currentGroup = (currentGroup - 1 + groups.length) % groups.length;               // Updates the current group index, ensuring it stays within bounds
  showGroup(currentGroup);                                                         // Displays the updated group
};
document.getElementById('nextButton').onclick = function() {                       // "Next" button click event
  currentGroup = (currentGroup + 1) % groups.length;                               // Updates the current group index, ensuring it stays within bounds
  showGroup(currentGroup);                                                         // Displays the updated group
};

showGroup(currentGroup);                                                           // Initializes showing the first group               