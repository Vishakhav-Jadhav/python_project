const fs = require('fs');
const path = require('path');

// Replace with your actual username or use process.env.HOME for cross-platform
const desktopPath = path.join(process.env.HOME || process.env.USERPROFILE, 'Desktop', 'example.txt');

// Read the file
fs.readFile(desktopPath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading the file:', err);
    return;
  }
  console.log('File content:\n', data);
});