
fetch('https://dev.shepherd.appoly.io/fruit.jsons')
  .then(response => response.json())
  .then(data => console.log(JSON.stringify(data)))

