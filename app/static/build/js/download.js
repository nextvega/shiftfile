document.addEventListener("DOMContentLoaded", function() {
  let downloadButton = document.getElementById('downloadFile')
  
  function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }
  const csrftoken = getCookie('csrftoken')

  downloadButton.addEventListener('click', function(e){
    e.preventDefault()
    if(tokenDocument){
      fetch(router, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(
          { 
            token: tokenDocument,
            format: formatDocument,
            name_file: nameDocument
          }) 
      })
      .then(response => {
        if (response.ok) {
          return response.json(); 
        } else {
          console.error('Error al enviar token');
        }
      })
      .then(data => {
        const link = document.createElement('a');
        link.href = 'data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,' + data.file_content_base64;
        link.download = data.file_name;
      
        document.body.appendChild(link);
        link.click();

        document.body.removeChild(link);
      })
      .catch(error => {
        Swal.fire({
          title: "Se produjo un Error",
          text: error,
          icon: "error"
        });
      });
    }else{
      Swal.fire({
        title: "Se produjo un Error",
        text: 'No existe ningun documento que descargar',
        icon: "error"
      });
    }
  })

});
