document.addEventListener("paste", function(e) {
    if (e.target.closest('.ace_editor')) {
      e.preventDefault();
      e.stopPropagation();
      alert(
        "El pegado de texto está desactivado para este ejercicio. Por favor escribe tu código."
      );
    }
  }, true);
