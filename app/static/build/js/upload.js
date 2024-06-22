document.addEventListener("DOMContentLoaded", function() {
  const dropzones = document.querySelectorAll('.upload__converter__grid');
  const fileInput = document.getElementById('fileInput');
  const uploadForm = document.getElementById('uploadForm');

  dropzones.forEach(dropzone => {
      dropzone.addEventListener('drop', (event) => {
          event.preventDefault(); 
          dropzone.classList.remove('dragover'); 

          var file = event.dataTransfer.files[0];
          fileInput.files = event.dataTransfer.files;

          var xhr = new XMLHttpRequest();
          xhr.open('POST', router, true);
          xhr.onload = function () {
              if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                const Toast = Swal.mixin({
                  toast: true,
                  position: "top-end",
                  showConfirmButton: false,
                  timer: 3000,
                  timerProgressBar: true,
                  didOpen: (toast) => {
                    toast.onmouseenter = Swal.stopTimer;
                    toast.onmouseleave = Swal.resumeTimer;
                  }
                });
                Toast.fire({
                  icon: "info",
                  title: "Uploading File..."
                }).then((result) =>{
                  console.log(response.redirect_url);
                  window.location.href = response.redirect_url;
                })
              } else {
                console.log(xhr.status);
                Swal.fire({
                  title: "Se produjo un Error",
                  text: 'No se admiten archivos diferentes al formato destino',
                  icon: "error"
                });
              }
          };

          var formData = new FormData(uploadForm);
          formData.append('file', file); 


          xhr.send(formData);

      });



      dropzone.addEventListener('dragover', (event) => {
        event.preventDefault();
        dropzone.classList.add('dragover'); 
      });
    

      dropzone.addEventListener('dragleave', () => {
        dropzone.classList.remove('dragover');
      });
    

      dropzone.addEventListener('drop', (event) => {
        event.preventDefault();
        dropzone.classList.remove('dragover');
      });
  });

  const fileButton = document.querySelector('.upload__converter__grid__file__button-click');
  fileButton.addEventListener('click', function() {
    fileInput.click();
  });

  fileInput.addEventListener('change', function(event) {
    event.preventDefault();
    const file = fileInput.files[0];
    fileInput.files = fileInput.files;

    var xhr = new XMLHttpRequest();
    xhr.open('POST', router, true);
    xhr.onload = function () {
        if (xhr.status === 200) {
          var response = JSON.parse(xhr.responseText);
          const Toast = Swal.mixin({
            toast: true,
            position: "top-end",
            showConfirmButton: false,
            timer: 3000,
            timerProgressBar: true,
            didOpen: (toast) => {
              toast.onmouseenter = Swal.stopTimer;
              toast.onmouseleave = Swal.resumeTimer;
            }
          });
          Toast.fire({
            icon: "info",
            title: "Uploading File..."
          }).then((result) =>{
            window.location.href = response.redirect_url;
          })


        } else {
          console.log(xhr.status);
          Swal.fire({
            title: "Se produjo un Error",
            text: 'No se admiten archivos diferentes al formato destino',
            icon: "error"
          });
        }
    };

    var formData = new FormData(uploadForm);
    formData.append('file', file); 

    xhr.send(formData);
  });
});
