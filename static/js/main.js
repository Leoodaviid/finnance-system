// Função para obter o token CSRF
function getCsrfToken() {
  return document
    .querySelector('meta[name="csrf-token"]')
    .getAttribute("content");
}

// Função para lidar com o logout
function setupLogoutButton() {
  const logoutButton = document.getElementById("logout-button");
  if (logoutButton) {
    logoutButton.addEventListener("click", function () {
      fetch("/auth/logout", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "X-CSRFToken": getCsrfToken(),
        },
      })
        .then((response) => {
          if (response.ok) {
            window.location.href = "/";
          } else {
            alert("Logout failed.");
          }
        })
        .catch((error) => {
          console.error("Error during logout:", error);
        });
    });
  }
}

// Função para lidar com a deleção de transações
function setupDeleteButtons() {
  document.querySelectorAll(".delete-button").forEach(function (button) {
    button.addEventListener("click", function () {
      const transactionId = this.getAttribute("data-id");
      fetch(`/transaction/delete/${transactionId}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "X-CSRFToken": getCsrfToken(),
        },
      })
        .then((response) => {
          if (response.ok) {
            window.location.reload();
          } else {
            alert("Failed to delete the transaction.");
          }
        })
        .catch((error) => {
          console.error("Error during transaction deletion:", error);
        });
    });
  });
}

// Inicializa todas as funções ao carregar o DOM
document.addEventListener("DOMContentLoaded", function () {
  setupLogoutButton();
  setupDeleteButtons();
});
