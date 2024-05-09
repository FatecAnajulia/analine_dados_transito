const fs = require('fs');
const csv = require('csv-parser');

const results = [];

fs.createReadStream('data.csv')
  .pipe(csv())
  .on('data', (data) => results.push(data))
  .on('end', () => {
    console.log(results);
    // Aqui você pode fazer o que quiser com os dados, como processá-los ou exibi-los.
  });
