function handleFileUpload(input) {
    const file = input.files[0];
    if (file) {
        console.log('Selected file:', file.name);
    }
}

function toggleUrlInput() {
    const urlInput = document.getElementById("urlInput");
    const fileInputContainer = document.getElementById("fileInputContainer");
    const searchInput = document.getElementById("searchInput");
    const urlImageContainer = document.getElementById("urlImageContainer");
    const searchImageContainer = document.getElementById("searchImageContainer");

    urlInput.style.display = "block";
    fileInputContainer.style.display = "none";
    searchInput.style.display = "none";
    urlImageContainer.style.display = "block";
    searchImageContainer.style.display = "none"; // Hide the Search image
}

function toggleSearchInput() {
    const urlInput = document.getElementById("urlInput");
    const fileInputContainer = document.getElementById("fileInputContainer");
    const searchInput = document.getElementById("searchInput");
    const urlImageContainer = document.getElementById("urlImageContainer");
    const searchImageContainer = document.getElementById("searchImageContainer");

    urlInput.style.display = "none";
    fileInputContainer.style.display = "none";
    searchInput.style.display = "block";
    urlImageContainer.style.display = "none"; // Hide the URL image
    searchImageContainer.style.display = "block"; // Show the Search image
}

function showFileInput() {
    const urlInput = document.getElementById("urlInput");
    const fileInputContainer = document.getElementById("fileInputContainer");
    const searchInput = document.getElementById("searchInput");
    const urlImageContainer = document.getElementById("urlImageContainer");
    const searchImageContainer = document.getElementById("searchImageContainer");

    urlInput.style.display = "none";
    fileInputContainer.style.display = "block";
    searchInput.style.display = "none";
    urlImageContainer.style.display = "none"; // Hide the URL image
    searchImageContainer.style.display = "none"; // Hide the Search image
}