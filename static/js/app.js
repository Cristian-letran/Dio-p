$(document).foundation()


$('[data-open-details]').click(function (e) {
    e.preventDefault();
    $(this).next().toggleClass('is-active');
    $(this).toggleClass('is-active');
  });
  
  const funcionInit = () => {
    if (!"geolocation" in navigator) {
      return alert("Tu navegador no soporta el acceso a la ubicación. Intenta con otro");
    }
  
    const $id_latitud = document.querySelector("#id_latitud"),
      $id_longitud = document.querySelector("#id_longitud"),
      $enlace = document.querySelector("#enlace");
  
  
    const onUbicacionConcedida = ubicacion => {
      console.log("Tengo la ubicación: ", ubicacion);
      const coordenadas = ubicacion.coords;
      $id_latitud.innerText = coordenadas.latitude;
      $id_longitud.innerText = coordenadas.longitude;
      $enlace.href = `https://www.google.com/maps/@${coordenadas.latitude},${coordenadas.longitude},20z`;
    }
    const onErrorDeUbicacion = err => {
  
      $id_latitud.innerText = "Error obteniendo ubicación: " + err.message;
      $id_longitud.innerText = "Error obteniendo ubicación: " + err.message;
      console.log("Error obteniendo ubicación: ", err);
    }
  
    const opcionesDeSolicitud = {
      enableHighAccuracy: true, // Alta precisión
      maximumAge: 0, // No queremos caché
      timeout: 5000 // Esperar solo 5 segundos
    };
  
    $id_latitud.innerText = "Cargando...";
    $id_longitud.innerText = "Cargando...";
    navigator.geolocation.getCurrentPosition(onUbicacionConcedida, onErrorDeUbicacion, opcionesDeSolicitud);
  
  };
  
  document.addEventListener("DOMContentLoaded", funcionInit);
 