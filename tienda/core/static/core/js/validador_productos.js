$("#formulario_productos").validate({
  rules: {
    categoria: {
      required: true,
    },
    nombre: {
      required: true,
      minlength: 3,
    },
    descripcion: {
      required: true,
      minlength: 3,
      maxlength: 200
    },
    precio: {
      required: true,
      number: true,
      min: 0
    },
    descuento_subscriptor: {
      required: true,
      number: true,
      min: 0,
      max: 100,
    },
    descuento_oferta: {
      required: true,
      number: true,
      min: 0,
      max: 100,
    },
    imagen: {
      required: true,
    },
  }, // --> Fin de reglas
  messages: {
    categoria: {
      required: "La categoría es un campo requerido",
    },
    nombre: {
      required: "El nombre es un campo requerido",
      minlength: "El nombre tiene que ser mínimo de 3 caracteres",
    },
    descripcion: {
      required: "La descripción es un campo requerido",
      minlength: "La descripción debe tener un mínimo de 3 caracteres",
      maxlength: "La descripción debe tener un máximo de 400 caracteres",
    },
    precio: {
      required: "El precio es un campo requerido",
      number: "El precio debe ser un número",
      min: "El precio debe ser mayor o igual a 0",
    },
    descuento_subscriptor: {
      required: "El descuento subscriptor es un campo requerido",
      number: "El descuento debe ser un número",
      min: "El descuento debe ser mayor o igual a 0",
      max: "El descuento debe ser menor o igual a 100",
    },
    descuento_oferta: {
      required: "El oferta subscriptor es un campo requerido",
      number: "El oferta debe ser un número",
      min: "El oferta debe ser mayor o igual a 0",
      max: "El oferta debe ser menor o igual a 100",
    },
    imagen: {
      required: "La imagen es un campo requerido",
    },
  }, 
});