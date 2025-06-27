const form = document.getElementById("study-form");
const logList = document.getElementById("log-list");
const chartCanvas = document.getElementById("studyChart");

let logs = JSON.parse(localStorage.getItem("studyLogs")) || [];

function saveLogs() {
  localStorage.setItem("studyLogs", JSON.stringify(logs));
}

function renderLogs() {
  logList.innerHTML = "";
  logs.forEach((log, index) => {
    const li = document.createElement("li");
    li.textContent = `${log.date} – ${log.subject}: ${log.hours} hour(s)`;
    logList.appendChild(li);
  });
}

function updateChart() {
  const dataByDate = {};

  logs.forEach(log => {
    if (!dataByDate[log.date]) dataByDate[log.date] = 0;
    dataByDate[log.date] += Number(log.hours);
  });

  const labels = Object.keys(dataByDate);
  const data = Object.values(dataByDate);

  if (window.studyChart) window.studyChart.destroy();

  window.studyChart = new Chart(chartCanvas, {
    type: "bar",
    data: {
      labels,
      datasets: [{
        label: "Study Hours",
        data,
        backgroundColor: "#4CAF50"
      }]
    },
    options: {
      scales: {
        y: { beginAtZero: true }
      }
    }
  });
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const date = document.getElementById("date").value;
  const subject = document.getElementById("subject").value;
  const hours = document.getElementById("hours").value;

  if (date && subject && hours) {
    logs.push({ date, subject, hours });
    saveLogs();
    renderLogs();
    updateChart();
    form.reset();
  }
});

// On page load
renderLogs();
updateChart();
