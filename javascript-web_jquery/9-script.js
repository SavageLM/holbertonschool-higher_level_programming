$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (helloData) => {
  $('DIV#hello').text(helloData.hello);
});
