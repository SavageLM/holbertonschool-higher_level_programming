$.get('https://swapi-api.hbtn.io/api/people/5/?format=json',(nameData) => {
    $('DIV#character').text(nameData.name);
  });
