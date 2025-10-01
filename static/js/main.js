// Utility functions
function showAlert(message, type = "info") {
  const alertDiv = document.createElement("div")
  alertDiv.className = `alert alert-${type}`
  alertDiv.textContent = message

  const container = document.querySelector(".container") || document.body
  container.insertBefore(alertDiv, container.firstChild)

  setTimeout(() => {
    alertDiv.remove()
  }, 5000)
}

// API helper
async function apiCall(url, method = "GET", data = null) {
  const options = {
    method,
    headers: {
      "Content-Type": "application/json",
    },
  }

  if (data) {
    options.body = JSON.stringify(data)
  }

  try {
    const response = await fetch(url, options)
    return await response.json()
  } catch (error) {
    console.error("API call failed:", error)
    showAlert("An error occurred. Please try again.", "error")
    return null
  }
}

// Format date
function formatDate(dateString) {
  if (!dateString) return "N/A"
  const date = new Date(dateString)
  return date.toLocaleDateString("en-US", {
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  })
}

// Get risk badge class
function getRiskBadgeClass(riskLevel) {
  const classes = {
    Low: "badge-success",
    Medium: "badge-warning",
    High: "badge-danger",
  }
  return classes[riskLevel] || "badge-info"
}

// Auto-hide alerts
document.addEventListener("DOMContentLoaded", () => {
  const alerts = document.querySelectorAll(".alert")
  alerts.forEach((alert) => {
    setTimeout(() => {
      alert.style.opacity = "0"
      setTimeout(() => alert.remove(), 300)
    }, 5000)
  })
})
