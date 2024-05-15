
    document.addEventListener('DOMContentLoaded', () => {
      const menuStatusToggles = document.querySelectorAll('.menu-status-toggle');
  
      menuStatusToggles.forEach(toggle => {
        toggle.addEventListener('change', async (event) => {
          const menu_id = event.target.dataset.menu_id;
          const isChecked = event.target.checked;
  
          try {
            const response = await fetch(`/api/menus/menu/${menu_id}`, {
              method: 'PUT',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                estado_menu: isChecked
              })
            });
  
            if (response.ok) {
              console.log(`Estado del menú con ID ${menu_id} actualizado`);
            } else {
              console.error(`Error al actualizar el estado del menú ${menu_id}`);
              // Vuelve a cambiar el estado del checkbox si hay un error
              event.target.checked = !isChecked;
            }
          } catch (error) {
            console.error('Error en la solicitud:', error);
            // Vuelve a cambiar el estado del checkbox si hay un error
            event.target.checked = !isChecked;
          }
        });
      });
    });